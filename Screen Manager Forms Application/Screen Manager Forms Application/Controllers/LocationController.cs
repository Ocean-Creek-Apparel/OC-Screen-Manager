using System;
using Microsoft.Data.Sqlite;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Screen_Manager_Forms_Application.Models;
using System.Configuration;
using System.Diagnostics;
using System.Windows.Forms;
using System.ComponentModel.DataAnnotations;

namespace Screen_Manager_Forms_Application.Controllers
{
    internal static class LocationController
    {
        private static List<Location> Locations = new();
        public static List<Location> LoadAllLocationsFromDatabase()
        {
            Locations.Clear();

            string connectionString = MainController.ConnectionString;

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
                        Locations.Add(location);
                    }
                }
            }

            return Locations;
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
        
        public static Location AddLocationToDatabase(string desc)
        {
            string connectionString = MainController.ConnectionString;
            int newID;

            using (var connection = new SqliteConnection(connectionString))
            {
                connection.Open();
                string query = "INSERT INTO Locations (Description) VALUES (@Description)";

                using (var command = new SqliteCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@Description", desc);
                    command.ExecuteNonQuery();
                }

                // Retrieve the ID of the newly inserted location
                string selectQuery = "SELECT last_insert_rowid()";
                using (var selectCommand = new SqliteCommand(selectQuery, connection))
                {
                    newID = Convert.ToInt32(selectCommand.ExecuteScalar());
                }
            }
            
            LoadAllLocationsFromDatabase();
            return GetLocation(newID);
        }

        public static bool IsLocationInUse(int id)
        {
            return ScreenController.IsLocationInUse(id);
        }

        public static bool RemoveLocationFromDatabase(int id)
        {
            string connectionString = MainController.ConnectionString;

            using(var connection = new SqliteConnection(connectionString))
            {
                connection.Open();
                string query = "DELETE FROM Locations WHERE LocationID = @LocationID";

                using(var command = new SqliteCommand(query, connection))
                {
                    command.Parameters.AddWithValue("@LocationID", id);
                    int rows_affected = command.ExecuteNonQuery();

                    if(rows_affected == 0)
                    {
                        return false;
                    }
                }
            }

            LoadAllLocationsFromDatabase();
            return true;
        }
        public static bool LocationsIsNotNull()
        {
            return (Locations.Any()) ? true : false;
        }
        public static void Debug_CheckLocationsLoaded()
        {
            foreach(Location l in Locations)
            {
                Debug.WriteLine(l);
            }
        }
    }
}
