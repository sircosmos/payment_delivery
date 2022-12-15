from ..views.payment import PaymentsApi, PaymentApi, PaymentSearchApi
from ..views.delivery import DeliveryApi, DeliverysApi, DeliverySearchApi


def initialize_routes(api):
    api.add_resource(PaymentsApi, "/api/payments")
    api.add_resource(PaymentApi, "/api/payment/<id>")
    api.add_resource(PaymentSearchApi, '/api/payments/search/')

    api.add_resource(DeliverysApi, "/api/deliverys")
    api.add_resource(DeliveryApi, "/api/delivery/<id>")
    api.add_resource(DeliverySearchApi, "/api/deliverys/search/")

    