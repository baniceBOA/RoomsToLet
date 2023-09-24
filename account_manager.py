from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder

kv = '''
#:import Window kivy.core.window.Window
<AccountManager>:
	ScrollView:
		pos_hint:{'top':0.9}
		MDBoxLayout:
			adaptive_height:True
			orientation:'vertical'
			spacing:'2sp'
			ClickableImage:
				pos_hint:{'center_x':0.5}
				source:'D:/files/images/IMG-20220313-WA0011.jpg'
				radius:70,70,70,70
				size_hint_x:None 
				width:Window.size[0]*0.25
				size_hint_y:None
				height:Window.size[0]*0.25
			MDSeparator:
			MDLabel:
				pos_hint:{'center_x':0.5}
				size_hint_y:None
				height:dp(56)
				text:'FIrstname'
			MDSeparator:
			MDLabel:
				pos_hint:{'center_x':0.5}
				size_hint_y:None
				height:dp(56)
				text:'secondName'
			MDSeparator:
			MDLabel:
				pos_hint:{'center_x':0.5}
				size_hint_y:None
				height:dp(56)
				text:'Username'
			MDSeparator:
			MDFillRoundFlatButton:
				pos_hint:{'center_x':0.5}
				size_hint_y:None
				text:'logout'

'''
Builder.load_string(kv)
class AccountManager(MDFloatLayout):
	pass