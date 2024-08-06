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
        - public Location ScreenLocation         (SQL -> Location.LocationID)
            Location identifier
        - publicint Quantity {get; set;}
            Number of screens for the design
        - public string Design {get; set;}
            Design information
        - public string CustomerName {get; set;}
            Name of customer
        - public string Description {get; set;}
            Additional information
    methods
        - public Screen(int id, int locationID, int quantity, string design, string custName, string desc)
            constructor

LOCATION - represents a location in the warehouse
    attributes
        - private int ID {get;}                  (SQL -> LocationID)
            Unique identifier
        - public string Description {get; set;}
            Additional information regarding where the location actually is
    methods
        - public Location(int id, string desc)
            Constructor
        - public override ToString()
            returns $"{ID} - {Description}"

MAINCONTROLLER - main controller class
    attributes
        - public static String ConnectionString = ConfigurationManager.ConnectionStrings["DatabaseConnection"].ConnectionString;
            Connection string for SQL database
    methods
        - static void Main()
            Entry point for application
LOCATIONCONTROLLER - controls all the location models and views
    attributes
        - private static List<Location> Locations {get;} = new()
            A list of all the Location objects from the database
    methods
        - public LocationController()
            Constructor, assigns Locations = LoadAllLocationsFromDatabase()
        - private static List<Location> LoadAllLocationsFromDatabase()
            Loads all the locations from the database and returns the list (empty if no objects found)
        - public static void Debug_CheckLocationsLoaded
            Prints all locations to debug console
        - public static Location GetLocation(int id)
            Returns location from locationlist using id
        - public static Location AddLocationToDatabase(string desc)
            Adds a location to the database and returns the location object that was added
            Refreshes the Locations list with LoadAllLocationsFromDatabase()
        - public static bool RemoveLocationFromDatabase(int id)
            Removes location from the database and returns true if removed successfully, false if not
            Refreshes Locations list

SCREENCONTROLLER
    attributes
        - private List<Screen> Screens{get;} = new()
    methods
        - public ScreenController()
            Constructor, assigns Screens = LoadAllScreensFromDatabase()
        - private List<Screen> LoadAllScreensFromDatabase()
            Loads all the screens from the database and returns the list (empty if no objects found)
        - public void Debug_CheckLocationsLoaded
            Prints all screens to debug console

*** ADDITIONAL INFORMATION ***
- Microsoft.Data.Sqlite is used to communicate with SQL Database
- The SQL connection string is in app.config
