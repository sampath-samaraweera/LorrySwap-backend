from app.models import Ride
from database import Session 
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
            'user_id': ride.user_id
        }
        rides_list.append(ride_dict)

    # Return the list of dictionaries
    return rides_list
