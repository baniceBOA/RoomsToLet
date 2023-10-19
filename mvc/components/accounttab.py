from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.boxlayout import MDBoxLayout
import os

Builder.load_file(os.path.join(os.path.dirname(__file__), 'accounttab.kv'))

class AccountTab(MDBoxLayout, MDTabsBase):
    
    def refresh(self,*args):
        print('refreshing')