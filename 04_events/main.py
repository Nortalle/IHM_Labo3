import kivy

kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from functools import partial


class PlusMinusWidget(BoxLayout):
    pass


class GUI(FloatLayout):
    def __init__(self, **kwargs):
        # Always call super() when overriding a function of the super class
        super().__init__(**kwargs)
        print(self.ids)

        # Step 1: Retrieve your widgets (here pmw1 i.e. PlusMinusWidget 1)
        self._pmw1 = self.ids.pmw1
        self._lbl1 = self.ids.lbl1

        # You can chain the call of `ids` to retrieve nested widget
        # like here with `btn_plus`
        btn_plus_w1 = self._pmw1.ids.btn_plus
        btn_plus_w1.text = "Add 1"

        btn_minus_w1 = self._pmw1.ids.btn_minus

        # Step 2: add the callback function, do not add () at the end of the function
        # we want to pass the function itself, not to call it directly
        # if you need to have a function that takes arguments there are 2 solutions:

        # Solution 1: use class members (e.g. self._mywidgetXXX)
        btn_plus_w1.on_release = self.add_one_to_label

        # Solution 2: use partial functions see: https://docs.python.org/3/library/functools.html#functools.partial
        # substract_one_to_lbl1 is a function where the argument `label` has been
        # set to `self._lbl1`
        substract_one_to_lbl1 = partial(self.substract_one_to_label, self._lbl1)
        btn_minus_w1.on_release = substract_one_to_lbl1

        # Note: here we define the behaviour of pmw1 in GUI class. This is fine
        # for this example but if we want to use PlusMinusWidget as an independant
        # component with its own reusable logic. We must handle the events directly
        # in PlusMinusWidget classpmw1 in GUI class. This is fine
        # for this example but if we want to use PlusMinusWidget as an independant
        # component with its own reusable logic. We must handle the events directly
        # in PlusMinusWidget class and add functions to be called externally (e.g.
        # `def on_plus_button_clicked(self)`

    def add_one_to_label(self):
        count = int(self._lbl1.text)
        count += 1
        self._lbl1.text = str(count)

    def substract_one_to_label(self, label):
        count = int(label.text)
        count -= 1
        label.text = str(count)


class GUIApp(App):
    def build(self):
        return GUI()


if __name__ == "__main__":
    GUIApp().run()
