import os
import requests
from flask import Flask, jsonify, send_file
from bs4 import BeautifulSoup as bs
from flask_cors import CORS, cross_origin
import urllib.request
from PIL import Image
app = Flask(__name__)
CORS(app)

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

@app.route('/imagem/<string:tokenide>/')
def editor_oficial(tokenide):

	url = f"https://api-mainnet.magiceden.dev/v2/tokens/{tokenide}"
	
	ak = requests.get(url)
	res = ak.json()
	print(res)
	if 'errors' in res or "status" in res:
		return "NO"
	else:
		imagem = res["image"]
		if ".gif" in imagem:
			return "GIF"
		else:
			urllib.request.urlretrieve(imagem, f"{tokenide}.png") 
			os.system("ls")
			img1 = Image.open("quadro.jpg") 
			img2 = Image.open(f"{tokenide}.png") 
			img2 = img2.resize((339, 339), Image.ANTIALIAS)
			img1.paste(img2, (141,131)) 
			img1.save(f"{tokenide}_final.jpg") 
			
			return send_file(f"{tokenide}_final.jpg", mimetype='image/jpg')
			
			os.remove(f"{tokenide}.png")
			os.remove(f"{tokenide}_final.jpg")
			

