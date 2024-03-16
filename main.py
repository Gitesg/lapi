import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://baseball4.p.rapidapi.com/v1/mlb/schedule"

    querystring = {"date": "2021-07-30"}

    headers = {
        "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "baseball4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.ok:
        series_data = response.json()
        return jsonify(series_data)
    else:
        return jsonify({"error": "Failed to fetch data from the API"}), 500

    app.run(debug=True)
