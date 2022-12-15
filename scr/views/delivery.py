import datetime
import json
from flask import Response, jsonify, request
from ..database.models import Delivery
from flask_restful import Resource
from mongoengine.errors import (
    FieldDoesNotExist,DoesNotExist,ValidationError, InvalidQueryError, 
)

from ..utility.errors import  (
   SchemaValidationError, InternalServerError, DeletingDeliveryError, 
   UpdatingDeliveryError, DeliveryNotExistsError
)
from mongoengine.queryset.visitor import Q

class DeliverysApi(Resource):

    def get(self):
        deliverys = Delivery.objects.all()
        return Response( deliverys.to_json(), mimetype="application/json", status=200 )

    def post(self):
        try:
            data = request.get_json()
            delivery = Delivery.objects.create(
                deliver_staff_name = data["deliver_staff_name"],
                location = data["location"],
                status = data["status"],
                created_at = data["created_at"],
            )
            delivery.save()
            return Response(delivery.to_json(), mimetype="application/json", status=200  )
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except Exception as e:
            raise InternalServerError
        

class DeliveryApi(Resource):
    def get(self, id):
        try:
            delivery = Delivery.objects.get(id=id).to_json()
            return Response(delivery, mimetype="application/json", status=200 )
        except:
            return jsonify(
                
                message="that Id does not exist",
                status=404
            )


    def put(self, id):
        try:
            update_delivery = Delivery.objects.get(id=id)
            data = request.get_json()
        
            update_delivery.update(
                deliver_staff_name = data["deliver_staff_name"],
                location = data["location"],
                status = data["status"],
                created_at = data["created_at"],
            )
            update_delivery.save()
            return Response(update_delivery.to_json(), mimetype="application/json", status=200)
        except Exception:
            raise  InternalServerError


class DeliverySearchApi(Resource):
     def get(self):
        deliver_staff_name = request.args.get("deliver_staff_name")
        location = request.args.get("location")
        status  = request.args.get("status")
        created_at = request.args.get("created_at")
        
        if deliver_staff_name:
            deliverys = Delivery.objects(deliver_staff_name__icontains = deliver_staff_name)
        elif location:
            deliverys = Delivery.objects(sale_price__lte = location)
        elif status:
            deliverys = Delivery.objects(status__lte = status)
        elif created_at:
            deliverys =  Delivery.objects(created_at__lte = datetime.datetime.now())
        else:
            return jsonify({
                "messeage":"please enter a valid field and value"
            })
            

        return Response( deliverys.to_json(), mimetype="application/json", status=200 )
        