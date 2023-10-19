from kivymd.uix.label import MDLabel
from kivy.lang import Builder
import os
Builder.load_file(os.path.join(os.path.dirname(__file__), 'header.kv'))
class Header(MDLabel):
    pass