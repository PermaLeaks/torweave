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


z = generate_wallet()
print(z)
print(z["n"])

jwktopub("xWSk11EQWRz5cFwlgapT-APSKRzof_Rn3fF6GkL2Hz7n11I6x48MC6MBxLUehGJ0cnyu3xAM2hzyz6_eEeLIMXh5qwDnbngAmb9rr80EP3Joqpbu2NuavpYbSZgTaQa74G_10TNOAxCM7N9n_ujca3WaBBMrcL_vYY0KpguYMjXrIWwrC5ZwFwUsJVe-FhQCmMtxNVByCGSoPaF1VNcWWsVLAMe7Jsb_7jWRRtQrmhp31WWZ1ignGAakcEsh4DXRf1BuAwiNrotZ0kZxOpe6i6I-MqRjM0Ex3IgmZZVPCyEz0ks6_9ljpWV1Hbng5OH6acvtOCqTXlN2I2nugXq1BmHXEnYypS9m5QL2UeoRGfKSQk-lToUtLN84ASegHioMVGh-M3qZUYHi8IESZqCXycr_fO__0faM7xsEe666ZCOya_1AT3skxaMev3JjREcGVHFDA0mki_d-FHOFXifgIARoA3hSIBXqxbaaARoY40CMrq47df6MsRBsuj9cpbdOB9GXoy32ZbDLfDWaEoPrgFhLzpblr09cGuYnCtW2vtBnZdAnYG8ej9-n2UbWtJw-haaTNrT_Xccj7-jF3oipjM2IzeYF8h4o5Xlsz6eOnzCcJR3NWlOUudHa_62kFtb4Jot4evxNkW9807ZmEbdJIiISGJpqt-64iGXC3jzQWvs")

#{'kty': 'RSA', 'e': 'AQAB', 'n': 'xWSk11EQWRz5cFwlgapT-APSKRzof_Rn3fF6GkL2Hz7n11I6x48MC6MBxLUehGJ0cnyu3xAM2hzyz6_eEeLIMXh5qwDnbngAmb9rr80EP3Joqpbu2NuavpYbSZgTaQa74G_10TNOAxCM7N9n_ujca3WaBBMrcL_vYY0KpguYMjXrIWwrC5ZwFwUsJVe-FhQCmMtxNVByCGSoPaF1VNcWWsVLAMe7Jsb_7jWRRtQrmhp31WWZ1ignGAakcEsh4DXRf1BuAwiNrotZ0kZxOpe6i6I-MqRjM0Ex3IgmZZVPCyEz0ks6_9ljpWV1Hbng5OH6acvtOCqTXlN2I2nugXq1BmHXEnYypS9m5QL2UeoRGfKSQk-lToUtLN84ASegHioMVGh-M3qZUYHi8IESZqCXycr_fO__0faM7xsEe666ZCOya_1AT3skxaMev3JjREcGVHFDA0mki_d-FHOFXifgIARoA3hSIBXqxbaaARoY40CMrq47df6MsRBsuj9cpbdOB9GXoy32ZbDLfDWaEoPrgFhLzpblr09cGuYnCtW2vtBnZdAnYG8ej9-n2UbWtJw-haaTNrT_Xccj7-jF3oipjM2IzeYF8h4o5Xlsz6eOnzCcJR3NWlOUudHa_62kFtb4Jot4evxNkW9807ZmEbdJIiISGJpqt-64iGXC3jzQWvs', 'd': 'sJb3OYFWBML9DF4DV9sPP8P7UbiA72exPEb5m2DoWs-mDWWNHFaGyipMPLRj1r9Vuc59iyUKul5HgzGsk4e03T0Qa8FlSdilgOZU6nOZJ0GtDV_10Z-08mfLha09QCo8De9blIo3clpuGMNMgCnGd4RAAwE7TaUH_Nd2_VFGGTVPYxkn8Tfmk1GXStkSPyIrqJHod2--dG_Ia0p0cy_w2cfC77G_ZlOFRpA5pYnOcBDZv9kjJQnK352hoqw0ZCcBgsprgN84ETytYIaQaYCv7Jd62UdjT8k1WDudTiejDSvo9mtDHvxWPvNjMPLHlTvtEJTVZfgA2tQDzm7IZqFmK_nMDIOZd-YVDV9WTMrGbcUe0p-vlnc9QQat5NR-opvk7XwTGnFYDeuQJuQF6oPRFfORSHf76CIMLT_f0qJDWWWw3Znh29l0QmYCftA8NULUpMqItrmaQ8FOWIH4Y_0PK5QcvmP3zlwPqNvCyfa1eoeA0PuwtLRuAqPXJ2Yc0XnnhMOqfCOTE27b5h_vdIfQPuL9rThBh98GSfXZfmS_0uI7EtJQnwnoXV6Gczsvl24R1CzPua0XHQIR9lUTt9xVLESkSXKPExn7VmAp2U2NMV2CiQXjShKYREKX_UNWyFMT3gewEs7pU_5yBa_siyrt696-iEQGgU6sKgURb-w1pDE', 'p': '9PyptZ9-8bCJ-aewiCbDF29iMgRO36BePQIeX3MXDP2w32jnj6Bn-IlrnDPw8uBFyOFpJ6MSw4tIklXwOkakmFfYYDye3AyPgmERvtWvwUplIcWEia9P4xLDWFTiO-rTCi75g-hNdkRDv_Xz5KQjLlanRF1P0ZgFVbflAuEPRRO9yUKtqAaKg8JW3N83jfuSP3_gKfDLKh5qDboh1G8UTDLHYiR7vbp_VH5Ejq7Bd5Ne_i4-vfF42Vd6MpOxTHNvfce19FVv1jc2EEaCVB8P-ALHpuHUpVI9wCVax9ifjwaytYVqqcXvim9JF3YjdSLS2knvkw1p5DakQTVqbP_ULQ', 'q': 'zkREGAHJWlw6PAl5sAHCEdgdnAIP8DdSQO6-EV4DenbpCywPfoA6qBI0pe_5phYQ4b-kMLd_NLvy7XhmS_efZ0Kicm1f5it3vpTFVDafMHNgTpETvw3dIXKwJKScsrOMlvuO6otmDxR5lSH4VL90EN57MJvOCjj5O6MnCfjBdeHihLBxqtzDEukKQiYeDrVmdqLVjhpPdaa5ShNYompT8J0lIoB2zoIm6_Tw68568omFK1nS0jmTL3SxsToTYtcpMFlUsarlLu5_Bl0uTRf5ku5OWKjkQbXblYL1wcWmwvFeejhs-Ow0C_UHM8SlgiEuGhKwkSnhdjyV0ERAFKOcxw', 'dp': '1YjA16jsufcZXDzYduPqWivgmB3_LZYXbe_Bz4p-Rfl9yE0kwKCc3xnQbPctBlWLHfuzbzQJb92gZMR5PiJC5vJyi_dqs_xSvd6j3AVfSwfwPE5wJp5i8FZzZDOgeX9FcXPeUiYSFoqLzu6vJdQXQhWPd9wpbVOnGr7N4wOODrSVUK5ItNL2ur-SfLQnNR9YqvZnycazHsQhxlM9l282bvA3r4iDPq0mvNvOH9uckAAo5T4ju-WUY0SHIzxuZmebfzOqmgw6DapT-j2q7W2hupeZtBDVC0AyyJ8GkHh1IvJApE1k2hPHpY84UzXK1BeFV3ToV_FyIdOquZe4asdWBQ', 'dq': 'b88XbkABqqaVtpeYS-0YCt4wZrHDe_4w6xu_EeD5V7f_aVvv5i2SHisIOO7VT89kRUrBsNq27Jn4-_qo0QMgeDPppMdfFYB4f2lbcePN9NCF4vDHWGgmdwwZKTPF8SRc0Db6aG852nDJ2yo315CUVNSUyGuci3QIvegZsFEUZVcVl8GhS_IxGB4Uvni1EFoKecKYqlfevLKse9fy0s96QtKcH5CtVhG9EWiL8_bQNIqREke1fNlSzIWgEKaffZOOMzQpMcmmRANp_cQi5g1Z7uiYtXyPhoMSzX_YwbnnRILcKLpPb7tyFw0yY0B0Sw67U8zPw1CFc7cxqlxktAtgXw', 'qi': 'a0kBQY7k5_tVFNo8Mcs1j36-DpIdm3_S5UXvZbTF5KnYv0oLw065SNbpYR4itseOGO8A5SRxAxuRXh0Ry6gnQoJg9GUglrvW02WC_TLvnATnIOHqN4x2_04pQyEleIw88MoaYnqKmnaqc3nYthDWfe7hnI4I7xRM39bQ6_jq0PX74tZBVz4zZZJMxOeR59-I6i99clGrAh8MyDv6JNtDGi0C9p3PnSwytAU8lW37mTKvjok77HWvDWtrytq7TctjXac9xol6cr02EcuieqqlyxLnf3QJMK-WULVw2rnAN2TmPwdGW7Xf2usBJc7HtUsqvtUkthEsw-mIppy-uYA1Bg'}
