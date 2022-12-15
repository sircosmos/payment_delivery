class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class UpdatingPaymentError(Exception):
    pass

class DeletingPaymentError(Exception):
    pass

class PaymentNotExistsError(Exception):
    pass

class FieldDoesNotExistError(Exception):
    pass



errors = {
     "InternalServerError": {
        "message": "Something went wrong on the code",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "UpdatingPaymentError": {
         "message": "Updating Payment added by other is forbidden",
         "status": 403
     },
     "DeletingPaymentError": {
         "message": "Deleting Payment added by other is forbidden",
         "status": 403
     },
     "PaymentNotExistsError": {
         "message": "Payment with given id doesn't exists",
         "status": 400
     },     
     "FieldDoesNotExistError": {
        "message": "The field is invalid",
        "status": 400
     },

}


### delivery Errors

class UpdatingDeliveryError(Exception):
    pass

class DeletingDeliveryError(Exception):
    pass

class DeliveryNotExistsError(Exception):
    pass

class FieldDoesNotExistError(Exception):
    pass


errors = {
     
    "UpdatingDeliveryError": {
         "message": "Updating Delivery added by other is forbidden",
         "status": 403
     },
     "DeletingDeliveryError": {
         "message": "Deleting Delivery added by other is forbidden",
         "status": 403
     },
     "DeliveryNotExistsError": {
         "message": "Delivery with given id doesn't exists",
         "status": 400
     }, 
     "FieldDoesNotExistError": {
        "message": "The field is invalid",
        "status": 400
     }    
}

