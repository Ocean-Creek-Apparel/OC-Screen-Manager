class Screen:
    """
    Represents a screenprinting screen.
    
    Attributes:
        id (int): the id as defined in the database
        location_id (int): the id of the associated location in the database
        quantity (int): the number of screens associated with this design
        design (str): the name of the design on the screen
        customer (str): the owner of the design
        description (str): other data relevant to the screen
        in_use (bool): is the screen in use
    """

    def __init__(self, id, location_id, quantity,
                 design, customer, description, in_use):
        self.id = id
        self.location_id = location_id
        self.quantity = quantity
        self.design = design
        self.customer = customer
        self.description = description
        self.in_use = in_use