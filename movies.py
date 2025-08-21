from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    movies = []
    if request.method == "POST":
        year = request.form.get("year")
        if year:
            url = f"http://www.omdbapi.com/?s=movie&y={year}&apikey=4ad22508"
            response = requests.get(url)
            data = response.json()
            if data.get("Search"):
                movies = data["Search"]
    return render_template("index.html", movies=movies)

if __name__ == "__main__":
    app.run(debug=True)
