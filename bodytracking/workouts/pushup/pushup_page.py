from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
class PushupPage(Screen):
    def __init__(self, **kwargs):
        super(PushupPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical")
        # Add your widgets and layout here
        self.add_widget(self.layout)