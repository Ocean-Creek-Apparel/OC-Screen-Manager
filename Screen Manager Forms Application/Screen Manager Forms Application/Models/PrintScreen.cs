using Screen_Manager_Forms_Application.Views;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Screen_Manager_Forms_Application.Models
{
    internal class PrintScreen
    {
        private int ID { get; } // Unique Identifier
        public Location ScreenLocation { get; set; } // Location identifier
        public int Quantity { get; set; } // How many screens there are
        public string Design { get; set; } // Design info
        public string CustomerName { get; set; } // Customer name
        public string Description { get; set; } // Additional info
        public ScreenViewControl ViewControl { get; set; }
        public int GetID()
        {
            return ID;
        }

        public PrintScreen(int id, Location location, int quantity, string design, string custName, string desc)
        {
            ID = id;
            ScreenLocation = location;
            Quantity = quantity;
            Design = design;
            CustomerName = custName;
            Description = desc;
            ViewControl = new();
            ViewControl.IDLabel.Text = Convert.ToString(id);
            ViewControl.DesignLabel.Text = design;
            ViewControl.LocationLabel.Text = Convert.ToString(location.GetID());
            ViewControl.CustomerLabel.Text = custName;
            ViewControl.QuantityLabel.Text = Convert.ToString(quantity);
            ViewControl.DescriptionLabel.Text = desc;
        }

        public override string ToString()
        {
            return $"ID: {ID}, Location: {ScreenLocation.GetID()}, Quantity: {Quantity}," +
                $" Design: {Design}, Customer: {CustomerName}, Description: {Description}";
        }
    }
}
