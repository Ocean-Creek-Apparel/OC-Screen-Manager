import sqlite3
import tkinter as tk

class Location:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        
    def __str__(self):
        return f"ID: {self.id}, Description: {self.description}"
    
class Screen:
    def __init__(self, id, location, quantity, design, customer, description):
        self.id = id
        self.location = location
        self.quantity = quantity
        self.design = design
        self.customer = customer
        self.description = description

    def __str__(self):
        return f"ID: {self.id}, Design: {self.design}, Location: {self.location.id}"

class Controller:
    locations = []
    screens = []
    connection_string = r"C:\Users\cugos\OneDrive\Documents\GitHub\OC-Screen-Manager\Database\Screen_Database.db"
    locations_read = False

    @classmethod
    def read_locations(cls):
        cls.locations.clear()

        with sqlite3.connect(cls.connection_string) as connection:
            cursor = connection.cursor()

            query = "SELECT LocationID, Description FROM Locations"
            cursor.execute(query)

            # Fetch all rows from the query result
            rows = cursor.fetchall()

            for row in rows:
                id = row[0]
                description = row[1]

                location = Location(id, description)
                cls.locations.append(location)
            cls.locations_read = True

    @classmethod
    def print_locations(cls):
        for loc in cls.locations:
            print(loc)

    @classmethod
    def read_screens(cls):
        cls.screens.clear()

        with sqlite3.connect(cls.connection_string) as connection:
            cursor = connection.cursor()

            query = "SELECT ScreenID, LocationID, Quantity, Design, CustomerName, Description FROM Screens"
            cursor.execute(query)

            rows = cursor.fetchall()

            for row in rows:
                id = row[0]
                location = cls.get_location(row[1])
                quantity = row[2]
                design = row[3]
                customer = row[4]
                description = row[5]
                screen = Screen(id, location, quantity, design, customer, description)
                cls.screens.append(screen)

    @classmethod
    def get_location(cls, id):
        for location in cls.locations:
            if location.id == id:
                return location

    @classmethod
    def print_screens(cls):
        for screen in cls.screens:
            print(screen)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Manager")
        
        # Create a frame for displaying screen information
        self.info_frame = tk.Frame(root, padx=10, pady=10)
        self.info_frame.pack()

        # Create a label for each attribute of the screen
        self.label_id = tk.Label(self.info_frame, text="Screen ID: ")
        self.label_id.grid(row=0, column=0, sticky="w")

        self.label_design = tk.Label(self.info_frame, text="Design: ")
        self.label_design.grid(row=1, column=0, sticky="w")

        self.label_location = tk.Label(self.info_frame, text="Location: ")
        self.label_location.grid(row=2, column=0, sticky="w")

        self.label_customer = tk.Label(self.info_frame, text="Customer: ")
        self.label_customer.grid(row=3, column=0, sticky="w")

        self.label_quantity = tk.Label(self.info_frame, text="Quantity: ")
        self.label_quantity.grid(row=4, column=0, sticky="w")

        self.label_description = tk.Label(self.info_frame, text="Description: ")
        self.label_description.grid(row=5, column=0, sticky="w")

        # Create a frame for the buttons (e.g., search, add, edit)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.search_button = tk.Button(self.button_frame, text="Search", command=self.search)
        self.search_button.pack(side="left", padx=5)

        self.add_button = tk.Button(self.button_frame, text="Add Screen", command=self.add_screen)
        self.add_button.pack(side="left", padx=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Screen", command=self.edit_screen)
        self.edit_button.pack(side="left", padx=5)

    def search(self):
        # Implement search logic here
        pass

    def add_screen(self):
        # Implement add screen logic here
        pass

    def edit_screen(self):
        # Implement edit screen logic here
        pass

class Main:
    @staticmethod
    def main():
        Controller.read_locations()
        Controller.print_locations()    
        Controller.read_screens()
        Controller.print_screens()
        root = tk.Tk()
        app = App(root)
        root.mainloop()

    
if __name__ == "__main__":
    Main.main()