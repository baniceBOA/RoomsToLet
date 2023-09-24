from tkinter import ON
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy_garden.mapview import MapView, MapMarker
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.toolbar import MDToolbar
from kivymd.utils.fitimage import FitImage
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.list import OneLineIconListItem
from kivy.clock import Clock
from kivy.lang import Builder
from random import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
Window.size = (360, 640)
kv = '''
#:import Window kivy.core.window.Window
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

<Map>:

<Vertical@MDBoxLayout>:
	orientation:'vertical'

<OneListItem>:
	
	IconLeftWidget:
		icon:root.icon
<Horizontal@MDBoxLayout>:
	spacing:'8sp'

<ClickableImage>: 

<CreateAccount>:
	MDLabel:
		text:' CreateAccount'
		pos_hint:{'center_y':0.85, 'center_x':0.5}

	ClickableImage:
		source:'D:/files/images/IMG-20220313-WA0011.jpg'
		radius:70,70,70,70
		size_hint_x:None
		width: Window.size[0]*0.25
		size_hint_y:None
		height:Window.size[0]*0.25
		pos_hint:{'top':0.85, 'center_x':0.5}
	ScrollView:
		pos_hint:{'top':0.70, 'center_x':0.5}
		Vertical:
			adaptive_height:True
			
			MDTextField:
				id:firstname
				radius: 50,50,50,50
				hint_text:'firstname'
				helper_text:'firstname'
				helper_text_mode:'on_error'
				size_hint_x:None
				width:dp(260)
				pos_hint:{'center_x':0.5}
			MDTextField:
				id:secondname
				radius: 50,50,50,50
				hint_text:'secondname'
				helper_text:'secondname'
				helper_text_mode:'on_error'
				size_hint_x:None
				width:dp(260)
				pos_hint:{'center_x':0.5}
			MDTextField:
				id:email
				required:True
				radius: 50,50,50,50
				hint_text:'E-mail'
				helper_text:'E-mail'
				helper_text_mode:'on_error'
				size_hint_x:None
				width:dp(260)
				pos_hint:{'center_x':0.5}
			MDTextField:
				id:username
				required:True
				radius: 50,50,50,50
				hint_text:'username'
				helper_text:'username'
				helper_text_mode:'on_error'
				size_hint_x:None
				width:dp(260)
				pos_hint:{'center_x':0.5}
				
			MDTextField:
				id:password
				hint_text:'password'
				required:True
				size_hint_x:None
				width:dp(260)
				pos_hint:{'center_x':0.5}
				helper_text_mode:'on_error'
				helper_text:'Weak password'
				on_text:root.check_password(password.text)
			MDTextField:
				id:repeat_password
				required:True
				hint_text:'password'
				size_hint_x:None
				width:dp(260)
				pos_hint:{'center_x':0.5}
				helper_text_mode:'persistent'
				helper_text:'repeat_password'

			MDFillRoundFlatButton:
				text:'Create'
				pos_hint:{'center_x':0.5}

<Login>:
	create_account:create_account
	password:password
	ClickableImage:
		source:'D:/files/images/IMG-20220313-WA0011.jpg'
		radius:70,70,70,70
		size_hint_x:None
		width: Window.size[0]*0.40
		size_hint_y:None
		height:Window.size[0]*0.40
		pos_hint:{'top':0.8, 'center_x':0.5}
		on_press:print('Clicked here')
	ScrollView:
		pos_hint:{'top':0.55, 'center_x':0.5}
		Vertical:
			adaptive_height:True
			
			MDTextField:
				id:username
				radius: 50,50,50,50
				hint_text:'username'
				helper_text:'username'
				helper_text_mode:'on_error'
				size_hint_x:None
				width:dp(260)
				pos_hint:{'center_x':0.5}
				
			MDTextField:
				id:password
				hint_text:'password'
				size_hint_x:None
				width:dp(260)
				pos_hint:{'center_x':0.5}
				helper_text_mode:'on_error'
				helper_text:'Weak password'
			MDFillRoundFlatButton:
				text:'login'
				pos_hint:{'center_x':0.5}
	
	MDLabel:
		text:"Don't have an Account"
		pos_hint:{'center_y':0.22, 'center_x':0.8}
	MDFillRoundFlatButton:
		id:create_account
		text:'Create Account'
		pos_hint:{'top':0.2, 'center_x':0.5}
		on_press:root.account_screen()
<ExtendedButton>:
	elevation:3
	-height:'56dp'
<HouseToLet>:
	Vertical:
		pos_hint:{'top':0.9}
		spacing:'2sp'
		MDTextField:
			id:name
			hint_text:'Residents Name'
		MDTextField:
			id:region
			hint_text: 'Region'
		MDTextField:
			id:location
			hint_text:'Location descripton'
		MDSeparator:
			height:'8dp'
			color:[0,0,0.4, 0.6]

		MDLabel:
			text:'Amenities'
			pos_hint:{'center_x':0.5}

		Horizontal:
			MDLabel:
				text:'water'
			MDSwitch:
				id:water
		Horizontal:
			MDLabel:
				text:'Electricty'
			MDSwitch:
				id:electricity
		Horizontal:
			MDLabel:
				text:'Gate'
			MDSwitch:
				id:gate
		MDFlatButton:
			id:picture 
			text:'Pictures'

		MDFlatButton:
			id:gps
			text:'Grab location'
		Widget:
<RoomsToLet>:
	Vertical:
		pos_hint:{'top':0.9}
		spacing:'2sp'
		MDTextField:
			id:name
			hint_text:'Hotel Name'
		MDTextField:
			id:region
			hint_text: 'Region'
		MDTextField:
			id:location
			hint_text:'Location descripton'
		MDSeparator:
			height:'8dp'
			color:[0,0,0.4, 0.6]

		Horizontal:
			MDLabel:
				text:'water'
			MDSwitch:
		Horizontal:
			MDLabel:
				text:'Electricty'
			MDSwitch:
		Horizontal:
			MDLabel:
				text:'Gate'
			MDSwitch:
		MDFlatButton:
			id:picture
			text:'Pictures'

		MDFlatButton:
			id:gps
			text:'Grab location'
		Widget:
<LandLord>:

<ViewRooms>:
	view:view
	size_hint_y:None
	height:dp(90)
	orientation:'vertical'
	MDCard:
		FitImage:
			id:thumbnail_image
			source:'D:/files/images/IMG-20220313-WA0011.jpg'
			size_hint_x:None
			width:dp(100)
			size_hint_y:None
			height:root.height-dp(12)
		MDLabel:
			id:residents_description
			text:'The descripton of the Residents'
		MDRectangleFlatButton:
			id:view
			text:'view'
			
	MDSeparator:
		height:'2dp'
		color:[0,0,0.4,0.6]

<ViewCatalogue>:
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
			



<ToLetApp>:
	pos_hint:{'top':0.9}
	Vertical:
		Horizontal:
			size_hint_y:None
			height:dp(50)
			MDTextField:
				hint_text:'Search'
				size_hint_x:None
				width:dp(260)

			MDFillRoundFlatButton:
				text:'Search'
				on_release: root.update_searches()
		MDScrollViewRefreshLayout:
			root_layout:root
			Vertical:
				adaptive_height:True

				id:view_rooms
					

<MainToLetApp>:
	screen_manager:screen_manager
	MDToolbar:
		id: toolbar
		pos_hint: {"top": 1}
		elevation: 10
		title: "TO Let"
		left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
	MDNavigationLayout:
		x:toolbar.height
		ScreenManager:
			id:screen_manager
			transition:FadeTransition(duration=0.0001, clearcolor=app.theme_cls.bg_dark)
			MDScreen:
				name:'ToLetApp'
				ToLetApp:
			MDScreen:
				name:'HouseToLet'
				HouseToLet:
			MDScreen:
				name:'RoomsToLet'
				RoomsToLet:
			MDScreen:
				name:'view_rooms'
				ViewCatalogue:
			MDScreen:
				name:'map'
				Map:
			MDScreen:
				name:'landlord'
				LandLord:
			MDScreen:
				name:'create_account'
				CreateAccount:
			MDScreen:
				name:'login'
				Login:
		MDNavigationDrawer:
			id:nav_drawer
			MDBoxLayout:
				orientation:'vertical'
				spacing:'2sp'
				FitImage:
					radius:45,45,0,0
					size_hint_x:None
					width:nav_drawer.width
					size_hint_y:None
					height:nav_drawer.height*0.25
					source:'D:/files/images/IMG-20220313-WA0011.jpg'
				ScrollView:
					Vertical:
						adaptive_height:True
						OneListItem:
							text:'Login'
							icon:'account'
							on_press:
								screen_manager.current = 'login'
								nav_drawer.set_state('close')
						OneListItem:
							icon:'home'
							text:'LandLord'
							on_press:
								screen_manager.current = 'landlord'
								nav_drawer.set_state('close')
						OneListItem:
							icon:'handshake'
							text:'Join '
						OneListItem:
							icon:'account-child'
							text:'Create Account'
							on_press:
								screen_manager.current = 'create_account'
								nav_drawer.set_state('close')
						OneListItem:
							icon:'file-document'
							text:'Terms Of Service'
	
	Horizontal:
		size_hint_y:None
		height:dp(67)
		pos_hint:{'top':0.12}
		MDRectangleFlatButton:
			id:to_let_app
			text:'ToLetApp'
			on_press:root.change_screen(to_let_app)
		MDRectangleFlatButton:
			id:house
			text:'HouseToLet'
			on_release:root.change_screen(house)
		MDRectangleFlatButton:
			id:rooms
			text:'RoomsToLet'
			on_release:root.change_screen(rooms)

'''
Builder.load_string(kv)
class OneListItem(OneLineIconListItem):
	icon = StringProperty()
class ClickableImage(ButtonBehavior, FitImage):
	pass
class ExtendedButton(RectangularElevationBehavior, MDFillRoundFlatButton):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.padding = '16dp'
		Clock.schedule_once(self.set_spacing)
	def set_spacing(self, interval):
		print(self.ids)
	def set_radius(self, *args):
		if self.rounded_button:
			self._radius = self.radius = self.height/4
class Login(MDFloatLayout):
	''' create a login of the application'''
	password =  ObjectProperty()
	create_account = ObjectProperty()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	def login(self):
		if self.password and self.username:
			#login the user
			pass
	def check_password(self, password):
		''' check the password if it is strong enough'''
		
		if len(password) < 8:
			#the password is weak or middle 
			self.password.error = True
			self.password.helper_text = 'weak password'
		elif len(password) == 8:
			self.password.helper_text = 'fair password'
			self.password.error = False
			self.password.helper_text_mode = 'persistent'
			self.password.helper_text_color_normal = [1, 1, 0, 1]
			
		elif len(password)>8:
			for c, p in zip(punctuation, password):
				if c == p:
					self.password.helper_text = 'strong password'
					self.password.helper_text_color_focus =  [0, 1, 0, 1]

	def account_screen(self, *args):
		screen = self.parent.parent
		screen.current = 'create_account'
					
		 
class CreateAccount(MDFloatLayout):
	pass
class HouseToLet(MDFloatLayout):
	name = ObjectProperty()
	region = ObjectProperty()
	location = ObjectProperty()
	water = ObjectProperty()
	electricity = ObjectProperty()
	gate = ObjectProperty()
	picture = ObjectProperty()
	gps = ObjectProperty()


class RoomsToLet(MDFloatLayout):
	name = ObjectProperty()
	region = ObjectProperty()
	location = ObjectProperty()
	water = ObjectProperty()
	electricity = ObjectProperty()
	gate = ObjectProperty()
	picture = ObjectProperty()
	gps = ObjectProperty()


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
	def go_to_map(self):
		screen = self.parent.parent
		screen.current = 'map'

class ViewRooms(MDBoxLayout):
	views = ObjectProperty()
	def change_screen(self):
		pass


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


class LandLord(MDFloatLayout):
	pass
class ToLetApp(MDBoxLayout):
	def update_searches(self):
		for i in range(10):
			room = ViewRooms()
			room.ids.view.bind(on_release=self.in_views)
			print(room.ids.view)
			self.ids.view_rooms.add_widget(room)
	def in_views(self, touch):
		screen = self.parent.parent
		screen.current = 'view_rooms'
		

class MainToLetApp(MDFloatLayout):
	screen_manager = ObjectProperty()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def change_screen(self, touch):
		self.screen_manager.current = touch.text
		print('changing screen to', touch.text)
class MainApp(MDApp):
	screen_manager = ObjectProperty()
	def build(self):
		return Map(longitude=0.02394, latitude=45.67867)
	def change_screen(self, touch):
		self.screen_manager.current = touch.text
		print('changing screen to', touch.text)


	 