"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp
from .orders.user_routes import user_bp
from .orders.review_routes import review_bp
from .orders.reservation_routes import reservation_bp
from .orders.transaction_routes import transaction_bp
from .orders.blocked_fund_routes import blocked_fund_bp
from .orders.hotel_routes import hotel_bp
from .orders.location_routes import location_bp
from .orders.hotel_network_routes import hotel_network_bp
from .orders.network_routes import network_bp
from .orders.room_routes import room_bp

def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(reservation_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(blocked_fund_bp)
    app.register_blueprint(hotel_bp)
    app.register_blueprint(location_bp)
    app.register_blueprint(hotel_network_bp)
    app.register_blueprint(network_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(room_bp)
