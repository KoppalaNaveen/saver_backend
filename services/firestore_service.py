from config.firebase_config import db


# 🔴 GET VEHICLE USING PLATE NUMBER
def get_vehicle_by_plate(plate):

    try:
        # 🔴 Get all users
        users = db.collection("users").stream()

        # 🔴 Loop through users
        for user in users:

            # 🔴 Search inside each user's vehicles collection
            vehicles = (
                db.collection("users")
                .document(user.id)
                .collection("vehicles")
                .where("plateNumber", "==", plate)
                .stream()
            )

            # 🔴 If vehicle found → return data
            for vehicle in vehicles:

                data = vehicle.to_dict()

                return {
                    "vehicleId": vehicle.id,
                    "userId": user.id,
                    "plateNumber": data.get("plateNumber"),
                    "emergencyPhone": data.get("emergencyPhone"),
                    "ownerName": data.get("ownerName"),
                }

        # 🔴 No vehicle found
        return None

    except Exception as e:
        print("Firestore Error:", e)
        return None