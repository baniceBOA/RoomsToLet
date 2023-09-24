from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.floatlayout import FloatLayout
from kivymd.toast import toast


class ClickMe(FloatLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.orientation = 'vertical'
		self.btn = MDFillRoundFlatButton(text='ClickMe')
		self.btn.pos_hint = {'center_x':0.5, 'center_y':0.5}
		self.btn.bind(on_release=self.callback)
		self.add_widget(self.btn)

	def callback(self, *args):
		toast('Woooo you clicked me')

class Main(MDApp):
	def build(self):
		return ClickMe()


Main().run()