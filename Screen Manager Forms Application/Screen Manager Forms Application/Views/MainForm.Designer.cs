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
            LocationsPage = new TabPage();
            LogoLabel = new Label();
            ScreensPanel = new FlowLayoutPanel();
            AddScreenButton = new Button();
            LocationsPanel = new FlowLayoutPanel();
            AddLocationButton = new Button();
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
            tabControl1.Size = new Size(1240, 874);
            tabControl1.TabIndex = 0;
            // 
            // ScreensPage
            // 
            ScreensPage.Controls.Add(AddScreenButton);
            ScreensPage.Controls.Add(ScreensPanel);
            ScreensPage.Location = new Point(4, 39);
            ScreensPage.Name = "ScreensPage";
            ScreensPage.Padding = new Padding(3);
            ScreensPage.Size = new Size(1232, 831);
            ScreensPage.TabIndex = 0;
            ScreensPage.Text = "Screens";
            ScreensPage.UseVisualStyleBackColor = true;
            // 
            // LocationsPage
            // 
            LocationsPage.Controls.Add(AddLocationButton);
            LocationsPage.Controls.Add(LocationsPanel);
            LocationsPage.Location = new Point(4, 39);
            LocationsPage.Name = "LocationsPage";
            LocationsPage.Padding = new Padding(3);
            LocationsPage.Size = new Size(1232, 831);
            LocationsPage.TabIndex = 1;
            LocationsPage.Text = "Locations";
            LocationsPage.UseVisualStyleBackColor = true;
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
            // ScreensPanel
            // 
            ScreensPanel.AutoScroll = true;
            ScreensPanel.FlowDirection = FlowDirection.TopDown;
            ScreensPanel.Location = new Point(6, 6);
            ScreensPanel.Name = "ScreensPanel";
            ScreensPanel.Size = new Size(1220, 750);
            ScreensPanel.TabIndex = 0;
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
            // LocationsPanel
            // 
            LocationsPanel.Location = new Point(6, 6);
            LocationsPanel.Name = "LocationsPanel";
            LocationsPanel.Size = new Size(1220, 750);
            LocationsPanel.TabIndex = 0;
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
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1264, 921);
            Controls.Add(LogoLabel);
            Controls.Add(tabControl1);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            MaximizeBox = false;
            Name = "MainForm";
            Text = "Ocean Creek Apparel - Screens Manager";
            Load += MainForm_Load;
            tabControl1.ResumeLayout(false);
            ScreensPage.ResumeLayout(false);
            LocationsPage.ResumeLayout(false);
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private TabControl tabControl1;
        private TabPage ScreensPage;
        private TabPage LocationsPage;
        private Button AddScreenButton;
        private FlowLayoutPanel ScreensPanel;
        private Label LogoLabel;
        private Button AddLocationButton;
        private FlowLayoutPanel LocationsPanel;
    }
}