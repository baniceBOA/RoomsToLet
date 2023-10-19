# controller:
from models.db import Account, Room, House, LandLord, engine
from sqlalchemy.orm import sessionmaker
import json

session = sessionmaker()(bind=engine) #create a custom session for updating the database
# this is to ensure reliability of the database even with multiple connections


class Controller:
    name = 'Controller'
    
    
    def create_json_dict(self, result):
        ''' 
        convert the result into  a dictionary then to the to a json which will be return to the request
            :args: result
                result is a list a list of list
            returns a list 
        '''
        mappings = {}
        data = []
        for res in result:
            if res:
                #confirm the the list actualy has values before processing it
                for value in res:
                    # the value here is taken to be a ~db.Room  
                    dic = value.serialize
                    if dic['id'] in mappings:
                        pass
                    else:
                        mappings[dic['id']] = dic
        for key, value in mappings.items():
            data.append(value)

        return data
class RoomController(Controller):
    ''' create a brigde between between the view and the models'''
    name = 'Room'
    def __init__(self):
        self.room = None
    @staticmethod
    def add_items(self, hotelname='',
                  region='',
                  roomtype='',
                  location='',
                  gps='',
                  amount=0,
                  description=''):
        ''' populate the fields of the room database'''
        self.room = Room(hotelname=hotelname,region=region, roomtype=roomtype,location=location,gps=gps, amount=amount, description=description,)
        self.commit(self.room)
    def commit(self, room_instance):
        session.add(room_instance)
        session.commit()
    def query(self, value):
        ''' :'Query the database for multiple value in different fields
        returns an json with the values found in the database
        '''
        hotelname = session.query(Room).filter(Room.hotelname.like(f'%{value}%')).all()
        region = session.query(Room).filter(Room.region.like(f'%{value}%')).all()
        roomtype = session.query(Room).filter(Room.roomtype.like(f'%{value}%')).all()
        location = session.query(Room).filter(Room.location.like(f'%{value}%')).all()
        description = session.query(Room).filter(Room.description.like(f'%{value}%')).all()
        values =[hotelname, region, roomtype, location, description]
        return self.create_json_dict(values)
    


class AccountController(Controller):
    name = 'Account'
    def __init__(self):
        self.account = None
    def query(self, value):
        ''' Search the username of with that value'''
        username = session.query(Account).filter(Account.username.like(f'%{value}%')).all()
        
        return self.create_json_dict([username])
        
class HouseController(Controller):
    name = 'House'
    
    def query(self, value):
        ''' search the hotel name '''
        name = session.query(House).filter(House.name.like(f'%{value}%')).all()
        location = session.query(House).filter(House.location.like(f'%{value}%')).all()
        result = [location, name]
        return self.create_json_dict(result)
        
class LandlordController(Controller):
    name = 'LandLord'
    def query(self, value):
        name = session.query(LandLord).filter(LandLord.names.like(f'%{value}%')).all()
        return self.create_json_dict([name])


        
        

