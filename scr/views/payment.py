import datetime
import json
from flask import Response, jsonify, request
from ..database.models import Payment
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist,DoesNotExist,ValidationError, InvalidQueryError, 
)

from ..utility.errors import  (
   SchemaValidationError, InternalServerError, DeletingPaymentError, 
   UpdatingPaymentError, PaymentNotExistsError
)
from mongoengine.queryset.visitor import Q


class PaymentsApi(Resource):

    def get(self):
        payments = Payment.objects.all()
        return Response( payments.to_json(), mimetype="application/json", status=200 )

    def post(self):
        try:
            data = request.get_json()
            payment = Payment.objects.create(
                payment_mode = data["payment_mode"],
                transaction_status = data["transaction_status"],
                currency = data["currency"],
                amount_paid = data["amount_paid"],
            )
            payment.save()
            return Response(payment.to_json(), mimetype="application/json", status=200  )
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError

class PaymentApi(Resource):
    def get(self, id):
        try:
            payment = Payment.objects.get(id=id).to_json()
            return Response(payment, mimetype="application/json", status=200 )
        except:
            return jsonify(
                
                message="that Id does not exist",
                status=404
            )


class PaymentSearchApi(Resource):
     def get(self):
        payment_mode = request.args.get("payment_mode")
        transaction_status = request.args.get("transaction_status")
        currency  = request.args.get("currency")
        amount_paid = request.args.get("amount_paid")
        
        if payment_mode:
            payments = Payment.objects(payment_mode__icontains = payment_mode)
        elif transaction_status:
            payments = Payment.objects(transaction_status__lte = transaction_status)
        elif currency:
            payments = Payment.objects(currency__lte = currency)
        elif amount_paid:
            products = Payment.objects(amount_paid__lte = amount_paid)
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
            

        return Response( payments.to_json(), mimetype="application/json", status=200 )