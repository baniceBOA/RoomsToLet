from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.properties import ObjectProperty
from kivy.lang import Builder
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'searchtab.kv'))



class SearchTab(MDFloatLayout, MDTabsBase):
    ''' Implements the tabs'''
    refresh = ObjectProperty()