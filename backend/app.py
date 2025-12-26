from flask import Flask
from dotenv import load_dotenv
import os
from routes import auth_routes

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(auth_routes)

@app.route("/")
def home():
    return "Backend running successfully"

if __name__ == "__main__":
    app.run(debug=True)
