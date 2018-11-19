# Import kivy as you must always do
import kivy

# Specify here the version you are using
kivy.require("1.10.1")

# Import here the modules needed to build you app
from kivy.app import App
from kivy.uix.button import Button


# This is where you app is built. It is a class that inherits from
# App and follow the lifecycle described here:
# https://kivy.org/doc/stable/guide/basic.html#kivy-app-life-cycle
class HelloWorldApp(App):
    def build(self):
        """
        build() is a function that is called when the app is building.
        This is where the widgets (e.g. a button, a label,...) are
        instanciated. It will only be called once as the source
        says (https://github.com/kivy/kivy/blob/5bef72df85015f04b54eda43078fcbf699b57a2b/kivy/app.py#L487)

        In build() you must return the root widget. In this example, a button
        is returned but in general we return a layout containing several widgets.
        """
        return Button(text="Hello world")


if __name__ == "__main__":
    HelloWorldApp().run()
