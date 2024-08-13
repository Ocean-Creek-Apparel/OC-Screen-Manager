namespace Screen_Manager_Forms_Application.Views
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            tabControl1 = new TabControl();
            ScreensPage = new TabPage();
            DescriptionSearchBox = new TextBox();
            CustomerSearchBox = new TextBox();
            LocationSearchBox = new TextBox();
            DesignSearchBox = new TextBox();
            ScreenIDSearchBox = new TextBox();
            label2 = new Label();
            label1 = new Label();
            CustomerLabel = new Label();
            LocationLabel = new Label();
            DesignLabel = new Label();
            ScreenIDLabel = new Label();
            AddScreenButton = new Button();
            ScreensPanel = new FlowLayoutPanel();
            LocationsPage = new TabPage();
            AddLocationButton = new Button();
            LocationsPanel = new FlowLayoutPanel();
            LogoLabel = new Label();
            tabControl1.SuspendLayout();
            ScreensPage.SuspendLayout();
            LocationsPage.SuspendLayout();
            SuspendLayout();
            // 
            // tabControl1
            // 
            tabControl1.Controls.Add(ScreensPage);
            tabControl1.Controls.Add(LocationsPage);
            tabControl1.Font = new Font("Segoe UI", 16F);
            tabControl1.Location = new Point(12, 42);
            tabControl1.Name = "tabControl1";
            tabControl1.SelectedIndex = 0;
            tabControl1.Size = new Size(1570, 874);
            tabControl1.TabIndex = 0;
            // 
            // ScreensPage
            // 
            ScreensPage.Controls.Add(DescriptionSearchBox);
            ScreensPage.Controls.Add(CustomerSearchBox);
            ScreensPage.Controls.Add(LocationSearchBox);
            ScreensPage.Controls.Add(DesignSearchBox);
            ScreensPage.Controls.Add(ScreenIDSearchBox);
            ScreensPage.Controls.Add(label2);
            ScreensPage.Controls.Add(label1);
            ScreensPage.Controls.Add(CustomerLabel);
            ScreensPage.Controls.Add(LocationLabel);
            ScreensPage.Controls.Add(DesignLabel);
            ScreensPage.Controls.Add(ScreenIDLabel);
            ScreensPage.Controls.Add(AddScreenButton);
            ScreensPage.Controls.Add(ScreensPanel);
            ScreensPage.Location = new Point(4, 39);
            ScreensPage.Name = "ScreensPage";
            ScreensPage.Padding = new Padding(3);
            ScreensPage.Size = new Size(1562, 831);
            ScreensPage.TabIndex = 0;
            ScreensPage.Text = "Screens";
            ScreensPage.UseVisualStyleBackColor = true;
            // 
            // DescriptionSearchBox
            // 
            DescriptionSearchBox.Location = new Point(932, 6);
            DescriptionSearchBox.Name = "DescriptionSearchBox";
            DescriptionSearchBox.Size = new Size(295, 36);
            DescriptionSearchBox.TabIndex = 12;
            DescriptionSearchBox.TextChanged += DescriptionSearchBox_TextChanged;
            // 
            // CustomerSearchBox
            // 
            CustomerSearchBox.Location = new Point(638, 6);
            CustomerSearchBox.Name = "CustomerSearchBox";
            CustomerSearchBox.Size = new Size(288, 36);
            CustomerSearchBox.TabIndex = 11;
            CustomerSearchBox.TextChanged += CustomerSearchBox_TextChanged;
            // 
            // LocationSearchBox
            // 
            LocationSearchBox.Location = new Point(370, 6);
            LocationSearchBox.Name = "LocationSearchBox";
            LocationSearchBox.Size = new Size(262, 36);
            LocationSearchBox.TabIndex = 10;
            LocationSearchBox.TextChanged += LocationSearchBox_TextChanged;
            // 
            // DesignSearchBox
            // 
            DesignSearchBox.Location = new Point(59, 6);
            DesignSearchBox.Name = "DesignSearchBox";
            DesignSearchBox.Size = new Size(305, 36);
            DesignSearchBox.TabIndex = 9;
            DesignSearchBox.TextChanged += DesignSearchBox_TextChanged;
            // 
            // ScreenIDSearchBox
            // 
            ScreenIDSearchBox.Location = new Point(6, 6);
            ScreenIDSearchBox.Name = "ScreenIDSearchBox";
            ScreenIDSearchBox.Size = new Size(47, 36);
            ScreenIDSearchBox.TabIndex = 8;
            ScreenIDSearchBox.TextChanged += ScreenIDSearchBox_TextChanged;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(932, 45);
            label2.Name = "label2";
            label2.Size = new Size(122, 30);
            label2.TabIndex = 7;
            label2.Text = "Description";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(1461, 45);
            label1.Name = "label1";
            label1.Size = new Size(95, 30);
            label1.TabIndex = 6;
            label1.Text = "Quantity";
            // 
            // CustomerLabel
            // 
            CustomerLabel.AutoSize = true;
            CustomerLabel.Location = new Point(638, 45);
            CustomerLabel.Name = "CustomerLabel";
            CustomerLabel.Size = new Size(107, 30);
            CustomerLabel.TabIndex = 5;
            CustomerLabel.Text = "Customer";
            // 
            // LocationLabel
            // 
            LocationLabel.AutoSize = true;
            LocationLabel.Location = new Point(370, 45);
            LocationLabel.Name = "LocationLabel";
            LocationLabel.Size = new Size(94, 30);
            LocationLabel.TabIndex = 4;
            LocationLabel.Text = "Location";
            // 
            // DesignLabel
            // 
            DesignLabel.AutoSize = true;
            DesignLabel.Location = new Point(59, 45);
            DesignLabel.Name = "DesignLabel";
            DesignLabel.Size = new Size(79, 30);
            DesignLabel.TabIndex = 3;
            DesignLabel.Text = "Design";
            // 
            // ScreenIDLabel
            // 
            ScreenIDLabel.AutoSize = true;
            ScreenIDLabel.Location = new Point(6, 45);
            ScreenIDLabel.Name = "ScreenIDLabel";
            ScreenIDLabel.Size = new Size(34, 30);
            ScreenIDLabel.TabIndex = 2;
            ScreenIDLabel.Text = "ID";
            ScreenIDLabel.Click += ScreenIDLabel_Click;
            // 
            // AddScreenButton
            // 
            AddScreenButton.Location = new Point(6, 762);
            AddScreenButton.Name = "AddScreenButton";
            AddScreenButton.Size = new Size(275, 63);
            AddScreenButton.TabIndex = 1;
            AddScreenButton.Text = "Add New Screen";
            AddScreenButton.UseVisualStyleBackColor = true;
            // 
            // ScreensPanel
            // 
            ScreensPanel.AutoScroll = true;
            ScreensPanel.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            ScreensPanel.FlowDirection = FlowDirection.TopDown;
            ScreensPanel.Location = new Point(3, 78);
            ScreensPanel.Name = "ScreensPanel";
            ScreensPanel.Size = new Size(1553, 678);
            ScreensPanel.TabIndex = 0;
            ScreensPanel.WrapContents = false;
            // 
            // LocationsPage
            // 
            LocationsPage.Controls.Add(AddLocationButton);
            LocationsPage.Controls.Add(LocationsPanel);
            LocationsPage.Location = new Point(4, 39);
            LocationsPage.Name = "LocationsPage";
            LocationsPage.Padding = new Padding(3);
            LocationsPage.Size = new Size(1562, 831);
            LocationsPage.TabIndex = 1;
            LocationsPage.Text = "Locations";
            LocationsPage.UseVisualStyleBackColor = true;
            // 
            // AddLocationButton
            // 
            AddLocationButton.Location = new Point(6, 762);
            AddLocationButton.Name = "AddLocationButton";
            AddLocationButton.Size = new Size(275, 63);
            AddLocationButton.TabIndex = 2;
            AddLocationButton.Text = "Add New Location";
            AddLocationButton.UseVisualStyleBackColor = true;
            // 
            // LocationsPanel
            // 
            LocationsPanel.Location = new Point(6, 6);
            LocationsPanel.Name = "LocationsPanel";
            LocationsPanel.Size = new Size(1220, 750);
            LocationsPanel.TabIndex = 0;
            // 
            // LogoLabel
            // 
            LogoLabel.AutoSize = true;
            LogoLabel.Font = new Font("Segoe UI", 16F);
            LogoLabel.Location = new Point(12, 9);
            LogoLabel.Name = "LogoLabel";
            LogoLabel.Size = new Size(394, 30);
            LogoLabel.TabIndex = 0;
            LogoLabel.Text = "Ocean Creek Apparel Screens Manager";
            // 
            // MainForm
            // 
            AutoScaleMode = AutoScaleMode.None;
            ClientSize = new Size(1594, 921);
            Controls.Add(LogoLabel);
            Controls.Add(tabControl1);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;
            Name = "MainForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "Ocean Creek Apparel - Screens Manager";
            Load += MainForm_Load;
            tabControl1.ResumeLayout(false);
            ScreensPage.ResumeLayout(false);
            ScreensPage.PerformLayout();
            LocationsPage.ResumeLayout(false);
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        public TabControl tabControl1;
        public TabPage ScreensPage;
        private TabPage LocationsPage;
        public FlowLayoutPanel ScreensPanel;
        private Label LogoLabel;
        private Button AddLocationButton;
        private FlowLayoutPanel LocationsPanel;
        private Label label2;
        private Label label1;
        private Label CustomerLabel;
        private Label LocationLabel;
        private Label DesignLabel;
        private Label ScreenIDLabel;
        private TextBox DescriptionSearchBox;
        private TextBox CustomerSearchBox;
        private TextBox LocationSearchBox;
        private TextBox DesignSearchBox;
        private TextBox ScreenIDSearchBox;
        private Button AddScreenButton;
    }
}