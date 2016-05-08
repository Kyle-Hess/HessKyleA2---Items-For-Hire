from kivy.app import App
from kivy.app import Builder

class itemsForHire(App):
    def build(self):
        self.title = "Items For hire v2"
        self.root = Builder.load_file('menu.kv')
        return self.root
itemsForHire().run()