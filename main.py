from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from password_generator import PasswordGenerator

kv = """
Screen:
    in_class: text
    MDLabel:
        text: 'Password Generator'
        font_style: 'H4'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}
    MDTextField:
        id: text
        hint_text: 'Enter length of password'
        helper_text: 'Please provide the length of the password to generate!'
        helper_text_mode: "on_focus" 
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
        required: True
           
    MDRectangleFlatButton:
        text: 'Generate'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_press:
            app.generator()
            
    MDLabel:
        text: ''
        id: show
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}

    MDLabel:
        text: 'Created by www.rijumukherjee.com'
        font_style: 'Caption'
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
"""


class Main(MDApp):
    
    in_class = ObjectProperty(None)
    

    def build(self):
        return Builder.load_string(kv)

    def generator(self):
        pg = PasswordGenerator(int(self.root.in_class.text))
        pg.read_titles()
        password = pg.generate()
        label = self.root.ids.show
        label.text = password
    


Main().run()