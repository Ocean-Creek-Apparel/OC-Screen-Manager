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
        location_id (int): the id in the db, defaults to -1, do not pass ID from views."""
    def __init__(self, description: str, location_id: int=-1):
        self.location_id = location_id
        self.description = description