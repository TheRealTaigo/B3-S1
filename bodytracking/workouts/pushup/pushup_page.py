from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window


class PushupPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Page title
        self.title = Label(
            text="Push-ups",
            font_size=30
        )
        self.add_widget(self.title)

        # Start workout button
        self.start_button = Button(
            text="Start Workout",
            size_hint=(1, 0.2)
        )
        self.add_widget(self.start_button)
        self.start_button.bind(on_press=self.start_workout)
    def start_workout(self):
        Window.fullscreen = True
