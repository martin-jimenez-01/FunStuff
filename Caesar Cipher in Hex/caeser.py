from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from caeser_in_hex import *


class caeser(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # add widgets to window
        self.window.add_widget(Image(source ="caeser_logo.png"))

        # label widget 
        self.greeting = Label(
                        text = "Input the message you wish to encrypt.\nThen input a number to shift the message by.",
                        font_size = 50,
                        color = "#d19b2f"
                        )
        self.window.add_widget(self.greeting)

        # text input widget 
        self.msg = TextInput(
                    padding_y = (20,20),
                    size_hint = (1, .5)
                    )
        self.key = TextInput(
                    padding_y = (20,20),
                    size_hint = (1, .5)
                    )
                                
        self.window.add_widget(self.msg)
        self.window.add_widget(self.key)

        # button widget
        self.button = Button(
                        text="Encode",
                        size_hint = (1,.5),
                        bold = True,
                        background_color = "#d19b2f",
                        background_normal = ""
                        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = encoder(self.msg.text, int(self.key.text))

if __name__ == "__main__":
    caeser().run()