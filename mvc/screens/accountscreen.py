from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.lang import Builder
import os

from components import AccountTab
Builder.load_file(os.path.join(os.path.dirname(__file__), 'accountscreen.kv'))

class AccountScreen(MDScreen):
    username = StringProperty('username')
    region = StringProperty('region')
    like = StringProperty('19434')
    source = StringProperty("http://localhost:5000//get_file/IMG-20220627-WA0005.jpg")

    def chevron_back(self,instance):
        app = MDApp.get_running_app()
        app.root.screen_manager.current = app.root.screen_manager.previous()
