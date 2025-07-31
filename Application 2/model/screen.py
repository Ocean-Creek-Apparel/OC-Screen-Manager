import sqlite3

class Screen:
    """
    Represents a screenprinting screen.
    This class handles the CRUD operations for screens with methods read_all(),
    delete_screen(), and add_screen()
    
    Attributes:
        screen_id (int): the id as defined in the database, DO NOT ASSIGN UNLESS READING FROM DATABASE
        location_id (int): the id of the associated location in the database
        quantity (int): the number of screens associated with this design
        design (str): the name of the design on the screen
        customer (str): the owner of the design
        description (str): other data relevant to the screen
        in_use (bool): is the screen in use
    """
    def __init__(self, location_id: int, quantity: int, design: str, 
                 customer: str, description: str, in_use: bool, screen_id: int = -1):
        self.screen_id = screen_id
        self.location_id = location_id
        self.quantity = quantity
        self.design = design
        self.customer = customer
        self.description = description
        self.in_use = in_use

    @classmethod
    def read_all(cls, conn: sqlite3.Connection) -> list["Screen"]:
        """
        Reads all screens from the database.
        Intended to be called by the controller
        
        Arguments:
            conn (sqlite3.Connection): connection to database
        
        Returns:
            screens (Screen[]): the screens read from the database.
        """
        with(conn):
            cursor = conn.cursor()
            query = """SELECT ScreenID, LocationID, Quantity, 
            Design, CustomerName, Description, InUse FROM Screens"""

            cursor.execute(query)
            rows = cursor.fetchall()

            screens = []
            for row in rows:
                screen_id = row[0]
                location_id = row[1]
                quantity = row[2]
                design = row[3]
                customer = row[4]
                description = row[5]
                in_use = bool(row[6])
                screen = cls(location_id, quantity, design, customer, description, in_use, screen_id)
                screens.append(screen)
            return screens
        
    def delete_from_db(self, conn: sqlite3.Connection) -> bool:
        """
        Deletes the screen from the database.
        
        Arguments:
            conn (sqlite3.Connection): connection to database
        
        Returns:
            deleted (bool): true if operation successful, false otherwise.
        """
        deleted = False
        with(conn):
            cursor = conn.cursor()
            cursor.execute("""
            DELETE FROM Screens
            WHERE ScreenID = ?
            """, (self.screen_id,))
            deleted = True   
        return deleted
    
    def add_to_db(self, conn: sqlite3.Connection) -> bool:
        """
        Adds a new screen to the database (if id==-1) or updates
        existing screen if id != -1.
        
        Arguments:
            conn (sqlite3.Connection): connection to database
            
        Returns:
            added (bool): True if operation completed, otherwise false.
        """
        added = False
        with(conn):
            cursor = conn.cursor()
            if (self.screen_id == -1):
                cursor.execute("""
                INSERT INTO Screens (Design, LocationID, CustomerName, 
                Quantity, Description, InUse)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (self.design, self.location_id, self.customer,
                    self.quantity, self.description, 1 if self.in_use else 0))
                self.screen_id = cursor.lastrowid
                added = True
            else:
                cursor.execute("""
                UPDATE Screens
                SET Design = ?, LocationID = ?, CustomerName = ?, Quantity = ?, 
                Description = ?, InUse = ?
                WHERE ScreenID = ?
                """, (self.design, self.location_id, self.customer, 
                      self.quantity, self.description, 1 if self.in_use else 0, 
                      self.screen_id))
                added = True
        return added
    
