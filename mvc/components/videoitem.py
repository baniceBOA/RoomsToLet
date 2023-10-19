from kivy.properties import StringProperty

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
import os
Builder.load_file(os.path.join(os.path.dirname(__file__), 'videoitem.kv'))

class MDVideo(MDBoxLayout):
    source = StringProperty()
