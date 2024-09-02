# from flask import Flask, request, render_template
# import recommendation

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         anime_name = request.form["anime_name"]
#         recommendations = recommendation.get_recommendations(anime_name)
#         return render_template("index.html", recommendations=recommendations, anime_name=anime_name)
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import pandas as pd
import recommendation

app = Flask(__name__)

# Load your dataset
df = pd.read_csv('anime_data.csv')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    anime_name = None
    recommendations = None
    
    # Get the list of anime names
    anime_names = df['Name'].tolist()

    if request.method == 'POST':
        anime_name = request.form.get('anime_name')
        recommendations = recommendation.get_recommendations(anime_name)  # Assume this function is defined

    return render_template('index.html', anime_name=anime_name, recommendations=recommendations, anime_names=anime_names)

if __name__ == '__main__':
    app.run(debug=True)
