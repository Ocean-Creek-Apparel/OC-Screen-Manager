using System.Configuration;
using System.Diagnostics;
using Screen_Manager_Forms_Application.Models;
using Screen_Manager_Forms_Application.Views;

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
            ApplicationConfiguration.Initialize();
            Application.Run(new MainForm());
            LocationController.LoadAllLocationsFromDatabase();
            LocationController.Debug_CheckLocationsLoaded();
            ScreenController.LoadAllScreensFromDatabase();
            ScreenController.Debug_CheckScreensLoaded();
        }
    }
}