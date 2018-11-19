import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class GUI(FloatLayout):
    pass

class GUIApp(App):
    def build(self):
        return GUI()


if __name__ == '__main__':
    GUIApp().run()
