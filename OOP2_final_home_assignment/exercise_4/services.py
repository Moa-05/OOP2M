from models import db, User, Car

class UserService:
    @staticmethod
    def create_user(data):
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

class CarService:
    @staticmethod
    def create_car(data):
        car = Car(**data)
        db.session.add(car)
        db.session.commit()
        return car

    @staticmethod
    def get_all_cars():
        return Car.query.all()

    @staticmethod
    def get_car_by_id(car_id):
        return Car.query.get(car_id)

    @staticmethod
    def update_car(car_id, data):
        car = Car.query.get(car_id)
        if car:
            for key, value in data.items():
                setattr(car, key, value)
            db.session.commit()
        return car

    @staticmethod
    def delete_car(car_id):
        car = Car.query.get(car_id)
        if car:
            db.session.delete(car)
            db.session.commit()
        return car
