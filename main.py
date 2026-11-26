from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
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

    def _update_progress_bar(self, *args):
        self.progress_bar.pos = self.pos
        self.progress_bar.size = self.size

    def _update_Label(self, *args):
        self.progress_bar_counter.pos = self.pos
        self.progress_bar_counter.size = self.size
        self.exorcise_counter.pos = self.pos
        self.exorcise_counter.size = self.size
        self.point_counter.pos = self.pos
        self.point_counter.size = self.size


class MainLayout(BoxLayout):
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
            pos = self.pos,
            size = self.size,
        )

        self.progress_bar_counter = Label(
            text="81%",
            size_hint=(0.4, 0.2),
            pos_hint={"center_y": 0.5, "center_x": 0.48},
            pos = self.pos,
            size = self.size,
        )

        self.exorcise_counter = Label(
            text="16/20",
            size_hint=(0.4, 0.2),
            pos_hint={"center_y": 0.5, "center_x": 0.7},
            pos = self.pos,
            size = self.size,
        )

        self.point_counter = Label(
            text="240pt",
            size_hint=(0.4, 0.2),
            pos_hint={"center_y": 0.5, "center_x": 0.9},
            pos = self.pos,
            size = self.size,
        )

        self.bottom_container = FloatLayout()

        self.add_widget(self.top_section)
        self.add_widget(self.bottom_section)

        self.bottom_section.add_widget(self.bottom_container)
        self.bottom_container.add_widget(self.progress_bar)
        self.bottom_container.add_widget(self.progress_bar_counter)
        self.bottom_container.add_widget(self.exorcise_counter)
        self.bottom_container.add_widget(self.point_counter)

class MyApp(App):
    def build(self):
        self.title = "Progress Bar App"
        return MainLayout()


if __name__ == "__main__":
    MyApp().run()
