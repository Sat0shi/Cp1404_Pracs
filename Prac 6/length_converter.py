
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class LengthConverterApp(App):

    def build(self):
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('length_converter.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = int(value) * 1.60934

        except ValueError:
            result = 0
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment, value):
        try:
            result = int(value) + int(increment)

        except ValueError:
            result = 0 + int(increment)
        self.root.ids.input_number.text = str(result)


LengthConverterApp().run()