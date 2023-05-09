using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp1
{
    internal interface DummyInterface
    {
        // Function without Implementation (implemented in class using this)
        //DummyClass CreateDummy    = Returntype of function is DummyClass
        //(DummyClass dummyClass)   = Inputtype is DummyClass 
        DummyClass CreateDummy(DummyClass dummyClass);
    }
}
