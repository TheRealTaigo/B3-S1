from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle


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


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.top_section = Section(
            bg_color=(0.15, 0.15, 0.2, 1),
            size_hint=(1, 0.8),
        )

        self.bottom_section = Section(
            bg_color=(0.25, 0.25, 0.35, 1),
            size_hint=(1, 0.2),
        )

        self.add_widget(self.top_section)
        self.add_widget(self.bottom_section)


class MyApp(App):
    def build(self):
        self.title = "Progress Bar App"
        return MainLayout()


if __name__ == "__main__":
    MyApp().run()
