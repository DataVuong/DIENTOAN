from flask import Blueprint, request, jsonify, current_app, render_template
from app.services.analysis import analyze_sentiment
from firebase_admin import auth
from datetime import datetime

sentiment_blueprint = Blueprint('sentiment_blueprint', __name__)

@sentiment_blueprint.route('/')
def index():
    return render_template('index.html')

@sentiment_blueprint.route('/analyze', methods=['POST'])
def analyze():
    try:
        id_token = request.headers.get("Authorization")
        decoded_token = auth.verify_id_token(id_token)
        uid, email = decoded_token['uid'], decoded_token['email']

        text = request.json.get("text", "")
        food = request.json.get("food", "")  # Lấy tên món ăn từ request
        result = analyze_sentiment(text)

        current_app.db.reviews.insert_one({
            "uid": uid,
            "email": email,
            "text": text,
            "food": food,  # Lưu tên món ăn vào database
            "sentiment": result,
            "created_at": datetime.utcnow()
        })

        return jsonify({"sentiment": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400