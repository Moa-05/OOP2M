from flask import Flask, request, jsonify
from models import db, User, Car
from services import UserService, CarService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trafikverket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

# User Endpoints
@app.route('/users', methods=['GET'])
def get_all_users():
    users = UserService.get_all_users()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = UserService.create_user(data)
    return jsonify(user.to_dict()), 201

# Car Endpoints
@app.route('/cars', methods=['GET'])
def get_all_cars():
    cars = CarService.get_all_cars()
    return jsonify([car.to_dict() for car in cars]), 200

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = CarService.get_car_by_id(car_id)
    if car:
        return jsonify(car.to_dict()), 200
    return jsonify({'error': 'Car not found'}), 404

@app.route('/cars', methods=['POST'])
def create_car():
    data = request.json
    car = CarService.create_car(data)
    return jsonify(car.to_dict()), 201

@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    data = request.json
    car = CarService.update_car(car_id, data)
    if car:
        return jsonify(car.to_dict()), 200
    return jsonify({'error': 'Car not found'}), 404

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    car = CarService.delete_car(car_id)
    if car:
        return '', 204
    return jsonify({'error': 'Car not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
