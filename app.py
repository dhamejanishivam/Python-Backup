from kivy.app import *
from kivy.uix.widget import *
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class grid(GridLayout):
    def __init__(self,**kwargs):
        super(grid,self).__init__(**kwargs)
        # self.cols = 2
        # self.rows = 3

        self.inside = GridLayout()
        self.inside.col = 2

        self.inside.add_widget(Label(text="Hello , inside grid"))
        self.name = TextInput(multiline=True)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Hello , inside grid_1"))
        self.name_1 = TextInput(multiline=True)
        self.inside.add_widget(self.name_1)

        self.inside.add_widget(Label(text="Hello , inside grid_2",font_size=25))
        self.name_2 = TextInput(multiline=True)
        self.inside.add_widget(self.name_2)

        self.add_widget(self.inside)

        self.submit = Button(text='Click Here',font_size=30)
        self.add_widget(self.submit)

class apk(App):
    def build(self):
        return grid()    # Label(text="Hello World")
apk().run()


