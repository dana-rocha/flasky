from flask import Blueprint, jsonify 
from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    driver = db.Column(db.String)
    team = db.Column(db.String)
    mass_kg = db.Column(db.Integer)





# line 15 "cars" doesn't need to match line 17 "/cars" if theres 'url_prefix="/cars"'
# Creating a new Blueprint object
# cars_bp = Blueprint("cars", __name__, url_prefix="/cars")

# Going to look at the /cars endpoint
# This decorator changes what this function does --> this decorator says get_all_cars() will be handling a route
# @cars_bp.route("", methods = ["GET"])
# def get_all_cars():
#     response = []

#     for car in cars:
#         response.append(
#             {
#                 "id" : car.id,
#                 "driver": car.driver,
#                 "team": car.team,
#                 "mass_kg": car.mass_kg
#             }
#         )

    # list of dictionaries --> JSON
    # Should return in JSON because our web browser doesn't know Python
    # return jsonify(response)

# Adding a new route to access one car
# @cars_bp.route("/<car_id>", methods=["GET"])
# def get_one_car(car_id):
#     try:
#         # Need to convert string to int
#         car_id = int(car_id)
#     except ValueError:
#         return jsonify({'msg': f"Invalid car id '{car_id}'. ID must be an integer."}), 400



    # chosen_car = None

    # for car in cars:
    #     if car.id == car_id:
    #         chosen_car = {
    #             "id" : car.id,
    #             "driver": car.driver,
    #             "team": car.team,
    #             "mass_kg": car.mass_kg
    #         }
    
    # if chosen_car is None:
    #     return jsonify({'msg': f'Could not find car with id {car_id}'}), 404
        
    # return jsonify(chosen_car), 200
