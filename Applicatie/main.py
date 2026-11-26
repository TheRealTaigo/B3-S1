from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=80,
            spacing=30
        )

        WelkomText = Label(
            text="Welkom!",
            font_size=30,
            pos_hint={"center_x": 0.5}
        )

        StartButton = Button(
            text = "Start",
            size_hint = (None, None),
            size = (350,100),
            pos_hint={
                "center_x": 0.5
            }
        )
        BadgesButton = Button(
            text = "Badges",
            size_hint = (None, None),
            size = (350,100),
            pos_hint={
                "center_x": 0.5
            }
        )

        SettingsButton = Button(
            text = "Instellingen",
            size_hint = (None, None),
            size = (350,100),
            pos_hint={
                "center_x": 0.5
            }
        )

        layout.add_widget(WelkomText)
        layout.add_widget(StartButton)
        layout.add_widget(BadgesButton)
        layout.add_widget(SettingsButton)
        self.add_widget(layout)
        
        StartButton.bind(on_press=self.GoToSelect)

    def GoToSelect(self, instance):
        self.manager.current = "select"


class OefeningButton(ButtonBehavior, BoxLayout):

    def __init__(self, image_source, title, **kwargs):
        super().__init__(
            orientation="vertical",
            spacing=5,
            padding=8,
            size_hint=(1, None),
            height=150,
            **kwargs
        )

        # Button background
        from kivy.graphics import Color, RoundedRectangle

        with self.canvas.before:
            Color(0.35, 0.35, 0.35, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[8]
            )

        self.bind(pos=self.update_bg, size=self.update_bg)

        # Image at the top
        Foto = Image(
            source=image_source,
            fit_mode="contain",
            size_hint=(1, 0.75)
        )

        # Text underneath
        Naam = Label(
            text=title,
            font_size=20,
            size_hint=(1, 0.25)
        )

        self.add_widget(Foto)
        self.add_widget(Naam)

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size


class SelectPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            padding=80,
            spacing=30
        )

        SelectText = Label(
            text="Selecteer een oefening",
            font_size=30,
            pos_hint={"center_x": 0.5}
        )
        Oefening1 = OefeningButton(
            image_source="Images/Pushup.png",
            title="Push up"
        )
        Oefening2 = OefeningButton(
            image_source="Images/Test.jpg",
            title="Oefening 2 naam"
        )
        Oefening3 = OefeningButton(
            image_source="Images/Test.jpg",
            title="oefening 3 naam"
        )

        Oefening1.bind(on_press=self.Oefening1)
        Oefening2.bind(on_press=self.Oefening2)
        Oefening3.bind(on_press=self.Oefening3)
        


        layout.add_widget(SelectText)
        layout.add_widget(Oefening1)
        layout.add_widget(Oefening2)
        layout.add_widget(Oefening3)

        self.add_widget(layout)

    def Oefening1(self,instance):
        self.manager.current = "train"

    def Oefening2(self,instance):
            self.manager.current = "train"

    def Oefening3(self,instance):
            self.manager.current = "train"


class TrainingPage(Screen):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)


class Myapp(App):
    def build(self):
        Window.size = (300, 600)

        manager = ScreenManager()

        manager.add_widget(MainPage(name="main"))
        manager.add_widget(SelectPage(name="select"))
        manager.add_widget(TrainingPage(name="train"))

        manager.current = "main"

        return manager

Myapp().run()