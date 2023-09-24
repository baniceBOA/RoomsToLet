from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.toast import toast
import requests
kv = '''
<RoomsToLet>:
	name:hotelname
	region:region
	roomtype:roomtype
	location:location
	picture:picture
	gps:gps
	amount:amount
	description:description
	ScrollView:
		pos_hint:{'top':0.9}
		Vertical:
			adaptive_height:True
			MDTextField:
				id:hotelname
				hint_text:'Hotel Name'
			MDTextField:
				id:region
				hint_text: 'Region'
			MDTextField:
				id:roomtype
				hint_text: 'Room Type'
			MDTextField:
				id:amount
				hint_text: 'Amount'
			MDTextField:
				id:location
				hint_text:'Location descripton'
			MDTextField:
				id:description
				hint_text:'Room descripton'
			MDSeparator:
				height:'8dp'
				color:[0,0,0.4, 0.6]
			MDFlatButton:
				id:picture
				text:'Pictures'
			MDFlatButton:
				id:gps
				text:'Grab location'
			MDFillRoundFlatButton:
				text:'submit'
				on_release:root.submit()			
'''
Builder.load_string(kv)
class RoomsToLet(MDFloatLayout):
	hotelname = ObjectProperty()
	region = ObjectProperty()
	roomtype = ObjectProperty()
	picture = ObjectProperty()
	gps = ObjectProperty()
	amount = ObjectProperty()
	location = ObjectProperty()
	description = ObjectProperty()

	def submit(self, *args):
		self.url = ''
		data = {
				'hotelname':self.hotelname.text,
				'region':self.region.text,
				'roomtype':self.roomtype.text,
				'picture':self.picture.source,
				'gps':self.gps.text,
				'amount':self.amount.text,
				'location':self.location.text,
				'descripton':self.description.text
		}
		resp = requests.post(self.url, data=self.data)
		if resp.status_code == 200:
			toast('Updated succefully')
		else:
			toast('An error occured')
