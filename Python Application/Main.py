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
    def create_first_screen_display(self, screen, parent):
        # Create a frame for this screen's information
        frame = HorizontalFlowFrame(parent, max_columns=6, padx=10, pady=10)
        frame.bind("<Enter>", HorizontalFlowFrame.on_enter)
        frame.bind("<Leave>", HorizontalFlowFrame.on_leave)

        # Create labels for each attribute
        f_string = self.format_first_screen(screen)
        label_main = tk.Label(frame, text=f_string)
        frame.add_widget(label_main)

        # Return the frame for later placement in the main window
        return frame
    
    def create_other_screen_display(self, screen, parent):
        # Create a frame for this screen's information
        frame = HorizontalFlowFrame(parent, max_columns=6, padx=10, pady=10)
        frame.bind("<Enter>", HorizontalFlowFrame.on_enter)
        frame.bind("<Leave>", HorizontalFlowFrame.on_leave)

        # Create labels for each attribute
        label_main = tk.Label(frame, text=f"{screen.customer} - {screen.design}")
        frame.add_widget(label_main)

        # Return the frame for later placement in the main window
        return frame
    
    def format_first_screen(self, screen):
        formatted_string = (
            f"ID: {screen.id:<5} "
            f"Design: {screen.design:<15} "
            f"Location: {screen.location.id:<5} "
            f"Customer: {screen.customer:<15} "
            f"Quantity: {screen.quantity:<5} "
            f"Description: {screen.description:<20}"
        )
        return formatted_string

    def format_other_screen(self, screen):
        formatted_string = (
            f"{screen.id:<33} "
            f"{screen.design:<23} "
            f"{screen.location.id:<14} "
            f"{screen.customer:<29} "
            f"{screen.quantity:<15} "
            f"{screen.description:<33}"
        )
        return formatted_string

    def add_all_screens(self):   
        for screen in Controller.screens:
            display_frame = self.create_other_screen_display(screen, self.info_frame)
            display_frame.pack()
            
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Manager")

        # Create a frame for the buttons (e.g., search, add, edit)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Screen", command=self.add_screen)
        self.add_button.pack(side="left", padx=5)

        self.search_button = tk.Button(self.button_frame, text="Search", command=self.search)
        self.search_button.pack(side="left", padx=5)

        self.search_entry = tk.Entry(self.button_frame, width=60)
        self.search_entry.pack(side="left")
        self.search_entry.bind("<Return>", lambda event: self.search())

        # Create a frame for displaying screen information
        self.info_frame = tk.Frame(root, padx=10, pady=10)
        self.info_frame.pack()

        self.add_all_screens()

    def search(self):
        # Implement search logic here
        pass

    def add_screen(self):
        # Implement add screen logic here
        pass

    def edit_screen(self):
        # Implement edit screen logic here
        pass


class HorizontalFlowFrame(tk.Frame):
    def __init__(self, parent, max_columns=3, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.max_columns = max_columns
        self.current_row = 0
        self.current_column = 0

    def add_widget(self, widget):
        widget.grid(row=self.current_row, column=self.current_column, padx=5, pady=5)

        # Update row and column positions for the next widget
        self.current_column += 1
        if self.current_column >= self.max_columns:
            self.current_column = 0
            self.current_row += 1
    
    def on_enter(event):
        event.widget.config(bg="blue")

    def on_leave(event):
        event.widget.config(bg="white")

class Main:
    @staticmethod
    def main():
        Controller.read_locations()
        Controller.print_locations()    
        Controller.read_screens()
        Controller.print_screens()
        root = tk.Tk()
        Main.set_fonts(root)
        app = App(root)
        root.mainloop()

    def set_fonts(root):
        root.option_add("*Entry*Font", "Segoe_UI_Symbol 18")
        root.option_add("*Label.Font", "Segoe_UI_Light 14")
        root.option_add("*Button.Font", "Segoe_UI_Symbol 18")


    
if __name__ == "__main__":
    Main.main()