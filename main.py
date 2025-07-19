from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
from predict import predict_headline
import os

app = Flask(__name__,static_folder='news-classifier-frontend/build', static_url_path='/')
CORS(app)  # This enables CORS globally

@app.route('/predict', methods=['POST'])
@cross_origin(origin='http://localhost:3000')  # Allow requests from React
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)

        headline = data.get("headline")
        if not headline:
            raise ValueError("Headline is missing or empty")

        label = predict_headline(headline)
        print("Predicted label:", label)

        return jsonify({"label": label})  # Send correct JSON
    except Exception as e:
        print("Error in /predict:", str(e))
        return jsonify({"error": str(e)}), 500
    
# Serve React static files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')
    
if __name__ == "__main__":
    app.run(debug=True)
