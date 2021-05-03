from flask import Flask, request
from flask import jsonify
import json
import markdown.extensions.fenced_code
import tools.getdata as get
import tools.postdata as pos




app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

@app.route("/tweets/<person>")
def frasespersona(person):
    tweets = get.mensajespersona(person)
    return jsonify(tweets)

@app.route("/favorites/<fav>")
def frasesfavorites(fav):
    tweets = get.mensajesfavorites(fav)
    return jsonify(tweets)

@app.route("/locations/<location>")
def fraseslocation(location):
    tweet = get.mensajeslocation(location)
    return jsonify(tweet)

@app.route("/dates/<date>")
def frasesdate(date):
    tweets = get.mensajesdate(date)
    return jsonify(tweets)

@app.route("/hashtags/<hashtag>")
def fraseshashtag(hashtag):
    text = get.mensajeshashtag(hashtag)
    return jsonify(text)

@app.route("/date/<d>/hashtags/<h>")
def date_fav(d,h):
    tweet = get.date_hashtag(d,h)
    return jsonify(tweet)

@app.route("/locations/<l>/dates/<d>/hashtags/<h>")
def location_day_hash(l,d,h):
    tweet = get.location_date_hashtag(l,d,h)
    return jsonify(tweet)


@app.route("/nuevafrase", methods=["POST"])
def inserttweet():
    user_name = request.form.get("user_name")
    user_location = request.form.get("user_location")
    day = request.form.get("date")
    favorites = request.form.get("favorites")
    text = request.form.get("text")
    pos.insert_tweet(user_name,user_location,day,favorites,text)
    return "ok"







app.run(debug=True)
