using System;
using Microsoft.Data.Sqlite;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Screen_Manager_Forms_Application.Models;
using System.Configuration;
using System.Diagnostics;

namespace Screen_Manager_Forms_Application.Controllers
{
    internal class LocationController
    {
        private static List<Location> Locations = new();
        
        public LocationController()
        {
            Locations = LoadAllLocationsFromDatabase();
        }

        private List<Location> LoadAllLocationsFromDatabase()
        {
            List<Location> locations = new();

            string connectionString = ConfigurationManager.ConnectionStrings["DatabaseConnection"].ConnectionString;

            using (var connection = new SqliteConnection(connectionString))
            {
                connection.Open();

                string query = "SELECT LocationID, Description FROM Locations";

                using (var command = new SqliteCommand(query, connection))
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        int id = reader.GetInt32(0);
                        string description = reader.GetString(1);

                        Location location = new Location(id, description);
                        locations.Add(location);
                    }
                }
            }

            return locations;
        }

        public static Location GetLocation(int id)
        {
            foreach (Location l in Locations)
            {
                if(l.GetID() == id)
                {
                    return l;
                }
            }
            return null;
        }

        public bool LocationsIsNotNull()
        {
            return (Locations.Any()) ? true : false;
        }
        public void Debug_CheckLocationsLoaded()
        {
            foreach(Location l in Locations)
            {
                Debug.WriteLine(l);
            }
        }
    }
}
