from flask import Blueprint, jsonify, current_app, render_template, request
from bson import ObjectId

admin_blueprint = Blueprint('admin_blueprint', __name__)

@admin_blueprint.route('/admin')
def admin_page():
    return render_template('admin.html')

@admin_blueprint.route('/admin/reviews')
def all_reviews():
    # Trả về cả _id để xóa từng review
    reviews = list(current_app.db.reviews.find({}))
    # Chuyển ObjectId thành chuỗi để trả về JSON
    for r in reviews:
        r['_id'] = str(r['_id'])
    return jsonify(reviews)

@admin_blueprint.route('/admin/review/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    result = current_app.db.reviews.delete_one({"_id": ObjectId(review_id)})
    return jsonify({"deleted": result.deleted_count})

@admin_blueprint.route('/admin/reviews', methods=['DELETE'])
def delete_all_reviews():
    result = current_app.db.reviews.delete_many({})
    return jsonify({"deleted": result.deleted_count})