from flask import Blueprint

bp = Blueprint('customer', __name__, url_prefix='/customers')

@bp.route('', methods=['GET'])
def customer():
        return 'customers'