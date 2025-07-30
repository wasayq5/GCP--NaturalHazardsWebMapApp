import os
from flask import Flask
import libsql
import logging

app = Flask(__name__)

url = os.getenv("TURSO_DATABASE_URL")
auth_token = os.getenv("TURSO_AUTH_TOKEN")

print(f"TURSO_DATABASE_URL is {'set' if url else 'NOT set'}")
print(f"TURSO_AUTH_TOKEN is {'set' if auth_token else 'NOT set'}")

if not url or not auth_token:
    raise ValueError("Missing required environment variables!")

conn = libsql.connect("hello.db", sync_url=url, auth_token=auth_token)

conn.sync()

port = int(os.environ.get("PORT", 8080))
logging.info(f"Starting app on port {port}")

@app.route("/")
def hello_world():
    return f"Hello World! Turso DB connected!"

if __name__ == "__main__":
    #host = 0.0.0.0 tells Flask to listen for connections outside of local (since you're deploying publicly)
    #port=int(os.environ.get("PORT", 8080) sets port to the one provided by GCP. If none provided, use local port 8080
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))