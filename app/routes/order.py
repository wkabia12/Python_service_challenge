from flask import Blueprint, request, jsonify
from app.models import db, Order

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('', methods=['POST'])
def add_order():
    data = request.json
    order = Order(customer_id=data['customer_id'], item=data['item'], amount=data['amount'])
    db.session.add(order)
    db.session.commit()

    return jsonify({'message': 'Order added and SMS sent!'}), 201