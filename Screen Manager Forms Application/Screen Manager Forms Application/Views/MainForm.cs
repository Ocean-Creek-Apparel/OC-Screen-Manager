using Screen_Manager_Forms_Application.Controllers;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Screen_Manager_Forms_Application.Views
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {

        }

        private void ScreenIDLabel_Click(object sender, EventArgs e)
        {

        }

        private void ScreenIDSearchBox_TextChanged(object sender, EventArgs e)
        {
            MainController.IDSearch = ScreenIDSearchBox.Text;
            MainController.Search();
        }

        private void DesignSearchBox_TextChanged(object sender, EventArgs e)
        {
            MainController.DesignSearch = DesignSearchBox.Text;
            MainController.Search();
        }

        private void LocationSearchBox_TextChanged(object sender, EventArgs e)
        {
            MainController.LocationSearch = LocationSearchBox.Text;
            MainController.Search();
        }

        private void CustomerSearchBox_TextChanged(object sender, EventArgs e)
        {
            MainController.CustomerSearch = CustomerSearchBox.Text;
            MainController.Search();
        }

        private void DescriptionSearchBox_TextChanged(object sender, EventArgs e)
        {
            MainController.DescriptionSearch = DescriptionSearchBox.Text;
            MainController.Search();
        }
    }
}
