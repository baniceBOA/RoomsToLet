from kivy_garden.mapview import MapView
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty

from random import random

kv = '''
<Map>:
'''
Builder.load_string(kv)
class Map(MDFloatLayout):
	''' use the map of the kivy garden '''
	latitude = NumericProperty()
	longitude = NumericProperty() 
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.box = MDBoxLayout()
		self.box.pos_hint = {'top':0.93}
		ln = random()
		lg = random()
		self.map = MapView(zoom=9)
		self.box.add_widget(self.map)
		self.add_widget(self.box)
		if not self.latitude and self.longitude:
			self.longitude = lg
			self.latitude = ln
	def on_latitude(self, *args):
		''' updates the location of the marker on the map'''
		self.map = MapView(zoom=2)
		self.marker = MapMarker(lon=self.longitude, lat=self.latitude)
		self.map.add_marker(self.marker)
		self.map.center_on(self.latitude, self.longitude)#make the mark the center of the map

	def on_longitude(self, *args):
		''' updates the location of the marker on the map '''
		self.map = MapView(zoom=2)
		self.marker = MapMarker(lon=self.longitude, lat=self.latitude)
		self.map.add_marker(self.marker)
		self.map.center_on(self.latitude, self.longitude) #make the marker on the center of the map

