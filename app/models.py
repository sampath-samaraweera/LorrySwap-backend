from sqlalchemy import String, Column, ForeignKey, DATE, Integer, DateTime, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    # table name should be here
    __tablename__ = 'user'

    # all the columns and their properties should be here 
    id = Column(Integer, primary_key=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False ,unique=True)
    phone = Column(String(12), nullable=False ,unique=True)
    age = Column(Integer, nullable=False)
    gender = Column(String(1), nullable=False)
    photo = Column(String(255), nullable=False, server_default='../assests/images/default.jpg')
    nic = Column(String(15), nullable=False ,unique=True)
    # created_at = Column(DateTime, server_default=func.now())
    username = Column(String(50), nullable=False, unique=True)
    password_hash = Column(String(256), nullable=False)
    verified = Column(Boolean, default=False)

class Driver(Base):
    __tablename__ = 'driver'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    residence = Column(String(50), nullable=False)
    licence_side1 = Column(String(500), nullable=True, unique=True)
    licence_side2 = Column(String(500), nullable=True, unique=True)

class UserType(Base):
    __tablename__ = 'user_type'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_type = Column(String(50), nullable=False)

class Ride(Base):
    __tablename__ = "ride"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    location = Column(String(300), nullable=False)
    destination = Column(String(300), nullable=False)
    location_lat = Column(String(50), nullable=False)
    location_lon = Column(String(50), nullable=False)
    destination_lat = Column(String(50), nullable=False)
    destination_lon = Column(String(150), nullable=False)
    date = Column(DATE, nullable=False)
    time = Column(String(150), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    finished_ride = Column(Boolean, nullable=False, server_default='false')

class SuggestedRide(Base):
    __tablename__ = "suggestedRide"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    contact_recipient = Column(String(15), nullable=False)
    date = Column(DATE, nullable=False)
    package_type = Column(String(50), nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    length = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    truck_type = Column(String(50), nullable=False)
    location = Column(String(20), nullable=False, server_default='Colombo')
    destination = Column(String(20), nullable=False, server_default='Ratnapura')
    plat = Column(String(50), nullable=False)
    plon = Column(String(50), nullable=False)
    dlat = Column(String(50), nullable=False)
    dlon = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    driver_id = Column(Integer, ForeignKey('user.id'), nullable=True, server_default=None)
    driver_confirmation = Column(Boolean, nullable=False, server_default='false')
    cf_confirmation = Column(Boolean, nullable=False, server_default='false')
    finished = Column(Boolean, nullable=False, server_default='false')
    driver_rejection = Column(Boolean, nullable=False, server_default='false')
    cf_rejection = Column(Boolean, nullable=False, server_default='false')



    def __str__(self):
        return (
            f"SuggestedRide("
            f"id={self.id}, "
            f"contact_recipient={self.contact_recipient}, "
            f"date={self.date}, "
            f"package_type={self.package_type}, "
            f"weight={self.weight}, "
            f"height={self.height}, "
            f"length={self.length}, "
            f"width={self.width}, "
            f"truck_type={self.truck_type}, "
            f"location={self.location}, "
            f"destination={self.destination}, "
            f"plat={self.plat}, "
            f"plon={self.plon}, "
            f"dlat={self.dlat}, "
            f"dlon={self.dlon}, "
            f"user_id={self.user_id}, "
            f"driver_id={self.driver_id}, "
            f"driver_confirmation={self.driver_confirmation}, "
            f"cf_confirmation={self.cf_confirmation}, "
            f"finished={self.finished}"
            f")"
        )


