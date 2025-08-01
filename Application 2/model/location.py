import sqlite3

class Location:
    """
    Represents a location within the storage area.
    
    Attributes:       
        description (str): the name or identifier of the location
        location_id (int): the id in the db, default to -1 DO NOT CHANGE IF NOT READING FROM DB
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
            cursor.execute("""SELECT LocationID, Description FROM Location""")
            rows = cursor.fetchall()

            for row in rows:
                location_id = rows[0]
                description = rows[1]
                location = cls(description, location_id)
                locations.append(location)

        return locations
    
    @classmethod
    def delete_from_db(cls, conn: sqlite3.Connection):
        pass