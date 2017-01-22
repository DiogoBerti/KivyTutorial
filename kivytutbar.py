import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class SampleGridLayout(GridLayout):
    pass

class SampleApp(App):
    def build(self):
        return SampleGridLayout()

sample = SampleApp()
sample.run()
