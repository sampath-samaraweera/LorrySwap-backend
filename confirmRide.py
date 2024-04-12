from app.models import SuggestedRide, Ride, UserType, User, Driver, Base
from database import Session
from flask import jsonify
import requests
import polyline

def suggested_ride(userId=None):

    print(userId)

    session = Session()

    # all_rides = session.query(SuggestedRide).all()

    all_rides = session.query(
        UserType.user_type, 
        User.fname, 
        User.photo,
        SuggestedRide.contact_recipient,
        SuggestedRide.date,
        SuggestedRide.package_type,
        SuggestedRide.weight,
        SuggestedRide.height,
        SuggestedRide.length,
        SuggestedRide.width,
        SuggestedRide.truck_type,
        SuggestedRide.location,
        SuggestedRide.destination,
        SuggestedRide.plat,
        SuggestedRide.plon,
        SuggestedRide.dlat,
        SuggestedRide.dlon,
        SuggestedRide.id,
        SuggestedRide.driver_id,
        SuggestedRide.driver_confirmation,
        SuggestedRide.cf_confirmation,
        SuggestedRide.finished,
        User.phone,
        User.lname,
        )\
        .join(User, UserType.user_id == User.id) \
        .join(SuggestedRide, SuggestedRide.user_id == User.id) \
        .all()
    
    session.commit()

    ride_list = []
    for ride in all_rides:
        ride_dict = {
            'id': ride[17],
            'contact_recipient' : ride[3],
            'date' : ride[4],
            'package_type' : ride[5],
            'weight' : ride[6],
            'height' : ride[7],
            'length' : ride[8],
            'width' : ride[9],
            'truck_type' : ride[10],
            'photo' : ride[2],
            'location' : ride[11],
            'destination' : ride[12],
            'plat' : ride[13],
            'plon' : ride[14],
            'dlat' : ride[15],
            'dlon':  ride[16],
            'actor' : ride[0],
            'fname' : ride[1],
            'lname' : ride[23],
            'phone' : ride[22],
            'driver_id' : ride[18],
            'driver_confirmation' : ride[19],
            'cf_confirmation' : ride[20],
            'finished' : ride[21],
        }
        # print(ride_dict)
        ride_list.append(ride_dict)
    return ride_list

def update_driver_confirmation(userId, body):
    
    print(body)
    print(userId)
    session = Session()

    try:
        for ride_data in body:
            ride_id = ride_data.get('id')
            confirmed_ride = session.query(SuggestedRide).filter(SuggestedRide.id == ride_id).first()
            
            # Check if the ride exists
            if confirmed_ride:
                # Update the driver confirmation and driver id
                confirmed_ride.driver_confirmation = True
                confirmed_ride.driver_id = userId
                session.commit()
            else:
                # Handle case where the ride does not exist
                print(f"Ride with id {ride_id} does not exist.")

    except Exception as e:
        session.rollback()
        return {'error': str(e)}, 500
    finally:
        session.close()

    