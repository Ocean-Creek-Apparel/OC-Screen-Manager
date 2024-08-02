Author:  Cullen Gostel
Version: 08/02/24

This software is designed for Ocean Creek Apparel. It is intended to allow employees to easily
locate screens within the warehouse.

*** FOLDERS ***
- Documentation, includes diagrams and other additional documentation
- Screen Manager Forms Application, Visual Studio solution folder
- Database, SQL database folder

*** OBJECTS/RECORDS ***
SCREEN - represents a printing screen in the warehouse
    attributes
        - private int ID {get;}                  (SQL -> ScreenID)
            Unique Identifier
        - private Location ScreenLocation        (SQL -> Location.LocationID)
            Location identifier
        - private int Quantity {get; set;}
            Number of screens for the design
        - private string Design {get; set;}
            Design information
        - private string CustomerName {get; set;}
            Name of customer
        - private string Description {get; set;}
            Additional information
    methods
        - public Screen(int id, int locationID, int quantity, string design, string custName, string desc)
            constructor

LOCATION - represents a location in the warehouse
    attributes
        - private int ID {get;}                  (SQL -> LocationID)
            Unique identifier
        - private string Description {get; set;}
            Additional information regarding where the location actually is
    methods
        - public Location(int id, string desc)
            Constructor

LOCATIONCONTROLLER - controls all the screen objects
    attributes
        - private List<Location> Locations {get;} = new()
            A list of all the Location objects from the database
    methods
        - public LocationController()
            Constructor, assigns Locations = LoadAllLocationsFromDatabase()S
        - private List<Location> LoadAllLocationsFromDatabase()
            Loads all the locations from the database and returns the list (empty if no objects found)

*** ADDITIONAL INFORMATION ***
- Microsoft.Data.Sqlite is used to communicate with SQL Database
- The SQL connection string is in app.config
