from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from create_account import ContentBottomSheet
from kivy.factory import Factory
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.properties import ObjectProperty
import requests
kv = '''
<Login>:
	create_account:create_account
	password:password
	username:username
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
				on_press:root.login()
	
	MDLabel:
		text:"Don't have an Account"
		pos_hint:{'center_y':0.22, 'center_x':0.8}
	MDFillRoundFlatButton:
		id:create_account
		text:'Create Account'
		pos_hint:{'top':0.2, 'center_x':0.5}
		on_press:root.account_screen()
'''
Builder.load_string(kv)

class Login(MDFloatLayout):
	''' create a login of the application'''
	username = ObjectProperty()
	password =  ObjectProperty()
	create_account = ObjectProperty()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	def login(self):
		log_in = None
		url = url = 'http://192.168.137.1:5000/login'
		if self.password and self.username:
			data = {'username':self.username.text,
					'password':self.password.text}
			resp = requests.post(url, data=data)
			if 'succesfull' in str(resp.content):
				screen = self.parent.parent
				screen.current = 'landlord'
			else:
				self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentBottomSheet(msg='Invalid username or password'))
				self.custom_sheet.open()

		else:
			self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentBottomSheet(msg='Invalid username or password'))
			self.custom_sheet.open()
	def check_password(self, password):
		''' check the password if it is strong enough'''
		
		if len(password) < 8:
			#the password is weak or mild 
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
					self.password.helper_text_color_normal =  [0, 1, 0, 1]

	def account_screen(self, *args):
		screen = self.parent.parent
		screen.current = 'create_account'