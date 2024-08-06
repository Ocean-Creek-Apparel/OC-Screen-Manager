using System.Configuration;
using System.Diagnostics;
using Screen_Manager_Forms_Application.Models;

namespace Screen_Manager_Forms_Application.Controllers
{
    internal static class MainController
    {
        public static string ConnectionString = ConfigurationManager.ConnectionStrings["DatabaseConnection"].ConnectionString;

        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            // ApplicationConfiguration.Initialize();
            // Application.Run(new Form1());

            LocationController lc = new LocationController();
            LocationController.Debug_CheckLocationsLoaded();
            LocationController.RemoveLocationFromDatabase(7);
            LocationController.Debug_CheckLocationsLoaded();
        }
    }
}