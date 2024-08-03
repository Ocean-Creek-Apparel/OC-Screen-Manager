namespace Screen_Manager_Forms_Application.Controllers
{
    internal static class MainController
    {
        [STAThread]
        static void Main()
        {
            // To customize application configuration such as set high DPI settings or default font,
            // see https://aka.ms/applicationconfiguration.
            // ApplicationConfiguration.Initialize();
            // Application.Run(new Form1());

            LocationController locationController = new();
            locationController.Debug_CheckLocationsLoaded();
            ScreenController screenController = new();
            screenController.Debug_CheckScreensLoaded();
        }
    }
}