from flask import Flask

app = Flask(__name__)

@app.route('/solana/<string:address>/')
def consul_nft(address):
	url = f"https://nfteyez.global/api/accounts/{address}"
	ugi = []
	imagens = []
	nfts = {}
	req = requests.get(url)
	resposta = req.json()
	for c in resposta:
		nome = c["name"]
		update = c["tokenData"]
		update = update["updateAuthority"]
		if update in nfts:
			nfts[update].append(nome)
		else:
			nfts[update]  = [nome]
	return jsonify(nfts)