from flask import Blueprint

bp = Blueprint('order', __name__, url_prefix='/orders')

@bp.route('', methods=['GET'])
def order():
        return 'orders'