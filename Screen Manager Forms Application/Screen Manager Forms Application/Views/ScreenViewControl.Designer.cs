namespace Screen_Manager_Forms_Application.Views
{
    partial class ScreenViewControl
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
            IDLabel = new Label();
            DesignLabel = new Label();
            LocationLabel = new Label();
            CustomerLabel = new Label();
            QuantityLabel = new Label();
            DescriptionLabel = new Label();
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            label6 = new Label();
            label7 = new Label();
            SuspendLayout();
            // 
            // IDLabel
            // 
            IDLabel.AutoSize = true;
            IDLabel.Font = new Font("Segoe UI", 16F);
            IDLabel.Location = new Point(3, 20);
            IDLabel.Name = "IDLabel";
            IDLabel.Size = new Size(31, 30);
            IDLabel.TabIndex = 0;
            IDLabel.Text = "id";
            // 
            // DesignLabel
            // 
            DesignLabel.AutoSize = true;
            DesignLabel.Font = new Font("Segoe UI", 16F);
            DesignLabel.Location = new Point(67, 20);
            DesignLabel.Name = "DesignLabel";
            DesignLabel.Size = new Size(77, 30);
            DesignLabel.TabIndex = 1;
            DesignLabel.Text = "design";
            // 
            // LocationLabel
            // 
            LocationLabel.AutoSize = true;
            LocationLabel.Font = new Font("Segoe UI", 16F);
            LocationLabel.Location = new Point(282, 20);
            LocationLabel.Name = "LocationLabel";
            LocationLabel.Size = new Size(89, 30);
            LocationLabel.TabIndex = 2;
            LocationLabel.Text = "location";
            // 
            // CustomerLabel
            // 
            CustomerLabel.AutoSize = true;
            CustomerLabel.Font = new Font("Segoe UI", 16F);
            CustomerLabel.Location = new Point(510, 20);
            CustomerLabel.Name = "CustomerLabel";
            CustomerLabel.Size = new Size(103, 30);
            CustomerLabel.TabIndex = 3;
            CustomerLabel.Text = "customer";
            // 
            // QuantityLabel
            // 
            QuantityLabel.AutoSize = true;
            QuantityLabel.Font = new Font("Segoe UI", 16F);
            QuantityLabel.Location = new Point(692, 20);
            QuantityLabel.Name = "QuantityLabel";
            QuantityLabel.Size = new Size(91, 30);
            QuantityLabel.TabIndex = 4;
            QuantityLabel.Text = "quantity";
            // 
            // DescriptionLabel
            // 
            DescriptionLabel.AutoSize = true;
            DescriptionLabel.Font = new Font("Segoe UI", 16F);
            DescriptionLabel.Location = new Point(862, 20);
            DescriptionLabel.Name = "DescriptionLabel";
            DescriptionLabel.Size = new Size(122, 30);
            DescriptionLabel.TabIndex = 5;
            DescriptionLabel.Text = "Description";
            // 
            // label1
            // 
            label1.BackColor = SystemColors.ActiveCaptionText;
            label1.Location = new Point(51, 0);
            label1.Name = "label1";
            label1.Size = new Size(10, 70);
            label1.TabIndex = 6;
            label1.Text = "label1";
            // 
            // label2
            // 
            label2.BackColor = SystemColors.ActiveCaptionText;
            label2.Location = new Point(266, 0);
            label2.Name = "label2";
            label2.Size = new Size(10, 70);
            label2.TabIndex = 7;
            label2.Text = "label2";
            // 
            // label3
            // 
            label3.BackColor = SystemColors.ActiveCaptionText;
            label3.Location = new Point(494, 0);
            label3.Name = "label3";
            label3.Size = new Size(10, 70);
            label3.TabIndex = 8;
            label3.Text = "label3";
            // 
            // label4
            // 
            label4.BackColor = SystemColors.ActiveCaptionText;
            label4.Location = new Point(676, 0);
            label4.Name = "label4";
            label4.Size = new Size(10, 70);
            label4.TabIndex = 9;
            label4.Text = "label4";
            // 
            // label5
            // 
            label5.BackColor = SystemColors.ActiveCaptionText;
            label5.Location = new Point(846, 0);
            label5.Name = "label5";
            label5.Size = new Size(10, 70);
            label5.TabIndex = 10;
            label5.Text = "label5";
            // 
            // label6
            // 
            label6.BackColor = SystemColors.ActiveCaptionText;
            label6.Location = new Point(0, 0);
            label6.Name = "label6";
            label6.Size = new Size(1220, 5);
            label6.TabIndex = 11;
            label6.Text = "label6";
            // 
            // label7
            // 
            label7.BackColor = SystemColors.ActiveCaptionText;
            label7.Location = new Point(0, 65);
            label7.Name = "label7";
            label7.Size = new Size(1220, 5);
            label7.TabIndex = 12;
            label7.Text = "label7";
            // 
            // ScreenViewControl
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            Controls.Add(label7);
            Controls.Add(label6);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(DescriptionLabel);
            Controls.Add(QuantityLabel);
            Controls.Add(CustomerLabel);
            Controls.Add(LocationLabel);
            Controls.Add(DesignLabel);
            Controls.Add(IDLabel);
            Name = "ScreenViewControl";
            Size = new Size(1219, 70);
            Load += ScreenViewControl_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        public Label IDLabel;
        public Label DesignLabel;
        public Label LocationLabel;
        public Label CustomerLabel;
        public Label QuantityLabel;
        public Label DescriptionLabel;
        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private Label label6;
        private Label label7;
    }
}
