from kaki.app import App
from kivymd.app import MDApp
from kivy.factory import Factory

class LiveApp(App, MDApp):
	CLASSES = {
	'MainToLetApp':'app'
	}

	AUTORELOADER_PATHS = [
	('.', {'recursive':True})
	]
	def build_app(self, *args):
		return Factory.MainToLetApp()

LiveApp().run()
