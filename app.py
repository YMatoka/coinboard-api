# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import json
import requests

app = Flask(__name__)
API_URL = "https://api.coingecko.com/api/v3/"

@app.route("/")
def hello():
    return "The coinboard"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/api/trending')
def trending():
    
    API_TREND_URL = API_URL + "search/trending/"
    response = requests.get(API_TREND_URL)
    content = json.loads(response.content.decode('utf-8'))
    
    if response.status_code != 200:
        return jsonify({
            'status': 'error',
            'message': 'La requête à l\'API météo n\'a pas fonctionné. Voici le message renvoyé par l\'API : {}'.format(content['message'])
        }), 500

    data = []
    for elem in content["coins"]:
        data.append(elem["item"])

    return jsonify(data)
    pass

@app.route('/api/currency_details/<id_currency>')
def currensy_details(id_currency):
    
    currency = id_currency
    API_CURRENCY_URL = API_URL + "coins/" + currency
    response = requests.get(API_CURRENCY_URL)
    content = json.loads(response.content.decode('utf-8'))
    
    if response.status_code != 200:
        return jsonify({
            'status': 'error',
            'message': 'La requête à l\'API météo n\'a pas fonctionné. Voici le message renvoyé par l\'API : {}'.format(content['message'])
        }), 500

    return jsonify(content)
    pass



@app.route('/api/all_currencies')
def all_currencies():
    url = API_URL + "coins/markets?vs_currency=eur&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    response = requests.get(url)
    content = json.loads(response.content.decode('utf-8'))
    if response.status_code != 200:
        return jsonify({
            'status': 'error',
            'message': 'bad request.'
        })
    else:
        return jsonify(content)
    pass
    
if __name__ == "__main__":
    app.run(debug=True)
