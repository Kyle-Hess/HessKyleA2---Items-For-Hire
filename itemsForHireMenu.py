from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class ItemsForHireApp(App):
    """
    Main program - Kivy app to demo phonebook system
    """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super(ItemsForHireApp, self).__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.itemsList = []

        items = open("items.csv", "r")
        for line in items:
            match = line.strip().split(",")
            name = match[0]
            description = match[1]
            price = match[2]
            hire = match[3]
            self.itemsList.append([match[0], match[1], match[2], match[3]])
        items.close()

        # Construct main app

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Phonebook Demo - Popup & Buttons"
        self.root = Builder.load_file('addItemMenu.kv')
        self.create_entry_buttons()
        return self.root

    ####
    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """

        for is_star in self.itemsList:
            if is_star[3] == 'out':
                temp_button = Button(text='{0} ({1}) = ${2}*'.format(*is_star))
                temp_button.bind(on_release=self.press_entry)
            else:
                temp_button = Button(text='{} ({}) = ${}'.format(*is_star))
                temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)

        '''
        for name in self.itemsList:
            # create a button for each phonebook entry
            temp_button = Button(text='{0} ({1}) = ${2}*'.format(*name))
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_button)
        '''
    ####
    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        name = instance.text
        self.status_text = "{}".format(name, self.itemsList[0])
        instance.state = 'down'
    ####
    def hiring_item(self):


        '''
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
        :return: None
        """
        self.status_text = "Enter details for new Item entry"
        # this opens the popup
        self.root.ids.popup.open()

    ####
    def press_save(self, item_name, description, price):
        """
        Handler for pressing the save button in the add entry popup - save a new entry to memory
        :param item_name: name text input (from popup GUI)
        :param description: phone number text input (string)
        :return: None
        """
        self.itemsList.append([item_name, description, price, 'in'])
        # change the number of columns based on the number of entries (no more than 5 rows of entries)
        self.root.ids.entriesBox.cols = len(self.itemsList) // 5 + 1
        # add button for new entry (same as in create_entry_buttons())
        temp_button = Button(text=item_name)
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
        :return: None
        """
        self.root.ids.itemName.text = ""
        self.root.ids.itemDescription.text = ""
        self.root.ids.itemPrice.text = ""

    def press_clear(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        # use the .children attribute to access all widgets that are "in" another widget
        for instance in self.root.ids.entriesBox.children:
            instance.state = 'normal'
        self.status_text = ""
    ####
    def press_cancel(self):
        """
        Handler for pressing cancel in the add entry popup
        :return: None
        """
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""

    def clear_canvas(self):
        self.canvas.clear()
        with self.canvas:
            self.create_entry_buttons()

ItemsForHireApp().run()