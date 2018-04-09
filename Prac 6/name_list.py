from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class NameList(App):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.phonebook = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):

        self.title = "Name List"
        self.root = Builder.load_file('name_list.kv')
        self.create_label()
        return self.root

    def create_label(self):

        for name in self.phonebook:

            temp_label = Label(text=name, id=name)

            self.root.ids.entries_box.add_widget(temp_label)


NameList().run()