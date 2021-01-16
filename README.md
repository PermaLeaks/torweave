# torweave

<h1>requirements</h1>
To run torweave as intended, it's required to install TOR (software not the browser) on your system and run a TOR circuit

If you're using Debian, just run as root:
```
> apt-get install tor
> tor
```

<h1>Install</h1>

```
> python -m pip install torweave
```

if any error occured while building wheels of required packages, please try the following:
```
> sudo pip install torweave
```

<h1>Plain English</h1>

<h2>Why Tor?</h2>
<br>
Onion routing is implemented by encryption in the application layer of a communication protocol stack, nested like the layers of an onion. Tor encrypts the data, including the next node destination IP address, multiple times and sends it through a virtual circuit comprising successive, random-selection Tor relays. Each relay decrypts a layer of encryption to reveal the next relay in the circuit to pass the remaining encrypted data on to it. The final relay decrypts the innermost layer of encryption and sends the original data to its destination without revealing or knowing the source IP address [wikipedia]

And as The Arweave protocol is based on HTTP, it was possible to mask your requests IP address before sending any request/query to the node.

<h2>Arweave Over Tor</h2>
<br>
torweave is a python package built over Arweave HTTP api to make anonymous requests assuring `sender` privacy. we used `arweave-python-client` package to accelerate the developments. And since that package miss several essential functionalities like generating wallets, `/last_tx` issues and more, we have fixed it in torweave.

it's not required to use `torweave` in intention to post/publish leaks on <a href="https://permaleaks.org">permaleaks.org</a>, but if you are a user who cares about his ultimate privacy and refuse to share his IP with Arweave's peer, you can use `torweave`. For non-technical users, permaleaks UI provide an easy way to publish files on the platform.
<br>
<b>DNS Leakage</b>
<br>
torweave protects users from DNS leakage. Sending HTTP requests may ***(not always)*** leak your DNS to the public.
Information that might be leaked:
- Your IP: xxx.xxx.xx
- DNS IP: xxx.xxx.xx.xx
- Hostname: xxx.xxx.xx.xx
- ISP: ISP registred name
- Country: ...
- City: ...

<h2>Why not just using VPN?</h2>

In principle, ***VPNs emphasize privacy, and Tor emphasizes anonymity***. While there’s some overlap between these two concepts, think of it this way: anonymity hides who you are, and privacy hides what you do.

So, A VPN encrypts your connection and routes it through an intermediary server in another location of the user’s choosing. This server is operated by the VPN provider which is a centralised private third service which holds users information: e-mails, phone numbers, payments data, and more. Over this decade, many VPN services have been over-taken by governements or got servers hacked.

In contracts, Tor encrypts your internet connection and routes it through a random sequence of servers run by volunteers (decentralised). The network sends your data through no less than three relays at random. Your data is encrypted once for each relay, including the IP address of the next relay in the sequence. A layer of encryption is removed at each relay, revealing the next relay in the sequence while hiding it from previous relays in the chain. No one relay can see the contents, source, and destination of internet traffic, making it extremely difficult to trace. 

Using Tor you achieve:

* Anonymous HTTP requests
* Untraceable communication – Journalists and their sources, whistleblowers, activists, dissidents, and victims of crime who wish to remain anonymous can use Tor to securely communicate without being tracked or leaving behind a trail of evidence | PermaLeaks will launch later an enhanced version of weavemail protocol to add more anonymoty for on-chain communication.

**VPN point of failure:** <br>
A VPN can hide your IP address, but the VPN provider can still see connection data and traffic passing through its servers. Although most VPN providers say they don’t keep logs of this information, using them for anonymity still requires trusting the VPN provider, whereas Tor uses a trustless system.
