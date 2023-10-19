import os
os.environ['KIVY_VIDEO'] = 'ffpyplayer'


from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
import os
from screens import HomeScreen, SearchView, AccountScreen, SettingScreen

Builder.load_file(os.path.join(os.path.dirname(__file__), 'main.kv'))
Window.top = 1
Window.left = 988
Window.size = (400, 688)
class SpaceToletApp(MDFloatLayout):
    screen_manager = ObjectProperty()

    def callback(self, instance):
        if instance.icon == 'magnify':
           self.screen_manager.current = 'search'
        if instance.icon == 'account':
            self.screen_manager.current = 'account'
        if instance.icon == 'cog':
            self.screen_manager.current = 'settings'
    def action_callback(self, instance):
        print(instance)  
        self.screen_manager.current = 'home'

class SpaceTolet(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.material_style = "M3"

        return SpaceToletApp()
    

if __name__ == '__main__':
    SpaceTolet().run()