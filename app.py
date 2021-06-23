import os
import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup as bs
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

@app.route('/cp/<string:cpf>/')
def consul_cpf(cpf):
	url = requests.get(f"http://api.trackear.com.br/basepv/cpf/{cpf}/noip").json()
	if "Formato de CPF Invalido!" in url or "Sem Resultado!" in url:
		return jsonify({"status": "INVALIDO"})
	else:
		nome = url["nome"]
		idade = url["idade"]
		return jsonify({"status": "EXISTENTE", "nome": nome, "idade": idade})

def main():
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
	
	
if __name__ == "__main__":
	main()
