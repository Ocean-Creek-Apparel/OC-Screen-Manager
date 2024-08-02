using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Screen_Manager_Forms_Application.Models
{
    internal class Location
    {
        private int ID; // Unique Identifer
        public string Description { get; set; } // Additional Information
        public Location(int id, string desc) // Constructor
        {
            ID = id;
            Description = desc;
        }

        public int GetID()
        {
            return ID;
        }

        public override string ToString()
        {
            return $"{ID} - {Description}";
        }
    }
}
