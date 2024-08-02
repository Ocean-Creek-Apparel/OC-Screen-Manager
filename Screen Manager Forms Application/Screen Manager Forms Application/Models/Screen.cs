using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Screen_Manager_Forms_Application.Models
{
    internal class Screen
    {
        private int ID { get; } // Unique Identifier
        private Location ScreenLocation { get; set; } // Location identifier
        private int Quantity { get; set; } // How many screens there are
        private string Design { get; set; } // Design info
        private string CustomerName { get; set; } // Customer name
        private string Description { get; set; } // Additional info

        public Screen(int id, int locationID, int quantity, string design, string custName, string desc)
        {
            ID = id;
            LocationID = locationID;
            Quantity = quantity;
            Design = design;
            CustomerName = custName;
            Description = desc;
        }
    }
}
