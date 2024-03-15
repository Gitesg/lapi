import requests
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://baseball4.p.rapidapi.com/v1/mlb/schedule"
    querystring = {"date": "2021-07-30"}
    headers = {
        "X-RapidAPI-Key": os.getenv("apikey"),
        "X-RapidAPI-Host": "baseball4.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data from the API"}), 500

if __name__ == '__main__':
    app.run(debug=True)
