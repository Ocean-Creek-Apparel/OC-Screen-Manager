using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Screen_Manager_Forms_Application.Controllers;
using Screen_Manager_Forms_Application.Models;

namespace Screen_Manager_Forms_Application.Views
{
    public partial class LocationViewControl : UserControl
    {
        internal Location location { get; private set; }
        internal LocationViewControl(Location loc)
        {
            location = loc;
            InitializeComponent();
            UpdateLabels();
        }

        internal void UpdateLabels()
        {
            IDLabel.Text = $"ID: {location.GetID}";
            DescriptionLabel.Text = $"Description: {location.Description}";
        }
        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
