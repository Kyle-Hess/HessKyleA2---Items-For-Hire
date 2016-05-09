from kivy.app import App
from kivy.app import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
class itemsForHire(App):
    def build(self):
        self.title = "Items For hire v2"
        self.root = Builder.load_file('menu.kv')
        return self.root

    def hireItem(self):
        self.root = Builder.load_file('addItemMenu.kv')
itemsForHire().run()
