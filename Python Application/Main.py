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
    def __init__(self, id, location, quantity, design, customer, description, in_use):
        self.id = id
        self.location = location
        self.quantity = quantity
        self.design = design
        self.customer = customer
        self.description = description
        self.in_use = in_use

    def __str__(self):
        return f"ID: {self.id}, Design: {self.design}, Location: {self.location.id}"

class Controller:
    main_window_geometry = "800x900"
    locations = []
    screens = []
    connection_string = r"C:\Users\cugos\OneDrive\Documents\GitHub\OC-Screen-Manager\Database\Screen_Database.db"
    locations_read = False
    highlight_color = "#76a5e3"
    default_bg_color = "#c7e4f0"
    danger_color = "#e0654c"
    button_bg_color = "#7dc8e8"
    combo_box_font = "Segoe_UI_Symbol 18"

    @classmethod
    def update_screen(cls, screen):
        return True

    @classmethod
    def flip_screen_in_use(cls, screen):
        pass

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

                query = "SELECT ScreenID, LocationID, Quantity, Design, CustomerName, Description, InUse FROM Screens"
                cursor.execute(query)

                rows = cursor.fetchall()

                for row in rows:
                    id = row[0]
                    location = cls.get_location(row[1])
                    quantity = row[2]
                    design = row[3]
                    customer = row[4]
                    description = row[5]
                    in_use = False if (int(row[6]) == 0) else True
                    screen = Screen(id, location, quantity, design, customer, description, in_use)
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

    @classmethod
    def screens_using_location(cls, location_id):
        screens = []
        for screen in cls.screens:
            if screen.location.id == location_id:
                screens.append(screen)
        return screens

class App:  
    def __init__(self, root):
        self.clicked_location = False
        self.root = root
        self.root.title("Ocean Creek Screen Manager")
        self.root.configure(bg=Controller.default_bg_color)

        # Create a frame for the buttons (e.g., search, add)
        self.button_frame = tk.Frame(root, bg=Controller.default_bg_color)
        self.button_frame.pack(pady=10)

        self.search_button = tk.Button(self.button_frame, text="Search", command=self.search, bg=Controller.button_bg_color)
        self.search_button.pack(side="left", padx=5, pady=5)

        self.add_button = tk.Button(self.button_frame, text="Add Screen", command=self.add_screen_clicked, bg=Controller.button_bg_color)
        self.add_button.pack(side="left", padx=5, pady=5)

        self.location_button = tk.Button(self.button_frame, text="Add/Edit Locations", command=self.location_button_clicked, bg=Controller.button_bg_color)
        self.location_button.pack(side="left", padx=5, pady=5)

        self.search_entry = tk.Entry(root, width=45)
        self.search_entry.pack(side="top")
        self.search_entry.bind("<Return>", lambda event: self.search())

        self.scrollable_frame = ScrollableFrame(self, root, padx=5, pady=5, bg=Controller.default_bg_color)
        self.scrollable_frame.pack(fill="both", expand=True)
        self.scrollable_frame.display_screens(Controller.screens)

    def location_button_clicked(self):
        self.refresh("location_button_clicked")
        if not self.clicked_location:
            self.clicked_location = True
            self.scrollable_frame.display_locations(Controller.locations)
            self.location_button.config(text="Return to Screens")
            self.add_button.config(text="Add Location")
        else:
            self.clicked_location = False
            self.scrollable_frame.display_screens(Controller.screens)
            self.location_button.config(text="Add/Edit Locations")
            self.add_button.config(text="Add Screen")           

    def search(self):
        query = self.search_entry.get().lower()  # Get the search query and convert to lowercase
        results = []

        # Search through the screens
        if not self.clicked_location:
            for screen in Controller.screens:
                if (query in str(screen.id) or
                    query in screen.design.lower() or
                    query in str(screen.location.description).lower() or
                    query in screen.customer.lower() or
                    query in str(screen.quantity).lower() or
                    query in screen.description.lower()):
                    results.append(screen)

            self.scrollable_frame.display_screens(results)
        else:
            for location in Controller.locations:
                if (query in str(location.id) or
                    query in location.description.lower()):
                    results.append(location)

            self.scrollable_frame.display_locations(results)

    def add_screen_clicked(self):
        if not self.clicked_location:
            AddScreenDialog(self.root, self)
        else:
            AddLocationDialog(self.root, self)

    def refresh(self, reason="default"):
        if reason == "update_screen":
            messagebox.showinfo("Success!", "Changes saved! Screen updated.")
            Controller.read_screens()
            self.scrollable_frame.display_screens(Controller.screens)
        elif reason == "create_screen":
            messagebox.showinfo("Success!", "Changes saved! Screen created.")
            Controller.read_screens()
            self.scrollable_frame.display_screens(Controller.screens)
        elif reason == "delete_screen":
            messagebox.showinfo("Success!", "Changes saved! Screen deleted.")
            Controller.read_screens()
            self.scrollable_frame.display_screens(Controller.screens)
        elif reason == "location_button_clicked":
            Controller.read_locations()
            Controller.read_screens()
        elif reason == "update_location":
            Controller.read_locations()
            Controller.read_screens()
            self.scrollable_frame.display_locations(Controller.locations)
            messagebox.showinfo("Success!", "Changes saved! Location updated.")
        elif reason == "delete_location":
            Controller.read_locations()
            Controller.read_screens()
            self.scrollable_frame.display_locations(Controller.locations)
            messagebox.showinfo("Success", "Location succesfully deleted")
        elif reason == "create_location":
            Controller.read_locations()
            Controller.read_screens()
            messagebox.showinfo("Success!", "Changes saved! Location created.")
            self.scrollable_frame.display_locations(Controller.locations)

class ScreenDialog:
    def __init__(self, parent, screen, main_instance):
        self.screen = screen
        self.main_instance = main_instance
        self.top = tk.Toplevel(parent, bg=Controller.default_bg_color)
        self.top.title(f"{screen.customer} - {screen.design}")
        self.top.grab_set()
        self.top.resizable(False, False)

        tk.Label(self.top, text="Screen ID:", bg=Controller.default_bg_color).grid(row=0, column=0, padx=5, pady=5)
        self.id_label = tk.Label(self.top, text=f"{screen.id}", bg=Controller.default_bg_color).grid(row=0, column=1, padx=5, pady=5, sticky="W")

        tk.Label(self.top, text="Design:", bg=Controller.default_bg_color).grid(row=1, column=0, padx=5, pady=5)
        self.design_entry = tk.Entry(self.top, width="35")
        self.design_entry.insert(0, screen.design)
        self.design_entry.grid(row=1, column=1, padx=5, pady=5)

        
        tk.Label(self.top, text="Location", bg=Controller.default_bg_color).grid(row=2, column=0, padx=5, pady=5)

        self.location_combobox = ttk.Combobox(self.top, width=33, font=Controller.combo_box_font)
        self.locations = [location.description for location in Controller.locations]  # Get descriptions or IDs of locations
        self.location_combobox['values'] = self.locations
        self.location_combobox.set(screen.location.description)  # Set to the current location
        self.location_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        tk.Label(self.top, text="Customer:", bg=Controller.default_bg_color).grid(row=3, column=0, padx=5, pady=5)
        self.customer_entry = tk.Entry(self.top, width="35")
        self.customer_entry.insert(0, screen.customer)
        self.customer_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.top, text="Quantity:", bg=Controller.default_bg_color).grid(row=4, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(self.top, width="35")
        self.quantity_entry.insert(0, screen.quantity)
        self.quantity_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.top, text="Description:", bg=Controller.default_bg_color).grid(row=5, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.top, width="35")
        self.description_entry.insert(0, screen.description)
        self.description_entry.grid(row=5, column=1, padx=5, pady=5)

        self.checked = tk.BooleanVar()
        self.checked.set(self.screen.in_use)
        tk.Label(self.top, text="In Use:", bg=Controller.default_bg_color).grid(row=6, column=0, padx=5, pady=5)
        self.check_button = tk.Checkbutton(self.top, variable=self.checked, bg=Controller.default_bg_color).grid(row=6, column=1, padx=5, pady=5, sticky="w")

        button_frame = HorizontalFlowFrame(self.top, 3, bg=Controller.default_bg_color)
        button_frame.grid(row=7, column=0, columnspan=2)

        # Create save and cancel buttons
        self.save_button = tk.Button(button_frame, text="Save", command=lambda: self.save_screen(), bg=Controller.button_bg_color)
        self.save_button.pack(side="left", padx=5, pady=5)
        self.cancel_button = tk.Button(button_frame, text="Cancel", command=self.top.destroy, bg=Controller.button_bg_color)
        self.cancel_button.pack(side="left", padx=5, pady=5)
        self.delete_button = tk.Button(button_frame, text="Delete Screen", command=lambda: self.delete_screen(), bg=Controller.danger_color)
        self.delete_button.pack(side="left", padx=5, pady=5)

    def delete_screen(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to delete this screen?"):
            with sqlite3.connect(Controller.connection_string) as connection:
                cursor = connection.cursor()
                id = self.screen.id

                # Execute the delete statement
                cursor.execute("""
                DELETE FROM Screens
                WHERE ScreenID = ?
                """, (id,))
                connection.commit()       
            self.top.destroy()
            self.main_instance.refresh("delete_screen")

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
                in_use = 1 if self.checked.get() else 0

                cursor.execute("""
                UPDATE Screens
                SET Design = ?, LocationID = ?, CustomerName = ?, Quantity = ?, Description = ?, InUse = ?
                WHERE ScreenID = ?
                """, (design, location_id, customer, quantity, description, in_use, id))

                connection.commit()
            self.top.destroy()
            self.main_instance.refresh("update_screen")

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

class AddScreenDialog:
    def __init__(self, parent, main_instance):
        self.main_instance = main_instance
        self.top = tk.Toplevel(parent, bg=Controller.default_bg_color)
        self.top.title("Add Screen")
        self.top.grab_set()
        self.top.resizable(False, False)

        tk.Label(self.top, text="Design:", bg=Controller.default_bg_color).grid(row=1, column=0, padx=5, pady=5)
        self.design_entry = tk.Entry(self.top, width="35")
        self.design_entry.grid(row=1, column=1, padx=5, pady=5)

        
        tk.Label(self.top, text="Location", bg=Controller.default_bg_color).grid(row=2, column=0, padx=5, pady=5)

        self.location_combobox = ttk.Combobox(self.top, width=33, font=Controller.combo_box_font)
        self.locations = [location.description for location in Controller.locations]  # Get descriptions or IDs of locations
        self.location_combobox['values'] = self.locations
        self.location_combobox.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        tk.Label(self.top, text="Customer:", bg=Controller.default_bg_color).grid(row=3, column=0, padx=5, pady=5)
        self.customer_entry = tk.Entry(self.top, width="35")
        self.customer_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.top, text="Quantity:", bg=Controller.default_bg_color).grid(row=4, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(self.top, width="35")
        self.quantity_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.top, text="Description:", bg=Controller.default_bg_color).grid(row=5, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.top, width="35")
        self.description_entry.grid(row=5, column=1, padx=5, pady=5)

        button_frame = HorizontalFlowFrame(self.top, 3, bg=Controller.default_bg_color)
        button_frame.grid(row=6, column=0, columnspan=2)

        # Create save and cancel buttons
        self.save_button = tk.Button(button_frame, text="Save", command=lambda: self.create_screen(), bg=Controller.button_bg_color)
        self.save_button.pack(side="left", padx=5, pady=5)
        self.cancel_button = tk.Button(button_frame, text="Cancel", command=self.top.destroy, bg=Controller.button_bg_color)
        self.cancel_button.pack(side="left", padx=5, pady=5)

    def create_screen(self):
        if self.validate_screen():
            with sqlite3.connect(Controller.connection_string) as connection:
                cursor = connection.cursor()

                # Extract data from the entries
                design = self.design_entry.get().strip()
                location_id = Controller.find_location_id_by_desc(self.location_combobox.get())  # Assuming it returns the location's ID
                customer = self.customer_entry.get().strip()
                quantity = int(self.quantity_entry.get().strip())
                description = self.description_entry.get().strip()

                # Insert the new screen into the database
                cursor.execute("""
                INSERT INTO Screens (Design, LocationID, CustomerName, Quantity, Description)
                VALUES (?, ?, ?, ?, ?)
                """, (design, location_id, customer, quantity, description))

                connection.commit()
            self.main_instance.refresh("create_screen")
            self.design_entry.delete(0, tk.END)
            self.customer_entry.delete(0, tk.END)
            self.quantity_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)

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
        elif not self.location_combobox.get():
            messagebox.showwarning("Input Error", "Location field cannot be empty. If the location you're looking for isn't displayed,\nyou can add it from the locations menu.")
        elif Controller.find_location_id_by_desc(location_desc) == -1:
            messagebox.showwarning("Input Error", "Location not found!")
        else:
            return True

class AddLocationDialog:
    def __init__(self, parent, main_instance):
        self.main_instance = main_instance
        self.parent = parent
        self.top = tk.Toplevel(parent, bg=Controller.default_bg_color)
        self.top.title("Add Location")
        self.top.grab_set()
        self.top.resizable(False, False)

        tk.Label(self.top, text="Name/Description:", bg=Controller.default_bg_color).grid(row=0, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.top, width="45")
        self.description_entry.grid(row=0, column=1, padx=5, pady=5)

        button_frame = HorizontalFlowFrame(self.top, 3, bg=Controller.default_bg_color)
        button_frame.grid(row=1, column=0, columnspan=2)

        self.save_button = tk.Button(button_frame, text="Save", command=lambda: self.create_location(), bg=Controller.button_bg_color)
        self.save_button.pack(side="left", padx=5, pady=5)
        self.cancel_button = tk.Button(button_frame, text="Cancel", command=self.top.destroy, bg=Controller.button_bg_color)
        self.cancel_button.pack(side="left", padx=5, pady=5)

    def create_location(self):
        if self.validate_location():
            with sqlite3.connect(Controller.connection_string) as connection:
                cursor = connection.cursor()
                desc = str(self.description_entry.get())
                cursor.execute("""INSERT INTO Locations (Description) VALUES (?)""", (desc,))
                connection.commit()
            self.description_entry.delete(0, tk.END)
            self.main_instance.refresh("create_location")

    def validate_location(self):
        found = Controller.find_location_id_by_desc(self.description_entry.get())
        if found != -1:
            messagebox.showerror("Input Error", r"Another location already exists with that name/description.")
        else:
            return True

class LocationDialog:
    def __init__(self, root, location, main_instance):
        self.location = location
        self.root = root
        self.main_instance = main_instance
        self.top = tk.Toplevel(root, bg=Controller.default_bg_color)
        self.top.title(f"{location.description}")
        self.top.grab_set()
        self.top.resizable(False, False)

        tk.Label(self.top, text="Location ID:", bg=Controller.default_bg_color).grid(row=0, column=0, padx=5, pady=5)
        self.id_label = tk.Label(self.top, text=f"{location.id}", bg=Controller.default_bg_color).grid(row=0, column=1, padx=5, pady=5, sticky="W")

        tk.Label(self.top, text="Name/Description: ", bg=Controller.default_bg_color).grid(row=1, column=0,padx=5,pady=5)
        self.description_entry = tk.Entry(self.top, width=35)
        self.description_entry.insert(0, location.description)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.top, text="Screens located here: ", bg=Controller.default_bg_color).grid(row=2, column=0, padx=5, pady=5)

        screens_using = [screen.design for screen in Controller.screens_using_location(self.location.id)]

        if(screens_using):
            self.selected_option = tk.StringVar(root)
            self.selected_option.set(screens_using[0])
            self.screen_dropdown = tk.OptionMenu(self.top, self.selected_option, *screens_using)
            self.screen_dropdown.config(width="33")
            self.screen_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky="W")
        else:
            self.none_using = tk.Label(self.top, bg=Controller.default_bg_color, text="None")
            self.none_using.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        button_frame = HorizontalFlowFrame(self.top, 3, bg=Controller.default_bg_color)
        button_frame.grid(row=3, column=0, columnspan=2)

        self.save_button = tk.Button(button_frame, text="Save", command=lambda: self.save_location(), bg=Controller.button_bg_color)
        self.save_button.pack(side="left", padx=5, pady=5)
        self.cancel_button = tk.Button(button_frame, text="Cancel", command=self.top.destroy, bg=Controller.button_bg_color)
        self.cancel_button.pack(side="left", padx=5, pady=5)
        self.delete_button = tk.Button(button_frame, text="Delete Location", command=lambda: self.delete_location(), bg=Controller.danger_color)
        self.delete_button.pack(side="left", padx=5, pady=5)

    def save_location(self):
        if(self.validate_location("update")):
            with sqlite3.connect(Controller.connection_string) as connection:
                cursor = connection.cursor()

                # Extract data from the entries
                id = self.location.id
                desc = self.description_entry.get()

                cursor.execute("""
                UPDATE Locations
                SET Description = ?
                WHERE LocationID = ?
                """, (desc, id))

                connection.commit()
            self.top.destroy()
            self.main_instance.refresh("update_location")

    def delete_location(self):
        if(self.validate_location("delete")):
            with sqlite3.connect(Controller.connection_string) as connection:
                cursor = connection.cursor()
                cursor.execute("""DELETE FROM Locations WHERE LocationID = ?""", (self.location.id,))
                connection.commit()
            self.top.destroy()
            self.main_instance.refresh("delete_location")

    def validate_location(self, operation):
        if(operation.lower() == "create"):
            found = Controller.find_location_id_by_desc(self.description_entry.get())
            if found != -1:
                messagebox.showerror("Input Error", r"Another location already exists with that name/description.")
            else:
                return True
        if(operation.lower() == "update"):
            found = Controller.find_location_id_by_desc(self.description_entry.get())
            if found != self.location.id and found != -1:
                messagebox.showerror("Input Error", "Another location already exists with that name/description.")
            else:
                return True
        elif(operation.lower() == "delete"):
            if Controller.screens_using_location(self.location.id):
                messagebox.showerror("Error!", "Screens are in this location, re-assign or delete screens.")
            else:
                if messagebox.askyesno("Confirmation", "Are you sure you want to delete this location?"):
                    return True                           

class HorizontalFlowFrame(tk.Frame):
    def __init__(self, parent, max_columns=3, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.max_columns = max_columns
        self.current_row = 0
        self.current_column = 0

    def add_widget(self, widget, screen=None):
        widget.grid(row=self.current_row, column=self.current_column, padx=5, pady=5)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", lambda event: self.on_leave(event, screen))
        self.current_column += 1
        if self.current_column >= self.max_columns:
            self.current_column = 0
            self.current_row += 1
 
    def on_leave(self, event, screen=None):
        if screen:
            color = Controller.default_bg_color if not screen.in_use else Controller.danger_color
        else:
            color = Controller.default_bg_color
        self.config(bg=color)
        widgets = self.winfo_children()
        for w in widgets:
            w.config(bg=color)

    def on_enter(self, event):
        self.config(bg=Controller.highlight_color)
        widgets = self.winfo_children()
        for w in widgets:
            w.config(bg=Controller.highlight_color)
        #event.widget.config(bg=Controller.highlight_color)

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.bg = Controller.default_bg_color
        self.parent = parent
        self.root = root
        self.canvas = tk.Canvas(self, borderwidth=0, bg=Controller.default_bg_color)
        self.frame = tk.Frame(self.canvas, bg=Controller.default_bg_color)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind_all("<Button-4>", self.on_mouse_wheel)  # For Linux
        self.canvas.bind_all("<Button-5>", self.on_mouse_wheel)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        self.canvas.itemconfig("self.frame", width=canvas_width)

    def on_mouse_wheel(self, event):
        if event.delta: 
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else: 
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")

    def display_basic_screen_info(self, text_to_display):
        self.clear_frame()
        if not text_to_display:
            no_text = tk.Label(self.frame, text="None", bg=Controller.default_bg_color)
            no_text.pack()
        for text in text_to_display:
            text_label = tk.Label(self.frame, text=f"{text}", bg=Controller.default_bg_color)
            text_label.pack()

    def display_screens(self, screen_list):
        self.clear_frame()
        if not screen_list:
            no_result = tk.Label(self.frame, text="No results found!", bg=Controller.default_bg_color)
            no_result.pack()
        for s in screen_list:
            display_frame = self.create_screen_display(s, self.frame)
            display_frame.pack()

    def display_locations(self, location_list):
        self.clear_frame()
        if not location_list:
            no_result = tk.Label(self.frame, text="No results found!", bg=Controller.default_bg_color)
            no_result.pack()
        for l in location_list:
            display_frame = self.create_location_display(l, self.frame)
            display_frame.pack()

    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def create_screen_display(self, screen, parent):
        color = Controller.default_bg_color if not (screen.in_use == 1) else Controller.danger_color
        frame = HorizontalFlowFrame(parent, max_columns=6, padx=10, pady=10, bg=color)
        label_main = tk.Label(frame, text=f"{screen.customer} - {screen.design}", bg=color)

        label_main.bind("<Button-1>", lambda event: self.screen_label_clicked(screen))
        label_main.bind("<Button-3>", lambda event: self.screen_label_right_clicked(screen, label_main, frame))

        frame.bind("<Button-1>", lambda event: self.screen_label_clicked(screen))
        frame.bind("<Button-3>", lambda event: self.screen_label_right_clicked(screen, label_main, frame))

        frame.add_widget(label_main, screen)
        return frame
    
    def create_location_display(self, location, parent):
        frame = HorizontalFlowFrame(parent, max_columns=6, padx=10, pady=10, bg=Controller.default_bg_color)
        frame.bind("<Button-1>", lambda event: self.location_label_clicked(location))

        label_main = tk.Label(frame, text=f"{location.description}", bg=Controller.default_bg_color)
        label_main.bind("<Button-1>", lambda event: self.location_label_clicked(location))

        frame.add_widget(label_main)
        return frame

    def screen_label_right_clicked(self, screen, label, frame):
        if screen.in_use:
            label.config(bg=Controller.default_bg_color)
            frame.config(bg=Controller.default_bg_color)
        else:
            label.config(bg=Controller.danger_color)
            label.config(bg=Controller.danger_color)

    def screen_label_clicked(self, screen):
        ScreenDialog(self.parent.root, screen, self.parent)

    def location_label_clicked(self, location):
        LocationDialog(self.parent.root, location, self.parent)

class Main:
    @staticmethod
    def main():
        Controller.read_locations() 
        Controller.read_screens()
        root = tk.Tk()
        root.geometry(Controller.main_window_geometry)
        root.resizable(False, False)
        Main.set_fonts(root)
        app = App(root)
        root.mainloop()

    def set_fonts(root):
        root.option_add("*TCombobox*Listbox*Font", "Segoe_UI_Symbol 18")
        root.option_add("*Entry*Font", "Segoe_UI_Symbol 18")
        root.option_add("*Label.Font", "Segoe_UI_Symbol 16")
        root.option_add("*Button.Font", "Segoe_UI_Symbol 18")
    
if __name__ == "__main__":
    Main.main()