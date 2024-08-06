namespace Screen_Manager_Forms_Application.Views
{
    partial class LocationViewControl
    {
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
            IDLabel = new Label();
            DescriptionLabel = new Label();
            ModifyButton = new Button();
            SuspendLayout();
            // 
            // IDLabel
            // 
            IDLabel.AutoSize = true;
            IDLabel.Font = new Font("Segoe UI", 20F);
            IDLabel.Location = new Point(0, 14);
            IDLabel.Name = "IDLabel";
            IDLabel.Size = new Size(116, 37);
            IDLabel.TabIndex = 0;
            IDLabel.Text = "ID: ";
            // 
            // DescriptionLabel
            // 
            DescriptionLabel.AutoSize = true;
            DescriptionLabel.Font = new Font("Segoe UI", 20F);
            DescriptionLabel.Location = new Point(121, 14);
            DescriptionLabel.Name = "DescriptionLabel";
            DescriptionLabel.Size = new Size(165, 37);
            DescriptionLabel.TabIndex = 1;
            DescriptionLabel.Text = "Description: ";
            // 
            // ModifyButton
            // 
            ModifyButton.Font = new Font("Segoe UI", 20F);
            ModifyButton.Location = new Point(742, 10);
            ModifyButton.Name = "ModifyButton";
            ModifyButton.Size = new Size(150, 50);
            ModifyButton.TabIndex = 2;
            ModifyButton.Text = "Modify";
            ModifyButton.UseVisualStyleBackColor = true;
            // 
            // LocationViewControl
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            Controls.Add(ModifyButton);
            Controls.Add(DescriptionLabel);
            Controls.Add(IDLabel);
            Name = "LocationViewControl";
            Size = new Size(900, 70);
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label IDLabel;
        private Label DescriptionLabel;
        private Button ModifyButton;
    }
}
