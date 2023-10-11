from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import StringProperty, NumericProperty

kv = '''
<ConnectionSetting>:
    MDScrollView:
        pos_hint:{'top':0.9}
        MDBoxLayout:
            orientation:'vertical'
            adaptive_height:True
            padding:[15, 0, 15, 0]
            MDLabel:
                text:'Connection'
                font_size:'18sp'
                bold:True
                size_hint_y:None
                height:dp(50)
            MDLabel:
                text:'Host'
                font_size:'15sp'
                size_hint_y:None
                height:dp(50)
            MDTextField:
                id:host_id
                mode:'round'
                size_hint_y:None
                height:dp(50)
            MDLabel:
                text:'Port'
                size_hint_y:None
                height:dp(50)
            MDTextField:
                id:port_id
                mode:'round'
                size_hint_y:None
                height:dp(50)
            MDFillRoundFlatButton:
                text:'Connect'
                font_size:'12sp'
                on_release:root.on_connect()
    


'''
Builder.load_string(kv)

class ConnectionSetting(MDFloatLayout):
    host = StringProperty('localhost')
    port = NumericProperty(5000)

    def on_connect(self):
        if self.ids.host_id.text and self.ids.port_id.text:
            try:
                self.port = int(self.ids.port_id.text)
            except Exception as e:
                self.ids.port_id.error = True
                self.ids.port_id.helper_mode = 'on_error'
                self.ids.port_id.helper_text = 'Port should be a number'
            self.host = self.ids.host_id.text
            self.create_url(self.host, self.port)
        else:
            self.ids.host_id.error = True
            self.ids.host_id.helper_text = 'The Host is Invalid'
            self.ids.port_id.text.error = True
        self.create_url(self.host, self.port)

    def create_url(self, host, port):
        url = f'http://{host}:{port}/'
        app = App.get_running_app()
        try:
            app.url = url
            print('created url successfully')
        except Exception as e:
            print(f'{app} does not has attribute url \n Raised and error {e}')
    def preinit(self):
        self.ids.host_id.text = self.host
        self.ids.port_id.text = str(self.port)


        
            

            
