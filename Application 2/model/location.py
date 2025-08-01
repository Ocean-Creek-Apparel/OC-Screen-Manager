import sqlite3

class Location:
    """
    Represents a location within the storage area.
    
    Attributes:       
        description (str): the name or identifier of the location
        location_id (int): the id in the db, default to -1 (new location)
    """

    """
    Constructor, do not pass id argument if not reading from db!
    
    Arguments:
        description (str): the description/identifer of the location
        location_id (int): the id in the db, defaults to -1, do not pass ID from views.
    """
    def __init__(self, description: str, location_id: int=-1):
        self.location_id = location_id
        self.description = description

    @classmethod
    def read_all(cls, conn: sqlite3.Connection) -> list["Location"]:
        """
        Reads all locations from the database.
        Intended to be called by the controller
        
        Arguments:
            conn (sqlite3.Connection): the db connection to use
        
        Returns:
            locations (list["Location"]): the locations read
        """
        with(conn):
            cursor = conn.cursor()

            locations = []
            cursor.execute("""SELECT LocationID, Description FROM Locations""")
            rows = cursor.fetchall()

            for row in rows:
                location_id = rows[0]
                description = rows[1]
                location = cls(description, location_id)
                locations.append(location)

        return locations
    
    def delete_from_db(self, conn: sqlite3.Connection):
        """
        Deletes the screen from the database.
        
        Arguments:
            conn (sqlite3.Connection): connection to database
        """
        with(conn):
            cursor = conn.cursor()
            cursor.execute("""
            DELETE FROM Locations
            WHERE LocationID = ?""", 
            (self.location_id,))

    def add_to_db(self, conn: sqlite3.Connection):
        """
        Adds a location to the db (location.id == -1), updates otherwise.
        
        Arguments:
            conn (sqlite3.Connection): connection to database
        """
        with(conn):
            cursor = conn.cursor()
            if self.location_id == -1:
                cursor.execute("""
                INSERT INTO Locations (Description)
                VALUES (?)
                """, (self.description,))
            else:
                cursor.execute("""
                UPDATE Locations
                SET Description = ?
                WHERE LocationID = ?""", 
                (self.description, self.location_id,))