from flask import Blueprint, request, jsonify
from app.models import db, Customer

bp = Blueprint('customer', __name__, url_prefix='/customers')

@bp.route('', methods=['POST'])
def add_customer():
    data = request.json
    customer = Customer(name=data['name'], code=data['code'])
    db.session.add(customer)
    db.session.commit()
    
    return jsonify({'message': 'Customer added!'}), 201