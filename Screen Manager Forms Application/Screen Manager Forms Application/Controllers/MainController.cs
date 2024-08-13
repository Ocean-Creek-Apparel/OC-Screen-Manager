using System.Configuration;
using System.Diagnostics;
using System.Windows.Forms;
using Screen_Manager_Forms_Application.Models;
using Screen_Manager_Forms_Application.Views;

namespace Screen_Manager_Forms_Application.Controllers
{
    internal static class MainController
    {
        public static string ConnectionString = ConfigurationManager.ConnectionStrings["DatabaseConnection"].ConnectionString;
        public static string? IDSearch;
        public static string? DesignSearch;
        public static string? LocationSearch;
        public static string? CustomerSearch;
        public static string? DescriptionSearch;
        public static List<PrintScreen> SearchResults = [];
        public static MainForm form = new();
        [STAThread]
        static void Main()
        {
            ApplicationConfiguration.Initialize();
            LocationController.LoadAllLocationsFromDatabase();
            LocationController.Debug_CheckLocationsLoaded();
            ScreenController.LoadAllScreensFromDatabase();
            ScreenController.Debug_CheckScreensLoaded();
            Application.Run(form);
            AddAllScreensToPanel();
        }

        public static void AddAllScreensToPanel()
        {
            ClearScreenPanel();
            foreach(PrintScreen s in ScreenController.Screens)
            {
                Debug.WriteLine("Control added");
                form.ScreensPanel.Controls.Add(s.ViewControl);
            }
        }

        public static void Search()
        {
            GetSearchResults();
            AddSearchScreensToPanel();
        }
        public static void AddSearchScreensToPanel()
        {
            ClearScreenPanel();
            foreach(PrintScreen s in SearchResults)
            {
                form.ScreensPanel.Controls.Add(s.ViewControl);
            }
        }

        public static void ClearScreenPanel()
        {
            form.ScreensPanel.Controls.Clear();
        }

        public static void GetSearchResults()
        {
            SearchResults = ScreenController.Screens.Where(screen =>
        (string.IsNullOrEmpty(IDSearch) || screen.GetID().ToString().Contains(IDSearch)) &&
        (string.IsNullOrEmpty(DesignSearch) || screen.Design.Contains(DesignSearch, StringComparison.OrdinalIgnoreCase)) &&
        (string.IsNullOrEmpty(LocationSearch) || screen.ScreenLocation.Description.Contains(LocationSearch, StringComparison.OrdinalIgnoreCase)) &&
        (string.IsNullOrEmpty(CustomerSearch) || screen.CustomerName.Contains(CustomerSearch, StringComparison.OrdinalIgnoreCase)) &&
        (string.IsNullOrEmpty(DescriptionSearch) || screen.Description.Contains(DescriptionSearch, StringComparison.OrdinalIgnoreCase))
    ).ToList();
        }

        public static Size GetControlSize()
        {
            return new Size(1210, 70);
        }

    }
}