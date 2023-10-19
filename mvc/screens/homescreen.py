from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.clock import Clock
import os
from components import CustomViewRefreshLayout, MDRecycleBoxLayout, House

Builder.load_file(os.path.join(os.path.dirname(__file__), 'homescreen.kv'))


class HomeScreen(MDScreen):

    data = ListProperty()
    refresh_layout = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.load_data, 2)
    
    

    def refresh(self, *args):
        print('refreshing', *args)
        values = ["http://localhost:5000//get_file/IMG-20220630-WA0000_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220630-WA0001.jpg",
			"http://localhost:5000//get_file/IMG-20220630-WA0001_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220701-WA0000.jpg",
			"http://localhost:5000//get_file/IMG-20220701-WA0000_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220701-WA0001.jpg",
			"http://localhost:5000//get_file/IMG-20220701-WA0001_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220312-WA0002.jpg",
			"http://localhost:5000//get_file/IMG-20220312-WA0002_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220402-WA0001.jpg",
			"http://localhost:5000//get_file/IMG-20220402-WA0001_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220402-WA0002.jpg",
			"http://localhost:5000//get_file/IMG-20220402-WA0002_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220404-WA0009.jpg",
			"http://localhost:5000//get_file/IMG-20220404-WA0009_remove_bg.png",]
        for pic in values:
            data = {}
            data['source'] = pic
            data['account_avatar'] = pic
            data['name'] = 'Home'
            data['region'] ='kakamega'
            self.data.append(data)
        
        self.ids.refresh_layout.refresh_done()

    def load_data(self, interval):
        print('processing data')
        values =  [
			"http://localhost:5000//get_file/IMG-20220620-WA0000.jpg",
			"http://localhost:5000//get_file/IMG-20220620-WA0000_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220623-WA0000.jpg",
			"http://localhost:5000//get_file/IMG-20220623-WA0000_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220623-WA0001.jpg",
			"http://localhost:5000//get_file/IMG-20220623-WA0001_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220623-WA0002.jpg",
			"http://localhost:5000//get_file/IMG-20220623-WA0002_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220624-WA0000.jpg",
			"http://localhost:5000//get_file/IMG-20220624-WA0000_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220624-WA0002.jpg",
			"http://localhost:5000//get_file/IMG-20220624-WA0002_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220625-WA0000.jpg",
			"http://localhost:5000//get_file/IMG-20220625-WA0000_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220625-WA0001.jpg",
			"http://localhost:5000//get_file/IMG-20220625-WA0001_remove_bg.png",
			"http://localhost:5000//get_file/IMG-20220626-WA0003.jpg"]
        
        for pic in values:
            data = {}
            data['source'] = pic
            data['account_avatar'] = pic
            data['name'] = 'Home'
            data['region'] ='kakamega'
            self.data.append(data)
    
        

            
