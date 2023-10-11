from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty


kv = '''
<ViewCatalogue>:
	pos_hint:{'top':0.9}
	size_hint_y:None
	height:Window.size[1]*0.9
	
	carousel:carousel
	residents_name:residents_name
	area:area
	location_description:location_description
	map_location:map_location
	water:water
	electricity:electricity
	gate:gate
	roads:roads
	security:security
	Vertical:
		padding:[dp(10), 0, dp(10), 0]
		MDCarousel:
			id:carousel
			size_hint_y:None
			height:dp(200)
			FitImage:
				source:'D:/files/images/IMG-20220313-WA0011.jpg'
				size_hint_y:None
				height:dp(200)
				radius:[45,45, 0, 0]
			FitImage:
				source:'D:/files/images/IMG-20220313-WA0011.jpg'
				size_hint_y:None
				height:dp(200)
				radius:[45,45, 0, 0]
			FitImage:
				source:'D:/files/images/IMG-20220313-WA0011.jpg'
				size_hint_y:None
				height:dp(200)
				radius:[45,45, 0, 0]
		MDSeparator:
		MDScrollViewRefreshLayout:
			root_layout:root
			Vertical:
				padding:[dp(10), 0, dp(10), 0]
				adaptive_height:True
				
				MDLabel:
					id: residents_name
					text:'Residents Name'
					size_hint_y:None
					height:dp(67)
				MDSeparator:
				MDLabel:
					id:area
					text:'size in square metres'
					size_hint_y:None
					height:dp(67)
				MDSeparator:
				Horizontal:
					size_hint_y:None
					height:dp(67)
					MDLabel:
						id:location_description
						text:'location descripton'
						size_hint_x:None
						width:dp(240)
					MDFillRoundFlatButton:
						id:map_location
						text:'Map location'
						on_release:root.go_to_map()
				MDSeparator:
				Horizontal:
					size_hint_y:None
					height:dp(67)
					MDLabel:
						text:'water'
					MDCheckbox:
						id:water
				MDSeparator:
				Horizontal:
					size_hint_y:None
					height:dp(67)
					MDLabel:
						id:electricity
						text:'Electricty'
					MDCheckbox:
				MDSeparator:
				Horizontal:
					size_hint_y:None
					height:dp(67)
					MDLabel:
						id: gate
						text:'Gate'
					MDCheckbox:
				MDSeparator:
				Horizontal:
					size_hint_y:None
					height:dp(67)
					MDLabel:
						id:roads
						text:'Roads'
					MDCheckbox:
				MDSeparator:
				Horizontal:
					size_hint_y:None
					height:dp(67)
					MDLabel:
						id:security
						text:'Security'
					MDCheckbox:
'''
Builder.load_string(kv)
class ViewCatalogue(MDFloatLayout):
	carousel = ObjectProperty()
	residents_name = ObjectProperty()
	area = ObjectProperty()
	location_description = ObjectProperty()
	map_location = ObjectProperty()
	water = ObjectProperty()
	electricity = ObjectProperty()
	gate = ObjectProperty()
	roads = ObjectProperty()
	security = ObjectProperty()
	def load_data(self):
		''' Loads the data into the appropriate fields '''

		return NotImplemented
	def connection(self):
		''' Looks for a connection of the network '''
		return 


	def test_connection(self):
		''' test if we have a live connection 
		The method is called before the connection method to a certain a connectiong
		the Method returns a booleans of the method'''
		return NotImplemented


	def go_to_map(self):
		screen = self.parent.parent
		screen.current = 'map'