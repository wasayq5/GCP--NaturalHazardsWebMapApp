import os
import firebase_admin
from flask import Flask
from firebase_admin import firestore

firebase_app = firebase_admin.initialize_app()
db = firestore.Client()

app = Flask(__name__)

@app.route("/")

def hello_world():
    return f"Hello World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))