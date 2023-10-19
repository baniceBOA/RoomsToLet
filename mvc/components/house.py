from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBodyTouch
from kivy.properties import StringProperty
from kivy.lang import Builder
import os

class RightContainer(IRightBodyTouch, MDBoxLayout):
    pass
Builder.load_file(os.path.join(os.path.dirname(__file__), 'house.kv'))

class House(MDBoxLayout):
    source = StringProperty()
    account_avatar = StringProperty()
    name = StringProperty()
    region = StringProperty()
    