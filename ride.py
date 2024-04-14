from app.models import Ride
from database import Session
from sqlalchemy import and_
# from sqlalchemy import select

def create_ride(body):
    print(body)

    session = Session()
    
    location = body.get('location')
    destination = body.get('destination')
    location_lat = body.get('location_lat')
    location_lon = body.get('location_lon')
    destination_lat = body.get('destination_lat')
    destination_lon = body.get('destination_lon')
    date = body.get('date')
    time = body.get('time')
    user_id = body.get('user_id')
    finished_ride = body.get('finished_ride')

    try:
        new_ride = Ride(
            location = location,
            destination = destination,
            location_lat=location_lat,
            location_lon=location_lon,
            destination_lat=destination_lat, 
            destination_lon=destination_lon,
            date=date, 
            time=time,
            user_id=user_id,
            finished_ride=finished_ride
        )
        session.add(new_ride)
        session.flush()

        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Error creating newride: {e}")
        return False
    finally:
        session.close()

def get_all_rides():
    session = Session()

    # Use SQLAlchemy select to query all Rides objects
    all_rides = session.query(Ride).all()

    # Close the session
    session.close()

    # Convert each Ride object to a dictionary
    rides_list = []
    for ride in all_rides:
        ride_dict = {
            'id': ride.id,
            'location_lat': ride.location_lat,
            'location_lon': ride.location_lon,
            'destination_lat': ride.destination_lat,
            'destination_lon': ride.destination_lon,
            'date': ride.date,
            'time': ride.time,
            'user_id': ride.user_id,
            'finished_ride' : ride.finished_ride
        }
        rides_list.append(ride_dict)

    # Return the list of dictionaries
    return rides_list

def get_current_ride(userId):
    session = Session()

    # Query the database to find the ride with the given user ID
    driver_ride = session.query(Ride).filter(and_(Ride.user_id == userId, Ride.finished_ride == 0)).order_by(Ride.id.desc()).first()

    # Close the session
    session.close()

    # If no ride is found, return None
    ride_dict_none = {}
    if not driver_ride:
        return ride_dict_none

    # Convert the ride object to a dictionary
    ride_dict = {
        'id': driver_ride.id,
        'location_lat': driver_ride.location_lat,
        'location_lon': driver_ride.location_lon,
        'destination_lat': driver_ride.destination_lat,
        'destination_lon': driver_ride.destination_lon,
        'date': driver_ride.date,
        'time': driver_ride.time,
        'user_id': driver_ride.user_id,
        'location': driver_ride.location,
        'destination': driver_ride.destination
    }

    # Return the dictionary representing the ride
    return ride_dict


def delete_ride(userId):
    session = Session()

    # Query the database to find the ride with the given ID
    ride = session.query(Ride).filter(Ride.user_id == userId).order_by(Ride.id.desc()).first()

    # If the ride exists, delete it from the database
    if ride:
        session.delete(ride)
        session.commit()
        session.close()
        return True, 200
    else:
        session.close()
        return False, 404