import kivy
from kivy.app import App
from kivy.graphics.vertex_instructions import Rectangle
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.11.1')


class LoginView(App):
    def build(self):
        with self.canvas:
            Rectangle(pos=self.pos, size=self.size)
        layout = BoxLayout(padding=10, orientation='vertical')
        inside_layout = BoxLayout()
        inside_layout.add_widget(Button(text='Hello World'))
        layout.add_widget(inside_layout)
        return layout


LoginView().run()
