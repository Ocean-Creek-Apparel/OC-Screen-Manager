import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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
    def update_screen(cls, screen):
        return True

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
    def find_location_id_by_desc(cls, desc):
        for location in cls.locations:
            if desc == location.description:
                return location.id
        return -1
    @classmethod
    def read_screens(cls):
        cls.screens.clear()
        if cls.locations_read:
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
    def screen_label_clicked(self, screen):
        ScreenDialog(self.root, screen, self)
    
    def create_screen_display(self, screen, parent):
        # Create a frame for this screen's information
        frame = HorizontalFlowFrame(parent, max_columns=6, padx=10, pady=10)
        frame.bind("<Enter>", HorizontalFlowFrame.on_enter)
        frame.bind("<Leave>", HorizontalFlowFrame.on_leave)
        frame.bind("<Button-1>", lambda event: self.screen_label_clicked(screen))

        # Create labels for each attribute
        label_main = tk.Label(frame, text=f"{screen.customer} - {screen.design}")
        label_main.bind("<Button-1>", lambda event: self.screen_label_clicked(screen))
        frame.add_widget(label_main)

        # Return the frame for later placement in the main window
        return frame

    def display_all_screens(self):   
        self.clear_frame(self.info_frame)
        for screen in Controller.screens:
            display_frame = self.create_screen_display(screen, self.info_frame)
            display_frame.pack()
    
    def display_screens(self, screens):
        self.clear_frame(self.info_frame)

        if not screens:
            self.label_no_results = tk.Label(self.info_frame, text="No results found!")
            self.label_no_results.pack()

        for screen in screens:
            display_frame = self.create_screen_display(screen, self.info_frame)
            display_frame.pack()

    def clear_frame(self, frame):
        # Destroy all widgets in the frame
        for widget in frame.winfo_children():
            widget.destroy()

    def __init__(self, root):
        self.root = root
        self.root.title("Screen Manager")

        # Create a frame for the buttons (e.g., search, add)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.search_button = tk.Button(self.button_frame, text="Search", command=self.search)
        self.search_button.pack(side="left", padx=5)

        self.add_button = tk.Button(self.button_frame, text="Add Screen", command=self.add_screen_clicked)
        self.add_button.pack(side="left", padx=5)

        self.search_entry = tk.Entry(root, width=45)
        self.search_entry.pack(side="top")
        self.search_entry.bind("<Return>", lambda event: self.search())

        # Create a frame for displaying screen information
        self.info_frame = tk.Frame(root, padx=10, pady=10)
        self.info_frame.pack()

        self.display_all_screens()

    def search(self):
        query = self.search_entry.get().lower()  # Get the search query and convert to lowercase
        results = []

        # Search through the screens
        for screen in Controller.screens:
            if (query in str(screen.id).lower() or
                query in screen.design.lower() or
                query in str(screen.location.id).lower() or
                query in screen.customer.lower() or
                query in str(screen.quantity).lower() or
                query in screen.description.lower()):
                results.append(screen)

        # Display search results
        self.display_screens(results)

    def add_screen_clicked(self):
        # Implement add screen logic here
        pass

    def refresh(self, reason, data):
        if reason == "update_screen":
            messagebox.showinfo("Success!", f"Changes to {data} saved!" )
            Controller.read_screens()
            self.display_all_screens()

class ScreenDialog:
    def __init__(self, parent, screen, main_instance):
        self.screen = screen
        self.main_instance = main_instance
        self.top = tk.Toplevel(parent)
        self.top.title(f"{screen.customer} - {screen.design}")
        self.top.grab_set()

        tk.Label(self.top, text="Screen ID:").grid(row=0, column=0, padx=5, pady=5)
        self.id_label = tk.Label(self.top, text=f"{screen.id}").grid(row=0, column=1, padx=5, pady=5, sticky="W")

        tk.Label(self.top, text="Design:").grid(row=1, column=0, padx=5, pady=5)
        self.design_entry = tk.Entry(self.top, width="35")
        self.design_entry.insert(0, screen.design)
        self.design_entry.grid(row=1, column=1, padx=5, pady=5)

        
        tk.Label(self.top, text="Location").grid(row=2, column=0, padx=5, pady=5)

        self.location_combobox = ttk.Combobox(self.top, width=70)
        self.locations = [location.description for location in Controller.locations]  # Get descriptions or IDs of locations
        self.location_combobox['values'] = self.locations
        self.location_combobox.set(screen.location.description)  # Set to the current location
        self.location_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        tk.Label(self.top, text="Customer:").grid(row=3, column=0, padx=5, pady=5)
        self.customer_entry = tk.Entry(self.top, width="35")
        self.customer_entry.insert(0, screen.customer)
        self.customer_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.top, text="Quantity:").grid(row=4, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(self.top, width="35")
        self.quantity_entry.insert(0, screen.quantity)
        self.quantity_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.top, text="Description:").grid(row=5, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.top, width="35")
        self.description_entry.insert(0, screen.description)
        self.description_entry.grid(row=5, column=1, padx=5, pady=5)

        # Create save and cancel buttons
        self.save_button = tk.Button(self.top, text="Save", command=lambda: self.save_screen())
        self.save_button.grid(row=6, column=0, padx=5, pady=5)
        self.cancel_button = tk.Button(self.top, text="Cancel", command=self.top.destroy)
        self.cancel_button.grid(row=6, column=1, padx=5, pady=5)

    def save_screen(self):
        if self.validate_screen():
            with sqlite3.connect(Controller.connection_string) as connection:
                cursor = connection.cursor()

                # Extract data from the entries
                id = self.screen.id
                design = self.design_entry.get().strip()
                location_id = Controller.find_location_id_by_desc(self.location_combobox.get())  # Assuming it returns the location's ID
                customer = self.customer_entry.get().strip()
                quantity = int(self.quantity_entry.get().strip())
                description = self.description_entry.get().strip()

                cursor.execute("""
                UPDATE Screens
                SET Design = ?, LocationID = ?, CustomerName = ?, Quantity = ?, Description = ?
                WHERE ScreenID = ?
                """, (design, location_id, customer, quantity, description, id))

                connection.commit()
                self.top.destroy()
                self.main_instance.refresh("update_screen", design)

    def validate_screen(self):
        design = self.design_entry.get()
        customer = self.customer_entry.get()
        location_desc = self.location_combobox.get()
        quantity = self.quantity_entry.get()
        description = self.description_entry.get()

        if not design.strip():
            messagebox.showwarning("Input Error", "Design field cannot be empty!")
        elif len(design) > 150:
            messagebox.showwarning("Input Error", "Design field cannot exceed 150 characters.")
        elif not customer.strip():
            messagebox.showwarning("Input Error", "Customer field cannot be empty!")
        elif len(customer) > 150:
            messagebox.showwarning("Input Error", "Customer field cannot exceed 150 characters.")
        elif len(description) > 150:
            messagebox.showwarning("Input Error", "Description field cannot exceed 150 characters.")
        elif not quantity.isdigit() or int(quantity) < 0:
            messagebox.showwarning("Input Error", "Quantity must be a non-negative integer!")
        elif Controller.find_location_id_by_desc(location_desc) == -1:
            messagebox.showwarning("Input Error", "Location not found!")
        else:
            return True
        
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
        root.option_add("*Combobox*Font", "Segoe_UI_Symbol 18")
        root.option_add("*TCombobox*Listbox*Font", "Segoe_UI_Symbol 18")
        root.option_add("*Entry*Font", "Segoe_UI_Symbol 18")
        root.option_add("*Label.Font", "Segoe_UI_Light 16")
        root.option_add("*Button.Font", "Segoe_UI_Symbol 18")
    
if __name__ == "__main__":
    Main.main()