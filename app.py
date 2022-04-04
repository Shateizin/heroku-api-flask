import os
import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup as bs
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)
@app.route('/nft/<string:endereco>/')
def consul_nft(endereco):
	url = f"https://api.nftport.xyz/v0/accounts/{endereco}?chain=polygon"
	header = {"Content-Type": "application/json", "Authorization": "9e1339fe-e3e2-48b5-811f-2efb37253304"}
	ak = requests.get(url, headers=header)
	res = ak.json()
	res = res['nfts']
	nft = {'nft': []}
	for c in res:
		nfts = c['name']
		if nfts == "":
			pass
		else:
			nft['nft'].append(nfts)
	return jsonify(nft)
	
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
	


def main():
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
	
	
if __name__ == "__main__":
	main()
	

