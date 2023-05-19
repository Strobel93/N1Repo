using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class WindowForm : Form
    {
        int curr = 0;
        public WindowForm()
        {
            InitializeComponent();
        }
        // Clicking Functions
        private void label1_Click(object sender, EventArgs e)
        {
            Console.WriteLine("Label Clicked");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Call custom function
            CheckBoxWithButton();
        }

        private void ChangeLabelButton_Click(object sender, EventArgs e)
        {
            // Call function and return the value to add a counter
            curr = ChangeText(curr);

            //Using a button and form content to create a new class
            //Append Class to List, Save Data somewhere, ....
            DummyClass dc = new DummyClass(Int32.Parse(label1.Text), label2.Text);
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            Console.WriteLine("Checkbox ON/OFF");
        }

        //Custom function used on Button to check if Checkbox is checked
        public void CheckBoxWithButton()
        {   //reference form object name.attribute
            if (checkBox1.Checked == true)
                { checkBox1.Checked = false; }
            else
                { checkBox1.Checked = true; }
        }

        public int ChangeText(int currentValue)
        {
            int newcurrentValue = currentValue +1 ;
            label1.Text = newcurrentValue.ToString();
            return newcurrentValue;
        }


        private void WindowForm_Load(object sender, EventArgs e)
        {

        }
    }
}
