from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class itemInfo:
    #This class turns the items into objects
    def __init__(self, name="default", description="default", price="0", status="in"):
        self.name = name
        self.description = description
        self.price = price
        self.status = status

    def __str__(self):
        return "{}{}{}{}".format(self.name, self.description, self.price, self.status)


class item_load:
    #Stores the items once loaded
    def __init__(self, item_file, **kwargs):
        self.itemsList = []
        self.item_match(item_file)
# loads the item from the cvs file
    def item_match(self, item_file):
        items = open(item_file, "r")
        for line in items:
            match = line.strip().replace(" ", " ").split(",")
            self.itemsList.append(itemInfo(match[0], match[1], match[2], match[3]))
        items.close()


class ItemsForHireApp(App):
    """
    Main program
    """
    status_text = StringProperty()

        # Construct main app
    def __init__(self):
        super(ItemsForHireApp, self).__init__()
        self.item_vault = item_load("items.csv")
        self.status_text = "Choose action from the left, then select items on the right."

    def build(self):
        """
        Build the Kivy GUI
        """
        self.title = "Items For Hire - Hire & Return Items"
        self.root = Builder.load_file('addItemMenu.kv')
        self.create_entry_buttons()
        return self.root

    ####
    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        """
        #Loops through the items and checks whether they're in stock
        for item in self.item_vault.itemsList:
            if item.status == 'out':
                temp_button = Button(text=item.name)
                temp_button.background_color = (1, 1, 0, 1)
                #changes the colour of out of stock items
                temp_button.bind(on_release=self.press_entry)
            else:
                temp_button = Button(text=item.name)
                temp_button.background_color = (0, 1, 1, 1)
                temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)


    ####
    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        """
        for item in self.item_vault.itemsList:
            if item.name == instance.text:
                self.status_text = "{}, ${}, {}".format(item.description, item.price, item.status)
                instance.state = 'down'

    ####
    def hiring_item(self):

        '''
        Hires Selected items

        for hired_items in self.itemsList:
            if hired_items[3] == 'in':
                temp_button = Button(text='{} ({}) = ${}'.format(*hired_items))
                temp_button.bind(on_release=self.press_entry)
                self.root.ids.entriesBox.add_widget(temp_button)
        '''
        #hire = str(input("Enter the Item you want to hire: "))
        temp_button = str(self.root.ids.addButton.on_release)
        hire = temp_button

        for i, item_name in enumerate(self.itemsList):
            if item_name[0] == hire:
                temp = list(self.itemsList[i])
                temp[3] = "out"
                self.itemsList[i] = tuple(temp)
        if hire == '':
            print("Nothing was hired")
        else:
            print('{} | {} '.format(hire, "Has been hired"))
            temp_button = Button(text='{} | {} '.format(hire, "Has been hired"))
            temp_button.bind(on_release=self.press_entry)


    ####

    def return_item(self):
        """
           Returns the selected items
        """

        for return_items in self.itemsList:
            if return_items[3] == 'out':
                print('{}: {} ({}) = ${}'.format("Out Items", *return_items))

        returning = str(input("Enter the Item you want to Return: "))
        for i, item_name in enumerate(self.itemsList):
            if item_name[0] == returning:
                temp = list(self.itemsList[i])
                temp[3] = "in"
                self.itemsList[i] = tuple(temp)
        if returning == '':
            print("Nothing was returned")
        else:
            print('{} | {} '.format(returning, "Has now returned"))

    ####
    def press_add(self):
        """
        Handler for pressing the add button
        """
        self.status_text = "Enter details for new Item entry"
        # this opens the popup
        self.root.ids.popup.open()

    ####
    def press_save(self, name, description, price, status = 'in'):
        """
        Handler for pressing the save button in the add entry popup - save a new entry to memory
        """
        #item_load.itemsList = ([name, description, price, status])
        self.item_vault.itemsList.append([name, description, price, status])
        # change the number of columns based on the number of entries (no more than 5 rows of entries)
        self.root.ids.entriesBox.cols = len(self.item_vault.itemsList) // 5 + 1
        # add button for new entry (same as in create_entry_buttons())
        temp_button = Button(text=name)
        temp_button.background_color = (0, 1, 1, 1)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entriesBox.add_widget(temp_button)
        # close popup
        self.root.ids.popup.dismiss()
        self.clear_fields()

    ####
    def clear_fields(self):
        """
        Clear the text input fields from the add entry popup
        If we don't do this, the popup will still have text in it when opened again
        """
        self.root.ids.itemName.text = ""
        self.root.ids.itemDescription.text = ""
        self.root.ids.itemPrice.text = ""

    def press_clear(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        """
        for instance in self.root.ids.entriesBox.children:
            instance.state = 'normal'
        self.status_text = ""

    ####
    def press_cancel(self):
        """
        Handler for pressing cancel in the add entry popup
        """
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""

# Handler for clearing the canvas when selecting List Items Button
    def clear_canvas(self):
        self.canvas.clear()
        with self.canvas:
            self.create_entry_buttons()

ItemsForHireApp().run()