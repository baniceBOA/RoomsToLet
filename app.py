
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy_garden.mapview import MapView, MapMarker
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.utils.fitimage import FitImage
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.tab import MDTabsBase
from kivy.clock import Clock, mainthread
from kivy.lang import Builder
from random import random 
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from kivy.network.urlrequest import UrlRequest
import os
import requests
from io import BytesIO
from threading import Thread
from time import time
from PIL import Image as PilImage
from loaders import AKImageLoader
Window.size = (360, 640)
kv = '''
#:import Window kivy.core.window.Window
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import CreateAccount create_account.CreateAccount
#:import RoomsToLet roomstolet.RoomsToLet
#:import HouseToLet housetolet.HouseToLet
#:import Login login.Login
#:import ViewCatalogue view_catalogue.ViewCatalogue
#:import AccountManager account_manager.AccountManager
#:import Map map.Map
#:import CustomViewRefreshLayout customrefreshview.CustomViewRefreshLayout
#:import MDRecycleBoxLayout customrefreshview.MDRecycleBoxLayout


<Vertical@MDBoxLayout>:
	orientation:'vertical'

<OneListItem>:
	
	IconLeftWidget:
		icon:root.icon
<Horizontal@MDBoxLayout>:
	spacing:'8sp'

<ClickableImage>: 

<Avatar@ClickableImage>:
	radius:45,45,45,45

<ExtendedButton>:
	elevation:3
	-height:'56dp'
<Tab>:
	
	Vertical:
		MDIconButton:
			id:icon
			icon:root.icon
		MDLabel:
			id:text
			text:root.text


<LandLord>:
	HouseToLet:
<ViewHouseImage>:

<ViewHouse>:
	orientation:'vertical'
	size_hint_y:None
	height:dp(300)
	padding:dp(10)
	pos_hint:{'center_x':0.5}
	md_bg_color:app.theme_cls.bg_darkest
	ViewHouseImage:
		source:root.image
		size_hint_x:None
		width:dp(340)
		size_hint_y:None
		height:dp(250)
	MDBoxLayout:
	    orientation:'vertical'
		size_hint_y:None
		height:dp(50)
		md_bg_color:app.theme_cls.bg_light
		size_hint_x:None
		width:dp(340)
		MDLabel:
		    font_size:dp(18)
			text:root.housetype
		MDLabel:
		    font_size:dp(12)
			text:root.rent
		MDLabel:
		    font_size:dp(12)
			text:root.region
		MDLabel:
		    font_size:dp(12)
			text:root.location_description

<ViewRooms>:
	view:view
	size_hint_y:None
	height:dp(90)
	orientation:'vertical'
	MDCard:
	    size_hint_y:None
		height:root.height-dp(15)
		FitImage:
			id:thumbnail_image
			source:root.source
			size_hint_x:None
			width:dp(100)
			size_hint_y:None
			height:root.height-dp(20)
		MDLabel:
			id:residents_description
			text:'The descripton of the Residents'
		MDRectangleFlatButton:
			id:view
			text:'view'
			on_release:root.in_views(view)
			
	MDSeparator:
		height:'2dp'
		color:[0,0,0.4,0.6]


			 
<ToLetApp>:
	pos_hint:{'top':0.9}
	size_hint_y:None
	height:Window.size[1]*0.9
	md_bg_color:app.theme_cls.bg_darkest
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
		CustomViewRefreshLayout:
			id:refresh_layout
			root_layout:root
			refresh_callback:app.refresh
			viewclass:'ViewHouse'
			MDRecycleBoxLayout:
			    orientation:'vertical'
			    default_size: None, dp(325)
                default_size_hint: 1, None
			    adaptive_height:True
			    
					

<MainToLetApp>:
	screen_manager:screen_manager
	MDTopAppBar:
		id: toolbar
		pos_hint: {"top": 1}
		elevation: 10
		title: "SpaceToLet"
		left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
	
	MDBottomNavigation:
		pos_hint:{'top':0.12}
		MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Python'
            icon: 'language-python'

            MDLabel:
                text: 'Python'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'C++'
            icon: 'language-cpp'

            MDLabel:
                text: 'I programming of C++'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'JS'
            icon: 'language-javascript'

            MDLabel:
                text: 'JS'
                halign: 'center'
    
	Avatar:
		source:'D:/files/images/IMG-20220313-WA0011.jpg'
		pos_hint:{'top':0.97, 'center_x':0.9}
		size_hint_x:None
		width:Window.size[0]*0.100
		size_hint_y:None
		height:Window.size[0]*0.100
		on_press:
			screen_manager.current = 'account_manager'
	
	MDNavigationLayout:
		x:toolbar.height
		ScreenManager:
			id:screen_manager
			transition:FadeTransition(duration=0.00001, clearcolor=app.theme_cls.bg_dark)
			MDScreen:
				name:'ToLetApp'
				ToLetApp:
					id:my_views
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
				id:map
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
			MDScreen: 
				name:'account_manager'
				AccountManager:

		MDNavigationDrawer:
			id:nav_drawer
			MDBoxLayout:
				orientation:'vertical'
				spacing:'2sp'
				MDRelativeLayout:
				    adaptive_height:True
				    FitImage:
					    radius:45,45,0,0
					    size_hint_x:None
					    width:nav_drawer.width-dp(15)
					    size_hint_y:None
					    height:nav_drawer.height*0.25
					    source:'D:/files/images/IMG-20220313-WA0011.jpg'
				    MDLabel:
			            text:app.title
					    font_size:dp(20)


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


class Tab(MDBoxLayout, MDTabsBase):
	icon = StringProperty()
	text = StringProperty()


class ViewHouseImage(ButtonBehavior, AKImageLoader):
	pass
		
class ViewHouse(RectangularElevationBehavior, MDBoxLayout):
	image = StringProperty()
	housetype = StringProperty()
	region = StringProperty()
	rent = StringProperty()
	location_description = StringProperty()
class ViewRooms(MDBoxLayout):
	views = ObjectProperty()
	source = StringProperty()

	def in_views(self, touch):
		print('changing screen', self.parent.parent.parent.parent.parent.parent)
		screen = self.parent.parent.parent.parent.parent.parent
		screen.current = 'view_rooms'

	
	

class LandLord(MDFloatLayout):
	pass


class ToLetApp(MDFloatLayout):
	def update_searches(self):
		if self.ids.refresh_layout.data:
			self.ids.refresh_layout.data = []
			self.ids.refresh_layout.viewclass = 'ViewRooms'
		self.ids.refresh_layout.data = [{'source':r'D:/files/images/IMG-20220313-WA0011.jpg'} for i in range(100)]


	
		

class MainToLetApp(MDFloatLayout):
	screen_manager = ObjectProperty()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def change_screen(self, touch):
		self.screen_manager.current = touch.text
		
class MainApp(MDApp):
	screen_manager = ObjectProperty()
	def build(self):
		self.images_list = []
		self.title = 'ToLetApp'
		self.theme_cls.primary_palette = 'Teal'
		return MainToLetApp()
	def on_start(self):
		self.images = [img for img in os.listdir('D:/files/images/') if img.endswith('.jpg')]
		self.toletapp = self.root.ids.my_views.ids.refresh_layout
		data = [{'image':f'D:/files/images/{img}', 'housetype':'bugalow'} for img in self.images]
		self.toletapp.data = data
		
	def refresh(self):
		Clock.schedule_once(self.refresh_callback, 1)

	def refresh_callback(self, interval):
		print('refreshing')
		'''
		import random
		img = random.choice(self.images)
		print(self.root.ids.my_views.ids.refresh_layout.viewclass)
		self.root.ids.my_views.ids.refresh_layout.data = []
		self.root.ids.my_views.ids.refresh_layout.viewclass = 'ViewHouse'
		self.root.ids.my_views.ids.refresh_layout.data = [{'image':f"D:/files/images/{img}", 'housetype':'bugalow'} for i in range(30)]
		
        '''
		
		
		#r = requests.get('http://127.0.0.1:5000/get_images')
		#result = r.json()
		url = 'http://127.0.0.1:5000/get_images'
		self.images_list = []
		UrlRequest(url, self.success_fetch)
		#self.root.ids.my_views.ids.refresh_layout.data = []
		self.root.ids.my_views.ids.refresh_layout.viewclass = 'ViewHouse'
		#self.root.ids.my_views.ids.refresh_layout.data = [{'image':i, 'housetype':'bugalow'} for i in self.images_list]
		
	@mainthread	
	def success_fetch(self, req, result):
	
		print(result.keys())
		
		for img in result['images']:
			self.images_list.append(f'http://localhost:5000/get_file/{img}')
			
		self.root.ids.my_views.ids.refresh_layout.data = []
		self.root.ids.my_views.ids.refresh_layout.viewclass = 'ViewHouse'
		self.root.ids.my_views.ids.refresh_layout.data = [{'image':i, 'housetype':'bugalow'} for i in self.images_list]
		self.root.ids.my_views.ids.refresh_layout.refresh_done()
    
	def on_stop(self):
		''' perform some cleaning before the application close and return back the resource consumed'''
		for file in self.images_list:
			os.remove(file)

	def generate_image(self, file):
		filename = f'image-{int(time())}.png'
		r = requests.get(f'http://localhost:5000/get_file/{file}')
		pic = PilImage.open(BytesIO(r.content))
		pic.save(filename)
		print(f'=====================================generated==={filename}===succefully')
		return filename
	
MainApp().run()	 