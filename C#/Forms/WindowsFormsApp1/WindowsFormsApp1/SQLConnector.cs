using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WindowsFormsApp1
{
    public class SQLConnector : DummyInterface
    {
        //Implementation of the not DummyInterface function
        DummyClass DummyInterface.CreateDummy(DummyClass dummyClass)
        {
            dummyClass.outputInt = 420;
            dummyClass.stringOutput = "69";

            return dummyClass;
        }
    }
}
