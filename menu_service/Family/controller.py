from flask import Blueprint, request, jsonify
from .services import AI_generate_family_meal

family_bp = Blueprint("family_bp", __name__)

# API tạo thực đơn cho gia đình
@family_bp.route("/generate-family-meal", methods=["POST"])
def generate_family_meal():
    try:
        data = request.json
        family_id = data.get("family_id")

        if not family_id:
            return jsonify({"error": "Thiếu family_id"}), 400

        # Gọi hàm tạo thực đơn gia đình
        AI_generate_family_meal(family_id)
        return jsonify({"message": "Thực đơn gia đình đã được tạo thành công"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
