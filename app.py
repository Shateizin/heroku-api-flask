import os
import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup as bs
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

@app.route('/cp/<string:cpf>/')
def consul_cpf(cpf):
	url = requests.get(f"http://3.223.192.184/CPF/api.php?lista={cpf}").text
	soup = bs(url, 'html.parser')
	if url == "":
		return "{'status': 'NÃO VALIDO'}"
	else:
		resul = soup.find("b").text
		resul = resul.replace("NOME", "").replace("CONSULTADO COM SUCESSO", "").replace("➜", "").replace("|", "").replace("SEXO", "").replace("NASCIMENTO", "").replace(":", "").replace("IDADE", "").replace("CPF", "").replace("DATA DA CONSULTA", "").replace("Seg", "").replace("MASCULINO", "").replace("3", "").replace("2", "").replace("/", "").replace("1", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("FEMININO", "").replace("0", "")
		return jsonify({"status": "EXISTENTE", "nome": resul})

def main():
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
	
	
if __name__ == "__main__":
	main()
