namespace WindowsFormsApp1
{
    partial class WindowForm
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
            this.label1 = new System.Windows.Forms.Label();
            this.checkBox1 = new System.Windows.Forms.CheckBox();
            this.CheckBoxButton = new System.Windows.Forms.Button();
            this.ChangeLabelButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.SystemColors.ActiveBorder;
            this.label1.Font = new System.Drawing.Font("Bernard MT Condensed", 16.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(294, 164);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(157, 33);
            this.label1.TabIndex = 1;
            this.label1.Text = "Random Text";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // checkBox1
            // 
            this.checkBox1.AutoSize = true;
            this.checkBox1.ForeColor = System.Drawing.Color.Coral;
            this.checkBox1.Location = new System.Drawing.Point(320, 87);
            this.checkBox1.Name = "checkBox1";
            this.checkBox1.Size = new System.Drawing.Size(99, 22);
            this.checkBox1.TabIndex = 2;
            this.checkBox1.Text = "CheckBox";
            this.checkBox1.UseVisualStyleBackColor = true;
            this.checkBox1.CheckedChanged += new System.EventHandler(this.checkBox1_CheckedChanged);
            // 
            // CheckBoxButton
            // 
            this.CheckBoxButton.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.CheckBoxButton.ForeColor = System.Drawing.Color.Coral;
            this.CheckBoxButton.Location = new System.Drawing.Point(31, 87);
            this.CheckBoxButton.Name = "CheckBoxButton";
            this.CheckBoxButton.Size = new System.Drawing.Size(189, 40);
            this.CheckBoxButton.TabIndex = 3;
            this.CheckBoxButton.Text = "CheckBoxButton";
            this.CheckBoxButton.UseVisualStyleBackColor = false;
            this.CheckBoxButton.Click += new System.EventHandler(this.button1_Click);
            // 
            // ChangeLabelButton
            // 
            this.ChangeLabelButton.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.ChangeLabelButton.ForeColor = System.Drawing.Color.Coral;
            this.ChangeLabelButton.Location = new System.Drawing.Point(31, 157);
            this.ChangeLabelButton.Name = "ChangeLabelButton";
            this.ChangeLabelButton.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.ChangeLabelButton.Size = new System.Drawing.Size(189, 40);
            this.ChangeLabelButton.TabIndex = 5;
            this.ChangeLabelButton.Text = "ChangeLabelButton";
            this.ChangeLabelButton.UseVisualStyleBackColor = false;
            this.ChangeLabelButton.Click += new System.EventHandler(this.ChangeLabelButton_Click);
            // 
            // WindowForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 18F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.ClientSize = new System.Drawing.Size(900, 506);
            this.Controls.Add(this.ChangeLabelButton);
            this.Controls.Add(this.CheckBoxButton);
            this.Controls.Add(this.checkBox1);
            this.Controls.Add(this.label1);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Name = "WindowForm";
            this.Text = "WindowName";
            this.Load += new System.EventHandler(this.WindowForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.CheckBox checkBox1;
        private System.Windows.Forms.Button CheckBoxButton;
        private System.Windows.Forms.Button ChangeLabelButton;
    }
}

