class Location:
    """
    Represents a location within the storage area.
    
    Attributes:
        id (int): the id of the location in the database
        description (str): the name or identifier of the location
    """

    def __init__(self, id, description):
        self.id = id
        self.description = description