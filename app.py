# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
import json
import requests

app = Flask(__name__)
API_URL = "https://api.coingecko.com/api/v3/"

@app.route("/")
def hello():
    return "Coinboard API"

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route('/api/meteo/<searchedCity>')
def meteo(searchedCity):
    city = searchedCity
    print(searchedCity)
    METEO_API_URL = "https://kraken-weather.herokuapp.com/api/weathers/london"
    response = requests.get(METEO_API_URL)
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
    url = API_URL + "global"
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