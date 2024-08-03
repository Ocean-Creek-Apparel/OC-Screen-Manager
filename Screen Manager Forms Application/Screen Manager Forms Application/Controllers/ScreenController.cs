using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Screen_Manager_Forms_Application.Controllers
{
    internal class ScreenController
    {
        private List<Screen> Screens = new();

        public ScreenController()
        {
            Screens = LoadAllScreensFromDatabase();
        }
        private List<Screen> LoadAllScreensFromDatabase()
        {

        }

        public void Debug_CheckScreensLoaded()
        {
            foreach(Screen s in Screens)
            {
                Debug.WriteLine(s);
            }
        }
    }
}
