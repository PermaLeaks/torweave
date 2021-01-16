# torweave

<h2>requirements</h2>
To run torweave as intended, it's required to install TOR (software not the browser) on your system and run a TOR circuit

On linux:
```
> apt-get install tor
> tor
```

<h2>Install</h2>

```
> python -m pip install torweave
```

if any error occured while building wheels of different packages, please try the following:
```
> sudo pip install torweave
```

<h2>plain english</h2>

<b>Why Tor?</b>
Onion routing is implemented by encryption in the application layer of a communication protocol stack, nested like the layers of an onion. Tor encrypts the data, including the next node destination IP address, multiple times and sends it through a virtual circuit comprising successive, random-selection Tor relays. Each relay decrypts a layer of encryption to reveal the next relay in the circuit to pass the remaining encrypted data on to it. The final relay decrypts the innermost layer of encryption and sends the original data to its destination without revealing or knowing the source IP address [wikipedia]("https://en.wikipedia.org/wiki/Tor_(anonymity_network)")

And as The Arweave protocol is based on HTTP, it was possible to mask your requests IP address before sending any request/query to the node.

<b>Arweave Over Tor</b>
torweave is a python package built over Arweave HTTP api to make anonymous requests assuring `sender` privacy. we used `arweave-python-client` package to accelerate the developments. And since that package miss several essential functionalities like generating wallets, `/last_tx` issues and more, we have fixed it in torweave.

it's not required to use `torweave` in intention to post/publish leaks on <a href="https://permaleaks.org">permaleaks.org</a>, but if you are a user who cares about his ultimate privacy and refuse to share his IP with Arweave's peer, you can use `torweave`. For non-technical users, permaleaks UI provide an easy way to publish files on the platform.
