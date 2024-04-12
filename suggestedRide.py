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

    # print(all_rides)

    driver_ride = session.query(Ride).filter(Ride.user_id == userId).order_by(Ride.id.desc()).first()

    # print(driver_ride)

    new_ride_list = matchRide(driver_ride, all_rides)

    # ride = driver_ride
    # for ride in driver_ride:
    #     print(ride.id, ride.location_lat,ride.location_lon)

    session.commit()

    ride_list = []
    for ride in new_ride_list:
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

def matchRide(driver_ride, all_rides):

    originLat = driver_ride.location_lat
    originLng = driver_ride.location_lon
    destinationLat = driver_ride.destination_lat
    destinationLng = driver_ride.destination_lon
    apiKey = 'AIzaSyDJ_gMdx_NFqDxKkGpST8t5EWCfbKNSijw'

    ride_list_pickup = []
    new_ride_list = []

    try:
        response = requests.get(
            f'https://maps.googleapis.com/maps/api/directions/json?origin={originLat},{originLng}&destination={destinationLat},{destinationLng}&key={apiKey}'
        )
        data = response.json()
        encoded_polyline = data['routes'][0]['overview_polyline']['points']
        decoded_coordinates = polyline.decode(encoded_polyline)

        # print(decoded_coordinates)
        # print(f"{round(decoded_coordinates[20][0],1)}")
        # print(f"{round(float(all_rides[7][13]),1)}")
        # print(f"{round(float(all_rides[7][14]),1)}")

        # print(round(6.71907,2))

        for ride in all_rides:
            # print(ride)
            # print()
            for coordinate in decoded_coordinates:

                current_coordLat = f"{round(coordinate[0], 1)}"
                current_coordLng = f"{round(coordinate[1], 1)}"
                current_ride_PLat = f"{round(float(ride[13]), 1)}"
                current_ride_PLng = f"{round(float(ride[14]), 1)}"

                if (current_ride_PLat == current_coordLat and current_ride_PLng == current_coordLng and ride[19] == False):
                    ride_list_pickup.append(ride)
                    break;

        for ride in ride_list_pickup:
            # print(ride)
            # print()
            for coordinate in decoded_coordinates:

                current_coordLat = f"{round(coordinate[0], 1)}"
                current_coordLng = f"{round(coordinate[1], 1)}"
                current_ride_DLat = f"{round(float(ride[15]), 1)}"
                current_ride_DLng = f"{round(float(ride[16]), 1)}"

                if (current_ride_DLat == current_coordLat and current_ride_DLng == current_coordLng):
                    new_ride_list.append(ride)
                    break;


        return new_ride_list
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

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

    