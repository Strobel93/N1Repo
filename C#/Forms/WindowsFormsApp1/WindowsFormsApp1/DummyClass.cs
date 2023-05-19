using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp1
{
    internal class DummyClass
    {
        public int intvalue {  get; set; }
        public string stringvalue { get; set; }

        public DummyClass(int intinput, string stringinput) 
        { 
            intvalue = intinput;
            stringvalue = stringinput;
        }
    }
}
