
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
from kivymd.uix.fitimage import FitImage
from kivymd.uix.imagelist import MDSmartTile
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.list import OneLineIconListItem
from kivymd.toast import toast
from kivymd.uix.tab import MDTabsBase
from kivy.clock import Clock, mainthread
from kivy.lang import Builder
from random import random 
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from kivy.network.urlrequest import UrlRequest
from kivy.utils import platform
import os
import requests
from io import BytesIO
from threading import Thread
from time import time
from PIL import Image as PilImage
from loaders import AKImageLoader
from plyer import storagepath
from PIL import ImageGrab
if platform != 'android':
	Window.size = (400, 800)

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
#:import ConnectionSetting connections.ConnectionSetting
#:import CustomViewRefreshLayout customrefreshview.CustomViewRefreshLayout
#:import MDRecycleBoxLayout customrefreshview.MDRecycleBoxLayout
#:import MDRecycleGridLayout customrefreshview.MDRecycleGridLayout
#:import SearchView searchview.SearchView


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
	radius: 24
	box_radius: [0, 0, 24, 24]
	lines: 2
	source: root.image
	pos_hint: {"center_x": .5, "center_y": .5}
	size_hint: None, None
	size: "320dp", "320dp"
	MDIconButton:
		icon: "heart-outline"
		theme_icon_color: "Custom"
		icon_color: 1, 0, 0, 1
		pos_hint: {"center_y": .5}
		on_release: self.icon = "heart" if self.icon == "heart-outline" else "heart-outline"
	TwoLineListItem:
		text: f"[color=#ffffff][b]{root.housetype}[/b][/color]"
		secondary_text: f"[color=#808080][b]{root.region}[/b][/color]"
		pos_hint: {"center_y": .5}

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
	
	md_bg_color:app.theme_cls.bg_darkest
	Vertical:
		Horizontal:
			size_hint_y:None
			height:dp(50)
			MDRelativeLayout:
				MDTextField:
					id:search_input
					mode:'round'
					hint_text:'search'
					size_hint_x:None
					width:Window.size[0]*0.7
					pos_hint:{'center_x':0.5, 'center_y':0.5}
				MDIconButton:
					icon:''
					id:toletapp_return_btn
					pos_hint:{'center_x':0.08, 'center_y':0.5}
					on_release:root.return_home_screen()
				MDIconButton:
					icon:'magnify'
					pos_hint:{'center_x':0.9, 'center_y':0.5}
					on_release:root.update_searches()
		MDScreenManager:
			id:toletapp_sm
			MDScreen:
				name:'toletapp_screen_home'
				CustomViewRefreshLayout:
					id:refresh_layout
					root_layout:root
					refresh_callback:app.refresh
					viewclass:'ViewHouse'
					MDRecycleGridLayout:
						default_size: None, dp(325)
						default_size_hint: 1, None
						adaptive_height:True
						cols:2
						spacing:"5sp"
			MDScreen:
				name:'toletapp_screen_search_view'
				SearchView:
					id:search_view
			    
					

<MainToLetApp>:
	screen_manager:screen_manager
	MDTopAppBar:
		id: toolbar
		pos_hint: {"top": 1}
		elevation: 10
		title: "SpaceToLet"
		left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
	
    
	Avatar:
		source:'https://assets-eu-01.kc-usercontent.com/3b3d460e-c5ae-0195-6b86-3ac7fb9d52db/819061b6-7d77-4e3b-96af-1075fb2de5cb/Bugatti%20Chiron%20Super%20Sport%20300%2B.jpeg?width=800&fm=jpg&auto=format'
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
				MDHeroFrom:
					id:hero
					tag:'toletapp'
					size_hint_y:None
					height:Window.size[1]*0.9
					ToLetApp:
						id:my_views
						size_hint:None, None
						size:hero.size

			MDScreen:
				name:'HouseToLet'
				HouseToLet:
			MDScreen:
				name:'RoomsToLet'
				RoomsToLet:
			MDScreen:
				name:'view_rooms'
				heroes_to:[hero_to]
				MDHeroTo:
					id:hero_to
					size_hint_y:None
					height:Window.size[1]*0.9
				ViewCatalogue:
					id:view_catalogue
					size_hint:None, None
					size:hero_to.size
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
			MDScreen: 
				name:'connections'
				on_enter:connect.preinit()
				ConnectionSetting:
					id:connect

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
					    source:'https://assets-eu-01.kc-usercontent.com/3b3d460e-c5ae-0195-6b86-3ac7fb9d52db/819061b6-7d77-4e3b-96af-1075fb2de5cb/Bugatti%20Chiron%20Super%20Sport%20300%2B.jpeg?width=800&fm=jpg&auto=format'
				    MDLabel:
			            text:app.title
					    font_size:dp(20)


				ScrollView:
					Vertical:
						adaptive_height:True
						OneListItem:
							icon:'home'
							text:'Home'
							on_press:
								screen_manager.current = 'ToLetApp'
								nav_drawer.set_state('close')
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
							icon:'connection'
							text:'Network'
							on_press:
								screen_manager.current = 'connections'
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
		
class ViewHouse(MDSmartTile):
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

	def return_home_screen(self):
		self.ids.toletapp_sm.current = 'toletapp_screen_home'
		self.ids.toletapp_return_btn.icon = ''

	def update_searches(self):
		#toggle the screens 
		self.ids.toletapp_sm.current = 'toletapp_screen_search_view'
		self.ids.toletapp_return_btn.icon = 'arrow-left'
		if self.ids.search_input.text:
			self.ids.search_view.search(self.ids.search_input.text)
			self.ids.search_input.text = ''
			self.ids.search_input.hint_text='search'
	


		

	
		

class MainToLetApp(MDFloatLayout):
	screen_manager = ObjectProperty()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def change_screen(self, touch):
		self.screen_manager.current = touch.text
		
class MainApp(MDApp):
	url = StringProperty('')
	screen_manager = ObjectProperty()
	def build(self):
		self.images_list = []
		self.title = 'ToLetApp'
		self.theme_cls.primary_palette = 'Teal'
		return MainToLetApp()
	def on_start(self):
		def callback(permission, result):
			if all([res for res in result]):
				toast('Permission allowed succesfully')
			else:
				toast('could not get permission\n try to enable manually')
		dirs = storagepath.get_pictures_dir()
		self.images = ['https://i.guim.co.uk/img/media/7d04c4cb7510a4bd9a8bec449f53425aeccee895/298_266_1150_690/master/1150.jpg?width=1200&quality=85&auto=format&fit=max&s=4ae508ecb99c15ec04610b617efb3fa7',
						'https://images7.alphacoders.com/345/thumbbig-345553.webp',
						'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRln-3kdi7WJ5fhB7DSmh_T_k_B5PbqJwVr6g&usqp=CAU',
						'https://upload.wikimedia.org/wikipedia/commons/6/6c/Priyanka-chopra-gesf-2018-7565.jpg',
						'https://images2.alphacoders.com/489/thumbbig-489212.webp',
						'https://i.redd.it/hje1fqzt8yi41.jpg',
						'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcbVuoDjA_X1W2ONHZ1_rKjGC0-2FuuoiTTQ&usqp=CAU',
						'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCmpWfyLnOW5BjPvWhJRbZyzM2tmTp0BGIEA&usqp=CAU'
						'https://www.instyle.com/thmb/yi4IXmywb9bqQ5t8PwW935X14_c=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Priyanka-Chopra-Lead-51411e8b9ded419b8839afe25f36db72.jpg',
						'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7Px4EIVER-q5mdTMHzBUeebeSeNgIXDN855peEfZ2BBtknPFidpzV4N7xzUHMZF-yis8&usqp=CAU'
						'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQE8DCWwBTi6XeNFXyCCoUAsrOerJILSZ0xSh57_FAxMw45P3VM_XhCDEJp1NevEd76V9Q&usqp=CAU',
						'https://assets-eu-01.kc-usercontent.com/3b3d460e-c5ae-0195-6b86-3ac7fb9d52db/819061b6-7d77-4e3b-96af-1075fb2de5cb/Bugatti%20Chiron%20Super%20Sport%20300%2B.jpeg?width=800&fm=jpg&auto=format']
		self.toletapp = self.root.ids.my_views.ids.refresh_layout
		data = [{'image':f'{img}', 'housetype':'bugalow','on_release':lambda x=f'{img}': self.change_screen(x)} for img in self.images]
		self.toletapp.data = data
	def change_screen(self, instance):
		self.root.ids.view_catalogue.carousel.clear_widgets()
		self.root.ids.view_catalogue.carousel.add_widget(MDSmartTile(source=instance, size_hint_y=None, radius=['12dp','12dp','12dp','12dp'], height='200dp'))
		self.root.screen_manager.current_heroes = ['hero']
		self.root.screen_manager.current = 'view_rooms'

	def refresh(self):
		Clock.schedule_once(self.refresh_callback, 1)

	def refresh_callback(self, interval):
		print('refreshing')
		
		
		#r = requests.get('http://127.0.0.1:5000/get_images')
		#result = r.json()
		url = self.url + '/get_images'
		self.images_list = []
		UrlRequest(url, on_success=self.success_fetch, on_error=self.error_fetch, on_failure=self.failure_fetch)
		#self.root.ids.my_views.ids.refresh_layout.data = []
		self.root.ids.my_views.ids.refresh_layout.viewclass = 'ViewHouse'
		#self.root.ids.my_views.ids.refresh_layout.data = [{'image':i, 'housetype':'bugalow'} for i in self.images_list]
		
	@mainthread	
	def success_fetch(self, req, result):
	
		print(result.keys())
		
		for img in result['images']:
			self.images_list.append(f'{self.url}/get_file/{img}')
			
		self.root.ids.my_views.ids.refresh_layout.data = []
		self.root.ids.my_views.ids.refresh_layout.viewclass = 'ViewHouse'
		self.root.ids.my_views.ids.refresh_layout.data = [{'image':i, 'housetype':'bugalow', 'on_release':lambda x=f'{i}': self.change_screen(x)} for i in self.images_list]
		self.root.ids.my_views.ids.refresh_layout.refresh_done()
	def error_fetch(self, reg, result):
		self.root.ids.my_views.ids.refresh_layout.refresh_done()
		print(result)
		toast('An error occured while processing yout request')

	def failure_fetch(self, reg, result):
		print('Failure')
		self.root.ids.my_views.ids.refresh_layout.refresh_done() 
		toast('Connection error: \n Check connection and try again')   
	def on_stop(self):
		''' perform some cleaning before the application close and return back the resource consumed'''
		for file in self.images_list:
			os.remove(file)

	def generate_image(self, file):
		filename = f'image-{int(time())}.png'
		r = requests.get(f'{self.url}/get_file/{file}')
		pic = PilImage.open(BytesIO(r.content))
		pic.save(filename)
		print(f'=====================================generated==={filename}===succefully')
		return filename
if __name__ == '__main__':	
	MainApp().run()	 