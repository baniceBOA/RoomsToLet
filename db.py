from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///roomstolet.db', echo=True)
Base = declarative_base()
class Tenat(Base):
	'''the tenant database'''

	__tablename__ = 'tenant'
	id = Column(Integer, primary_key=True)
	names= Column(String, )
	phone_no =Column(Integer)
	address =  Column(String)
	location = Column(String)


class LandLord(Base):
	''' the landlord database '''
	__tablename__= 'landlord'
	id = Column(Integer, primary_key=True)
	names= Column(String)
	house = Column(String)
	phone_no =Column(Integer)
	address =  Column(String)
	location = Column(String)

	def serialize(self):
		data = dict(id=self.id, names=self.name, phone_no=self.phone_no, address=self.address, location=self.location)
		return data


class House(Base):
	'''the housetype'''
	__tablename__= 'housetype'
	id = Column(Integer, primary_key=True)
	housetype= Column(String)
	floorspace=Column(Integer)# floorspace in meters squared.
	name = Column(String)# residents Name
	rooms = Column(Integer)
	region = Column(String)
	location=Column(String)
	location_description = Column(String)
	gps=Column(String)
	rent=Column(Integer)
	water=Column(Boolean)
	pictures = Column(String)
	@property
	def serialize(self):
		data = dict(id=self.id, housetype=self.housetype, floorspace=self.floorspace, name=self.name, rooms=self.rooms, region=self.region, loaction=self.location, rent=self.rent, water=self.water, pictures=self.pictures )
		return data

class Room(Base):
	__tablename__ = 'room'
	id = Column(Integer, primary_key=True)
	hotelname = Column(String)
	region = Column(String)
	roomtype = Column(String)
	picture = Column(String)
	gps = Column(String)
	amount = Column(Integer)
	location = Column(String)
	description = Column(String)

	@property
	def serialize(self):
		data = {'id': self.id, 'hotelname':self.hotelname, 'region':self.region, 'roomtype':self.roomtype, 'picture':self.picture, 'gps':self.gps, 'amount':self.amount, 'location':self.location, 'description':self.description}
		return data

class Account(Base):
	__tablename__ = 'account'
	id = Column(Integer, primary_key=True)
	firstname = Column(String)
	secondname = Column(String)
	email = Column(String)
	username = Column(String)
	password = Column(String)
	avatar = Column(String)

	@property
	def serialize(self):
		data = dict(id=self.id, firstname=self.firstname, secondname=self.secondname, email=self.email, username=self.username, avatar=self.avatar)
		return data

Base.metadata.create_all(engine)

#session = sessionmaker()(bind=engine)

