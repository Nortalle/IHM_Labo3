import kivy

kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class GUI(FloatLayout):
    pass


class GUIApp(App):
    def build(self):
        return GUI()


if __name__ == "__main__":
    GUIApp().run()
