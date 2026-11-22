from kivy.app import App
from kivy.uix.label import Label


class PushupPage(App):

    def build(self):
        return Label(text="Push-ups")


if __name__ == "__main__":
    PushupPage().run()