from flask import Flask, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
import firebase_admin
from firebase_admin import credentials
import os
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )
    CORS(app)

    # Khởi tạo MongoDB
    mongo_uri = os.getenv("MONGO_URI")
    app.db = MongoClient(mongo_uri)["sentiment_db"]

    # Khởi tạo Firebase
    cred = credentials.Certificate("firebase-auth.json")
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)

    # Đăng ký blueprint
    from app.routes.sentiment import sentiment_blueprint
    from app.routes.stats import stats_blueprint
    from app.routes.admin import admin_blueprint

    app.register_blueprint(sentiment_blueprint)
    app.register_blueprint(stats_blueprint)
    app.register_blueprint(admin_blueprint)

    # Route phục vụ ảnh từ thư mục 'anh' ngang hàng với backend
    @app.route('/anh/<path:filename>')
    def serve_anh(filename):
        # Đường dẫn tuyệt đối tới thư mục 'anh'
        anh_dir = os.path.abspath(os.path.join(app.root_path, '..', 'anh'))
        return send_from_directory(anh_dir, filename)

    return app