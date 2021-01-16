import requests
import json
from jwcrypto import jwk
import base64
from Crypto.Hash import SHA256, SHA3_256
def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

# Make a request through the Tor connection
# IP visible through Tor
session = get_tor_session()
print(session.get("http://httpbin.org/ip").text)

# Above should print an IP different than your public IP

# Following prints your normal public IP
print(requests.get("http://httpbin.org/ip").text)

def get_network():
    """

    :return:
    """
    network = session.get("https://arweave.net/info").json()
    return network


def get_peers():
    """

    :return:
    """
    peers = session.get("https://arweave.net/peers").json()
    return peers


def current_block():
    """

    :return:
    """
    cur_block = session.get("https://arweave.net/current_block").json()
    return cur_block


def generate_wallet():
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



def jwktopub(n):
    """

    :param n:
    :return:
    """
    h = SHA3_256.new()
    print(str.encode(n))
    h.update(str.encode(n))
    print(h.digest())



    y = base64.urlsafe_b64encode(h.digest())
    print(y)
    print(str(y.decode('utf-8')))



