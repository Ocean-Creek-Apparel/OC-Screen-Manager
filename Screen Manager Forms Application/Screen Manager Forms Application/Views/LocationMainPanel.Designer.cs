namespace Screen_Manager_Forms_Application.Views
{
    public partial class LocationMainPanel
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

        #region Component Designer generated code

        /// <summary> 
        /// Required method for Designer support - do not modify 
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            IDSearchBox = new TextBox();
            LayoutPanel = new FlowLayoutPanel();
            DescriptionSearchBox = new TextBox();
            SuspendLayout();
            // 
            // IDSearchBox
            // 
            IDSearchBox.Font = new Font("Segoe UI", 20F);
            IDSearchBox.Location = new Point(3, 3);
            IDSearchBox.Name = "IDSearchBox";
            IDSearchBox.Size = new Size(153, 43);
            IDSearchBox.TabIndex = 0;
            IDSearchBox.Text = "ID Search";
            // 
            // LayoutPanel
            // 
            LayoutPanel.AutoScroll = true;
            LayoutPanel.FlowDirection = FlowDirection.TopDown;
            LayoutPanel.Location = new Point(3, 52);
            LayoutPanel.Name = "LayoutPanel";
            LayoutPanel.Size = new Size(900, 900);
            LayoutPanel.TabIndex = 1;
            // 
            // DescriptionSearchBox
            // 
            DescriptionSearchBox.Font = new Font("Segoe UI", 20F);
            DescriptionSearchBox.Location = new Point(162, 3);
            DescriptionSearchBox.Name = "DescriptionSearchBox";
            DescriptionSearchBox.Size = new Size(236, 43);
            DescriptionSearchBox.TabIndex = 2;
            DescriptionSearchBox.Text = "Description Search";
            // 
            // LocationMainPanel
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            Controls.Add(DescriptionSearchBox);
            Controls.Add(LayoutPanel);
            Controls.Add(IDSearchBox);
            Name = "LocationMainPanel";
            Size = new Size(906, 1000);
            Load += LocationMainPanel_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        public TextBox IDSearchBox;
        public FlowLayoutPanel LayoutPanel;
        public TextBox DescriptionSearchBox;
    }
}
