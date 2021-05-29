__version__ = "0.1.0"

from . import english
import spacy
from flask import Flask, request, jsonify

spacy.prefer_gpu()

app = Flask(__name__)


@app.route("/")
def home():
    """Privison basic server information"""
    return jsonify(
        {
            "name": "Entity Identification",
            "version": __version__,
        }
    )


@app.route("/api/english", methods=["POST"])
def english_corpus():
    """Recognize entities in text corpus"""
    return jsonify(english.find_entities(request.data.decode("UTF-8")))
