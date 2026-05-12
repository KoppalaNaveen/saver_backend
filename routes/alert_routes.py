from flask import Blueprint, request, jsonify
from services.firestore_service import get_vehicle_by_plate
from utils.normalize import normalize_plate

alert_routes = Blueprint("alert_routes", __name__)

@alert_routes.route("/alert", methods=["POST"])
def handle_alert():
    try:
        data = request.get_json()

        plate = normalize_plate(data.get("plate", ""))

        if not plate:
            return jsonify({
                "success": False,
                "message": "Plate required"
            }), 400

        vehicle = get_vehicle_by_plate(plate)

        if not vehicle:
            return jsonify({
                "success": False,
                "message": "Vehicle not found"
            }), 404

        return jsonify({
            "success": True,
            "phone": vehicle.get("emergencyPhone")
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "message": str(e)
        }), 500