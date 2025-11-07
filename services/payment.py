from db import Database
import functions

class PaymentService:
    def checkout(self, employee_id, amount, phone):
        payment_id = functions.generate_payment_id()
        payment_code = functions.generate_payment_code()

        insert_query = """
            INSERT INTO payments (payment_id, payment_code, payment_amount, employee_id)
            VALUES (%s, %s, %s, %s)
        """
        check_employee_query = "SELECT * FROM employees WHERE employee_id=%s"

        try:
            with Database() as cursor:
                #  Verify employee exists
                cursor.execute(check_employee_query, (employee_id,))
                if cursor.rowcount == 0:
                    return {"success": False, "message": "Employee not found."}

                #  Insert payment
                cursor.execute(insert_query, (payment_id, payment_code, amount, employee_id))

                #  Trigger M-Pesa STK push
                mpesa_response = functions.mpesa_payment(amount, phone, payment_code)

                #  Return success + details
                return {
                    "success": True,
                    "message": "Payment initiated successfully.",
                    "payment_id": payment_id,
                    "payment_code": payment_code,
                    "mpesa_response": mpesa_response
                }
        except Exception as e:
            print("PAYMENT ERROR:", e)
            return {"success": False, "message": str(e)}
