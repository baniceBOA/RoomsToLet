from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
import os
Builder.load_file(os.path.join(os.path.dirname(__file__), 'settingscreen.kv'))

class SettingScreen(MDScreen):

    def chevron_back(self,instance):
        app = MDApp.get_running_app()
        app.root.screen_manager.current = app.root.screen_manager.previous()