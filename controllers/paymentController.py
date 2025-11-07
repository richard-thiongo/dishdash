from flask import jsonify
from services.payment import PaymentService

class PaymentController:
    def __init__(self):
        self.payment_service = PaymentService()

    def checkout(self, request):
        data = request.get_json()
        employee_id = data.get("employee_id")
        amount = data.get("amount")
        phone = data.get("phone")

        if not all([employee_id, amount, phone]):
            return jsonify({"message": "Missing required fields"}), 400

        result = self.payment_service.checkout(employee_id, amount, phone)

        if result["success"]:
            return jsonify({
                "message": result["message"],
                "payment_id": result["payment_id"],
                "payment_code": result["payment_code"],
                "mpesa_response": result["mpesa_response"]
            }), 200
        else:
            return jsonify({"message": result["message"]}), 500
