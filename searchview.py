from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.tab import MDTabsBase
from kivymd.app import MDApp
from kivy.network.urlrequest import UrlRequest
import urllib

kv = '''
#:import CustomViewRefreshLayout customrefreshview.CustomViewRefreshLayout
<SearchItems>:
    ImageLeftWidget:
        source:root.source
        radius:self.width/2
    
    
    
<SearchTab>:
    CustomViewRefreshLayout:
        id:search_refresh_layout
        root_layout:root
        refresh_callback:root.refresh
        viewclass:'SearchItems'
        MDRecycleBoxLayout:
            orientation:'vertical'
            default_size: None, dp(72)
            default_size_hint: 1, None
            adaptive_height:True
            cols:2
            spacing:"5sp"
    
<SearchView>:
    MDBoxLayout:
        MDTabs:
            SearchTab:
                title:'Account'
                id:account
                refresh:root.search_refresh_callback
            SearchTab:
                title:'House'
                id:house
                refresh:root.search_refresh_callback
            SearchTab:
                title:'LandLord'
                id:landlord
                refresh:root.search_refresh_callback
            SearchTab:
                title:'Rooms'
                id:room
                refresh:root.search_refresh_callback

            
        

'''
Builder.load_string(kv)
class SearchItems(ThreeLineAvatarIconListItem):
    source = StringProperty(r'C:\Users\HP\Pictures\_yibs_ke-20220923-0001.webp')
    
    
class SearchTab(MDFloatLayout, MDTabsBase):
    ''' Implements the tabs'''
    refresh = ObjectProperty()
    
    

class SearchView(MDFloatLayout):
    data = ObjectProperty()
    url =  StringProperty('http://127.0.0.1:5000/search')
    tab_screen = ['account', 'landlord', 'house', 'room']
   
    def search(self, query):
        self.data = urllib.parse.urlencode(dict(searchQuery=query))
        self.headers = {'Content-type': 'application/x-www-form-urlencoded','Accept': 'text/plain'}
        UrlRequest(self.url, on_success=self.success, on_error=self.error_fetch, on_failure=self.failure_fetch, req_headers=self.headers, req_body=self.data)


    def search_refresh_callback(self,*args):
        
        UrlRequest(self.url, on_success=self.success, on_error=self.error_fetch, on_failure=self.failure_fetch, req_headers=self.headers, req_body=self.data)

    def success(self, req, result):
        
        for key, value in result.items():
            self.ids[key.lower()].ids.search_refresh_layout.data = self.process_result(key.lower(), value)
            self.tab_screen.append(key.lower())

    def process_result(self, key,  values):
        ''' values if a list of dictionary'''
        # change the value to fit the value in our search items
        data = []
        print(values)
        if key == 'account':
            for v in values :
                mem = dict()
                if 'username' in v:
                    mem['text'] = v['username']
                if 'avatar' in v:
                    mem['source'] = f"http://127.0.0.1:5000/uploads/{v['avatar']}"
                if 'firstname' in v:
                    mem['secondary_text'] = v['firstname']
                if 'secondname' in v:
                    mem['tertiary_text'] = v['secondname']
                data.append(mem)
            
        if key == 'house':
            for v in values :
                mem = dict()
                if 'name' in v:
                    mem['text'] = v['name']
                if 'pictures' in v:
                    mem['source'] = f"http://127.0.0.1:5000/uploads/{v['pictures']}"
                if 'location' in v:
                    mem['secondary_text'] = v['location']
                if 'region' in v:
                    mem['tertiary'] = v['region']
                data.append(mem)
        if key == 'room':
            for v in values :
                mem = dict()
                if 'hotelname' in v:
                    mem['text'] = v['hotelname']
                if 'picture' in v:
                    mem['source'] = f"http://127.0.0.1:5000/uploads/{v['picture']}"
                if 'location' in v:
                    mem['secondary_text'] = v['location']
                if 'region' in v:
                    mem['tertiary'] = v['region']
                data.append(mem)
        if key == 'landlord':
            for v in values :
                mem = dict()
                if 'names' in v:
                    mem['text'] = v['names']
                if 'picture' in v:
                    mem['source'] = f"http://127.0.0.1:5000/uploads/{v['picture']}"
                if 'location' in v:
                    mem['secondary_text'] = v['location']
                if 'phone_no' in v:
                    mem['tertiary'] = v['phone_no']
                data.append(mem)
        self.ids[key].ids.search_refresh_layout.refresh_done()
        return data



        
    def error_fetch(self, reg, result):
        for tab in self.tab_screen:
            self.ids[tab].ids.search_refresh_layout.refresh_done()
        print('error')
    def failure_fetch(self, req, result):
        self.ids.account.ids.search_refresh_layout.refresh_done()
        print('failure')

class SearchViewApp(MDApp):
     def build(self):
        return SearchView()

    

if __name__ == '__main__':
    SearchViewApp().run()


