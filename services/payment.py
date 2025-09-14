from db import Database
import functions

class PaymentService:
    def __init__(self):
        self.db = Database()

    # payment_id 	payment_code 	payment_amount 	employee_id 	
    def checkout(self, payment_code, payment_amount, employee_id):
        