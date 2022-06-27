from flask import Blueprint, jsonify, request, make_response, abort

from app import db
from app.models.cars import Car

cars_bp = Blueprint("cars", __name__, url_prefix="/cars")

@cars_bp.route("", methods=["POST"])
def create_car():
    request_body = request.get_json()

    new_car = Car(
        driver=request_body["driver"],
        team=request_body["team"],
        mass_kg=request_body["mass_kg"]
    )

    db.session.add(new_car)
    db.session.commit()

    return {
        "id": new_car.id
    }, 201

@cars_bp.route("", methods = ["GET"])
def get_all_cars():

    # Can get all the arguments like this
    params = request.args

    # Now we can loop through al the params

    if "driver" in cars:
        driver_name = params["driver"]
        cars = Car.query.filter_by(driver=driver_name)
    elif "team" in cars:
        drivers_team = params["team"]
        cars = Car.query.filter_by(team=drivers_team)
    else:
        cars = Car.query.all()

    # Can use this on all of them, no matter the input
    cars = Car.query.all()

    response = []

    for car in cars:
        response.append(
            {
                "id" : car.id,
                "driver": car.driver,
                "team": car.team,
                "mass_kg": car.mass_kg
            }
        )





def get_one_car_or_abort(car_id):
    try:
        car_id = int(car_id)
    except ValueError:
        rsp = {'msg': f"Invalid car id: '{car_id}'. ID must be an integer"}
        abort(make_response(jsonify(rsp), 400))
    
    chosen_car = Car.query.get(car_id)

    if chosen_car is None:
        return jsonify({'msg': f'Could not find car with id {car_id}'}), 404 









@cars_bp.route("/<car_id>", methods=["GET"])
def get_one_car(car_id):
    try:
        car_id = int(car_id)
    except ValueError:
        return jsonify({'msg': f"Invalid car id: '{car_id}'. ID must be an integer"}), 400

    chosen_car = Car.query.get(car_id)

    if chosen_car is None:
        return jsonify({'msg': f'Could not find car with id {car_id}'}), 404 
            
    return jsonify({
        "id": chosen_car.id,
        "driver": chosen_car.driver,
        "team": chosen_car.team,
        "mass_kg": chosen_car.mass_kg
    })
    
@cars_bp.route("/<car_id>", methods=["PUT"])
def replace_one_car(car_id):
    try:
        car_id = int(car_id)
    except ValueError:
        return jsonify({'msg': f"Invalid car id: '{car_id}'. ID must be an integer"}), 400

    request_body = request.get_json()

    if "driver" not in request_body or \
        "team" not in request_body or \
        "mass_kg" not in request_body:
        return jsonify({'msg': f"Request must include driver, team, and mass_kg"}), 400

    chosen_car = Car.query.get(car_id)

    if chosen_car is None:
        return jsonify({'msg': f'Could not find car with id {car_id}'}), 404

    chosen_car.driver = request_body["driver"]
    chosen_car.team = request_body["team"]
    chosen_car.mass_kg = request_body["mass_kg"]

    db.session.commit()

    return make_response(
        jsonify({'msg': f"Successfully replaced car with id {car_id}"}),
        200
    )


@cars_bp.route("/<car_id>", methods=["DELETE"])
def delete_one_car(car_id):
    try:
        car_id = int(car_id)
    except ValueError:
        return jsonify({'msg': f"Invalid car id: '{car_id}'. ID must be an integer"}), 400

    chosen_car = Car.query.get(car_id)

    if chosen_car is None:
        return jsonify({'msg': f'Could not find car with id {car_id}'}), 404

    db.session.delete(chosen_car)
    db.session.commit()

    return jsonify({'msg': f'Deleted car with id {car_id}'})


@cars_bp.route("/<car_id>", methods=["PUT"])
def replace_one_car(car_id):
    # Validate that car_id is an integer
    try:
        # Need to convert id to int
        car_id = int(car_id)
    except: 
        return (jsonify({"message": f"Invalid car id: {car_id}. ID must be an integer"}, 400))
    
    request_body = request.get_json()

    # Don't need to include id in the request body because we already have the id in the request

    if "driver" not in request_body or \
        "team" not in request_body or \
        "mass_kg" not in request_body:
        return jsonify({"message": f"Request must include driver, team, and mass_kg"}, 400)
    
    chosen_car = Car.query.get(car_id)

    if chosen_car is None:
        return jsonify({'msg': f'Could not find car with id {car_id}'}), 404

    chosen_car.driver = request_body["driver"]
    chosen_car.team = request_body["team"]
    chosen_car.mass_kg = request_body["mass_kg"]

    db.session.commit()

    return jsonify({"message": f"Successfully replaced car with id {car_id}"})




@cars_bp.route("/<car_id>", methods=["DELETE"])
def delete_one_car(car_id):
    # Validate that car_id is an integer
    try:
        # Need to convert id to int
        car_id = int(car_id)
    except: 
        return (jsonify({"message": f"Invalid car id: {car_id}. ID must be an integer"}, 400))

    chosen_car = Car.query.get(car_id)

    if chosen_car is None:
        return jsonify({'msg': f'Could not find car with id {car_id}'}), 404

    db.session.delete(chosen_car)
    db.session.commit()
