import os
import requests
from flask import Flask
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
		return "{'status': 'EXISTENTE'}"

def main():
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)
	
	
if __name__ == "__main__":
	main()
