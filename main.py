import os
from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://moviesdatabase.p.rapidapi.com/titles/series/{seriesId}"  # Update seriesId dynamically

    # Example seriesId for demonstration
    series_id = "tt0944947"  # Example series ID for Game of Thrones

    headers = {
        "X-RapidAPI-Key": os.environ.get("RAPIDAPI_KEY"),  # Get the API key from environment variables
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    # Replace the {seriesId} placeholder in the URL with the actual series ID
    url = url.replace("{seriesId}", series_id)

    response = requests.get(url, headers=headers)

    if response.ok:
        series_data = response.json()
        # Render the home template and pass series_data to it
        return render_template('home.html', series_data=series_data)
    else:
        return jsonify({"error": "Failed to fetch data from the API"}), 500

if __name__ == '__main__':
    app.run(debug=True)
