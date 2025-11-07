import bcrypt
import re
import requests, base64, datetime, uuid
from requests.auth import HTTPBasicAuth


def hash_password(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash.decode()


def hash_verify(password, hashed_password):
    bytes = password.encode('utf-8')
    result = bcrypt.checkpw(bytes, hashed_password.encode())
    return result


def is_valid_password(password, min_len=8, max_len=64):
    return min_len <= len(password) <= max_len


def is_valid_email(company_email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, company_email) is not None


#  Generate a UUID-based payment_id
def generate_payment_id():
    return str(uuid.uuid4())


#  Generate a shorter random code (for Mpesa reference)
def generate_payment_code():
    return str(uuid.uuid4())[:8].upper()


def mpesa_payment(amount, phone, invoice_no):
    try:
        consumer_key = "Wh1HKC40sASaGZENt6F8th2NarA3TvPDiYbEM8Ru9SxcZh17"
        consumer_secret = "hj1KWY7O30tAEhqZRElpUU3QP25ov9hOEGTG70MgoOfdpmSk6vkHunl3hDzGpAXG"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        access_token = "Bearer " + r.json()['access_token']

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        password = base64.b64encode(data.encode()).decode('utf-8')

        payload = {
            "BusinessShortCode": business_short_code,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": 1,
            "PartyA": phone,
            "PartyB": business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
            "AccountReference": str(invoice_no),
            "TransactionDesc": "Payment for order"
        }

        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    except Exception as e:
        print("M-PESA ERROR:", e)
        return {"error": str(e)}
