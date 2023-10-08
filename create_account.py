from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivymd.uix.label import MDLabel
from kivy.factory import Factory
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import requests
kv = '''
<CreateAccount>:
	password:password
	repeat_password:repeat_password
	username:username
	firstname:firstname
	secondname:secondname
	image:image
	email:email
	btn_create:btn_create
	MDLabel:
		text:' CreateAccount'
		pos_hint:{'center_y':0.85, 'center_x':0.5}

	ClickableImage:
		id:image
		source:'https://assets-eu-01.kc-usercontent.com/3b3d460e-c5ae-0195-6b86-3ac7fb9d52db/819061b6-7d77-4e3b-96af-1075fb2de5cb/Bugatti%20Chiron%20Super%20Sport%20300%2B.jpeg?width=800&fm=jpg&auto=format'
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
				on_text:root.check_email(email.text)
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
				on_text:root.check_username(username.text)
				
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
				hint_text:'repeat_password'
				size_hint_x:None
				width:dp(260)
				pos_hint:{'center_x':0.5}
				helper_text_mode:'persistent'
				helper_text:'repeat_password'
				on_text:root.validate_password(repeat_password.text)

			MDFillRoundFlatButton:
				id:btn_create
				text:'Create'
				pos_hint:{'center_x':0.5}
				on_release:root.create()

'''
Builder.load_string(kv)

class ContentBottomSheet(MDBoxLayout):
	msg = StringProperty()
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.label = MDLabel(text=self.msg, valign='center', halign='center')
		self.add_widget(self.label)
class CreateAccount(MDFloatLayout):
	secondname = ObjectProperty()
	firstname = ObjectProperty()
	username = ObjectProperty()
	email = ObjectProperty()
	password = ObjectProperty()
	repeat_password = ObjectProperty()
	normal_color = ColorProperty()
	image = ObjectProperty()
	btn_create = ObjectProperty()
	url = 'http://127.0.0.1:5000/create_account'
	def create(self):
		'''perform validation of the data '''
		screen = self.parent.parent
		if self.username.text:
			pass
		else:
			self.username.error = True
			self.username.helper_text = 'username is required '
		if self.password.text:
			pass
		else:
			self.password.error = True
			self.password.helper_text = 'password is required'
		if self.password.text and self.username.text and self.repeat_password.text:
			self.create_account()
			screen.current = 'login'
		else:
			self.password.error = True
			self.username.error = True
			self.repeat_password = True
			self.custom_sheet = MDCustomBottomSheet(screen=Factory.ContentBottomSheet(msg='the fields in red are required'))
			self.custom_sheet.open()
			
	def validate_password(self, password):
		''' check if the repeat passwprd it the same as the password '''
		if self.password.text:
			if password == self.password.text:
				self.repeat_password.helper_text = 'Valid'
			else:
				self.repeat_password.helper_text = 'Invalid'
				self.repeat_password.error = True


	def check_password(self, password):
		''' check if the password is valid '''
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
					self.password.helper_text_color_normal =  [0, 1, 0, 1]
	def check_email(self, email):
		if not '@' in email:
			self.email.helper_text_mode = 'on_error'
			self.email.error = True
			self.email.helper_text = 'Invalid Email' 
		else:
			self.email.error = False
			self.email.helper_text = 'Valid'
			self.normal_color = [0, 1, 0, 1]
			self.email.helper_text_color_normal =  self.normal_color
	def check_username(self, username):
		''' check if the username is on the database '''
		url = 'http://127.0.0.1:5000/check_username'
		resp = requests.post(url, data={'username':username})
		if 'Invalid' in str(resp.content):
			self.username.error = True
			self.username.helper_text = 'The username is already in use kindly change to a unigue username '
			self.username.error = True
		elif self.username.text:
			self.username.helper_text = 'valid'
			self.username.error = False


	def create_account(self):
		''' create the user account with the provided details '''
		firstname = self.firstname.text
		secondname = self.secondname.text
		email = self.email.text
		username = self.username.text
		password = self.password.text
		image = self.image.source
		url = 'http://127.0.0.1:5000/create_account'
		data = {
		    'firstname':firstname,
		    'secondname':secondname,
		    'email':email,
		    'username':username,
		    'password':password,
		    'image':image
		}
		resp = requests.post(url, data=data)






