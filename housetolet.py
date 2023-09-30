from kivymd.uix.floatlayout  import MDFloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.toast import toast

from plyer import filechooser

import requests
kv = '''
<HouseToLet>:
	housetype:housetype
	name:name
	region:region
	location:location
	floorspace:floorspace
	gps:gps
	rooms:rooms
	rent:rent
	water:water
	picture:picture
	ScrollView:
		pos_hint:{'top':0.9}
		Vertical:
			adaptive_height:True
			MDTextField:
				id:name
				hint_text:'Residents Name'
			MDTextField:
				id:housetype
				hint_text:'House Type'
			MDTextField:
				id:region
				hint_text: 'Region'
			MDTextField:
				id:floorspace
				hint_text:'Floor space in meters squared'
			MDTextField:
				id:location
				hint_text:'Location descripton'
			MDTextField:
				id:rent
				hint_text:'House rent per month'
			MDTextField:
				id:rooms
				hint_text:'No of rooms'

			MDSeparator:

			MDLabel:
				text:'Amenities'
				pos_hint:{'center_x':0.5}

			Horizontal:
				size_hint_y:None
				height:dp(50)
				MDLabel:
					text:'water'
				MDSwitch:
					id:water
			
			MDFlatButton:
				id:picture 
				text:'Pictures'
				on_release:root.get_picture()

			MDFlatButton:
				id:gps
				text:'Grab location'
			
'''
Builder.load_string(kv)


class HouseToLet(MDFloatLayout):
	housetype= ObjectProperty()
	name = ObjectProperty()
	rooms = ObjectProperty()
	floorspace=ObjectProperty() # floorspace in meters squared.
	region = ObjectProperty()
	location_description = ObjectProperty()
	rent=ObjectProperty()
	water=ObjectProperty()
	gps = ObjectProperty()
	picture = ObjectProperty()

	def update_data(self):
		''' get the detials of the location under the current details '''
		self.url = ''
		#we are querying the data base
		data = {'housetype':self.housetype.text,
				'location_description':self.location_description.text,
				'floorspace':self.floorspace.text,
				'name':self.name.text,
				'rooms':self.rooms.text,
				'region':self.region.text,
				'location':self.location.text,
				'water':self.water.active,
				'rent':self.rent.text,
				'gps':self.gps.text}
		files = {'picture':open(self.picture.text, 'rb')}
		resp = requests.post(self.url, data=data, files=files)
		if resp.status_code == 200:
			toast(text='updated succefully')
		else:
			toast(text='An error occured')
	def get_picture(self, *args):
		''' Lock for image in the device filesystem '''
		filechooser.open_file(on_selection=self.selection)

	def selection(self, filename):
		self.picture.text = str(filename)

			
