from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import customer, order

    app.register_blueprint(customer.bp)
    app.register_blueprint(order.bp)

    

    return app