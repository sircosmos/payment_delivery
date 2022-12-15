from datetime import datetime
from app import db

class Payment(db.Document):
    payment_mode = db.StringField(required=True)
    transaction_status = db.StringField(required=False)
    currency = db.StringField(required=True)
    amount_paid = db.IntField()

    meta = {
        "ordering" :["-created_at"]
    }



class Delivery(db.Document):
    deliver_staff_name =db.StringField(required=True)
    location = db.StringField()
    status = db.StringField()

    meta = {
        "ordering" :["-created_at"]
    }


