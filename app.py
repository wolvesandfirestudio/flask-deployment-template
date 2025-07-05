from flask import Flask
from flask_cors import CORS

# Create Flask app
app = Flask(__name__)

# Basic CORS config for local and deployed frontend
CORS(app,
     origins=[
         "http://localhost:5173",
         "https://your-frontend-domain.com"
     ],
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "OPTIONS"]
)

# Health check route
@app.route("/", methods=["GET"])
def index():
    return {"message": "Backend is alive!"}

# Run app
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)