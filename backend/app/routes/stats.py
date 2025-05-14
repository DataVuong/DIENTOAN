from flask import Blueprint, jsonify, current_app, render_template

stats_blueprint = Blueprint('stats_blueprint', __name__)

@stats_blueprint.route('/stats')
def stats_page():
    return render_template('stats.html')

@stats_blueprint.route('/api/stats')
def stats_api():
    # Thống kê số lượng review theo từng loại cảm xúc
    pipeline = [
        {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}
    ]
    stats = list(current_app.db.reviews.aggregate(pipeline))
    return jsonify(stats)

@stats_blueprint.route('/api/stats/food')
def stats_by_food():
    pipeline = [
        {"$group": {
            "_id": {"food": "$food", "sentiment": "$sentiment"},
            "count": {"$sum": 1}
        }}
    ]
    stats = list(current_app.db.reviews.aggregate(pipeline))
    return jsonify(stats)