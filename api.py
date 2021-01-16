import requests
import json
from jwcrypto import jwk
import base64
from Crypto.Hash import SHA256
import arweave
from bs4 import BeautifulSoup


class Torweave(object):

    def get_tor(self):

        global session

        session = requests.session()
        # Tor uses the 9050 port as the default socks port
        session.proxies = {'http': 'socks5://127.0.0.1:9050',

                           'https': 'socks5://127.0.0.1:9050'}

        return session

    def check_connection(self):
        html = session.get("https://check.torproject.org").text
        soup = BeautifulSoup(html, "html.parser")
        soup_title = soup.find("title")

        result = \
            str(soup_title).replace("<title>", "")\
            .replace("</title>", "") \
            .strip()

        if result != "Congratulations. This browser is configured to use Tor.":

            raise Exception("Tor is not running. not connected")
        else:
            return "connected"

    def current_ip(self):
        """

        :return: Tor exit router IP adrs
        """
        return session.get("http://httpbin.org/ip").json()["origin"]

    
    def get_real_ip(self):
        """

        :return:
        """
        return requests.get("https://httpbin.org/ip").json()["origin"]

    def get_network(self):
        """

        :return:
        """
        network = session.get("https://arweave.net/info").json()
        return network

    def get_peers(self):
        """

        :return:
        """
        peers = session.get("https://arweave.net/peers").json()
        return peers

    def current_block(self):
        """

        :return:
        """
        cur_block = session.get("https://arweave.net/current_block").json()
        return cur_block
    
    def get_wallets_transactions(self, address):
        """
        
        :return: json list of encoded base64url transactions 
        """
        list = session.get(f"https://arweave.net/wallet/{address}/txs")
        return list
    
    def generate_wallet(self):
        """

        :return: json keyfile
        """
        key = jwk.JWK.generate(kty="RSA", size=4096)
        jwk_obj = jwk.JWK.export(key)

        dict = json.loads(jwk_obj)

        keyfile = {

            "kty": dict["kty"],
            "e": dict["e"],
            "n": dict["n"],
            "d": dict["d"],
            "p": dict["p"],
            "q": dict["q"],
            "dp": dict["dp"],
            "dq": dict["dq"],
            "qi": dict["qi"]

        }

        return keyfile

    def upload_txt(self, tags, filename):
        """

        :param path:
        :param jwk:
        :return:
        """
        wallet = arweave.Wallet('/path_to_/jwk.json')

        # reading .txt content

        with open(filename) as txt:
            content = txt.read()
            txt.close()

            tx_obj = arweave.Transaction(wallet, data=content)

            tx_obj.add_tag('Content Type', 'text/plain')
            for tag, value in tags.items():
                tx_obj.add_tag(tag, value)

            tx_obj.sign()
            tx_obj.send()

            return tx_obj.id



