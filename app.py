from flask import Flask
from scr.database.db import initialize_db
from scr.urls.routes import initialize_routes
from flask_restful import Api
import psycopg2





app = Flask(__name__)

# database connection

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost/payment-delivery-DB'



api = Api(app, )


initialize_db(app)
initialize_routes(api)




app.run()