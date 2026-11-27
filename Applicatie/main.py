from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, Rectangle
from kivy.graphics import Color, RoundedRectangle


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

class BadgeButton(ButtonBehavior,BoxLayout):
    def __init__(self, image_source, title, **kwargs):
        super().__init__(
            orientation="vertical",
            spacing=2,
            padding=20,
            size_hint=(None, None),
            height=100,
            **kwargs
        )
        with self.canvas.before:
            Color(0.35, 0.35, 0.35, 1)
            self.bg = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[2]
            )
        self.bind(pos=self.update_bg, size=self.update_bg)

        # Image at the top
        Foto = Image(
            source=image_source,
            fit_mode="contain",
            size_hint=(1, 0.75),
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

class BadgeRow(BoxLayout):
    def __init__(self, badge1, badge2, badge3, **kwargs):
            super().__init__(**kwargs)

            layout = BoxLayout(
                orientation='horizontal',
                padding=25,
                spacing=15
            )

            layout.add_widget(badge1)
            layout.add_widget(badge2)
            layout.add_widget(badge3)

            self.add_widget(layout)

class Section(BoxLayout):
    def __init__(self, bg_color=(1, 1, 1, 1), **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*bg_color)
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(pos=self._update_rect, size=self._update_rect)

    def _update_rect(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size



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
        BadgesButton.bind(on_press=self.GoToBadges)

    def GoToSelect(self, instance):
        self.manager.current = "select"
    def GoToBadges(self, instance):
         self.manager.current = "badge"

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

class TrainingPage(BoxLayout, Screen):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.top_section = Section(
            bg_color=(0.15, 0.15, 0.2, 1),
            size_hint=(1, 0.9),
        )

        self.bottom_section = Section(
            bg_color=(0.25, 0.25, 0.35, 1),
            size_hint=(1, 0.1),
        )

        self.progress_bar = Section(
            bg_color=(0.1, 0.6, 0.1, 1),
            size_hint=(0.4, 0.2),
            pos_hint={"center_y": 0.5, "center_x": 0.25},
        )

        self.progress_bar_counter = Label(
            text="81%",
            size_hint=(0.4, 0.2),
            pos_hint={"center_y": 0.5, "center_x": 0.48},
        )

        self.exorcise_counter = Label(
            text="16/20",
            size_hint=(0.4, 0.2),
            pos_hint={"center_y": 0.5, "center_x": 0.7},
        )

        self.point_counter = Label(
            text="240pt",
            size_hint=(0.4, 0.2),
            pos_hint={"center_y": 0.5, "center_x": 0.9},
        )

        self.bottom_container = FloatLayout()

        self.add_widget(self.top_section)
        self.add_widget(self.bottom_section)

        self.bottom_section.add_widget(self.bottom_container)
        self.bottom_container.add_widget(self.progress_bar)
        self.bottom_container.add_widget(self.progress_bar_counter)
        self.bottom_container.add_widget(self.exorcise_counter)
        self.bottom_container.add_widget(self.point_counter)

class BadgesPage(BoxLayout, Screen):
    def __init__(self, **kwargs):
            super().__init__(orientation="vertical", **kwargs)

            layout = BoxLayout(
                orientation='vertical',
                padding=80,
                spacing=30
            )

            TitleText = Label(
                text="Badges",
                font_size=30,
                pos_hint={"center_x": 0.5}
            )

            badge1 = BadgeButton(
                 image_source="Images/Test.jpg",
                 title="Test",
                 pos_hint={"center_x": 0.5}
            )
            badge2 = BadgeButton(
                image_source="Images/Test.jpg",
                title="Test",
                pos_hint={"center_x": 0.5}
            )
            badge3 = BadgeButton(
                image_source="Images/Test.jpg",
                title="Test",
                pos_hint={"center_x": 0.5}
            )
            
            

            badgeRow1 = BadgeRow(
                 badge1=badge1,
                 badge2=badge2,
                 badge3=badge3
            )
            self.add_widget(badgeRow1)

            self.add_widget(layout)


class Myapp(App):
    def build(self):
        self.title = "App"

        Window.size = (300, 600)

        manager = ScreenManager()

        manager.add_widget(MainPage(name="main"))
        manager.add_widget(SelectPage(name="select"))
        manager.add_widget(TrainingPage(name="train"))
        manager.add_widget(BadgesPage(name="badge"))

        manager.current = "main"

        return manager

Myapp().run()