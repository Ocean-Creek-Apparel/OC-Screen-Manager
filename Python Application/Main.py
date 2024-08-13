import sqlite3

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

    @classmethod
    def load_locations(cls):
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

    @classmethod
    def print_locations(cls):
        for loc in cls.locations:
            print(loc)

    @classmethod
    def load_screens(cls):
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

class Main:
    @staticmethod
    def main():
        Controller.load_locations()
        Controller.print_locations()    
        Controller.load_screens()
        Controller.print_screens()
    
if __name__ == "__main__":
    Main.main()