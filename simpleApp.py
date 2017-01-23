from kivy.app import App
#kivy.require('1.9.0')
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


class Widgets(Widget):
    pass


class Loginscreen(GridLayout):
    def __init__(self, **kwargs):
        super(Loginscreen, self).__init__(**kwargs)
        self.cols = 2


        self.add_widget(Label(text="User Name:"))
        self.user_name = TextInput(multiline=False)
        self.add_widget(self.user_name)

        self.add_widget(Label(text="Password:"))
        self.user_password = TextInput(multiline=False, password=True)
        self.add_widget(self.user_password)

        self.add_widget(Label(text="Autenticacao:"))
        self.user_auth = TextInput(multiline=False)
        self.add_widget(self.user_auth)

class SimpleKivy(App):
    def build(self):
        return Loginscreen()

if __name__ == '__main__':
    SimpleKivy().run()
