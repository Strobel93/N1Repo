/*############################################################################
 Basics and Theory
############################################################################*/
/* C#
    Theory:
        -- Interpreted language like Python
        -- Microsoft developed language based on .net
        -- ObjectNamingConvention
            --RegularConventionForMost
            --exceptionConventions
                --methodArguments
                --localVariables
                --fieldName
    Execution:
        -- every line of executing code must be inside a class
        -- ; at the end of codelines
        -- Main Method is the entry point, aka first method to be called
        -- Operators: 
               ==, !=, ||, &&, ! (not, aka is not reverse --> !(x=5))
               +=,-=
        -- "static" Keyword: 
            --can be called without instanciation of the object
            --faster than non static objects, due to internal pointer overhead
*/
//############################################################################
// Variables (int,long   float,double   char,string   bool)
//############################################################################
//Assignment
string name = "Craig";
string escaper = "Craig aka \"The King\"";
bool true = true;
int number = 69;
const string = "can not be altered";
int x = 69, y = 70, z = 71;
x = y = z = 70;
x.GetType();

string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
int[] myNum = { 10, 20, 30, 40 }; // myNum[0]


string UserInput = Console.ReadLine();

//Casting: tolerates data loss due to change of datatype
float floater = 69.8;
int iAmNow69 = (int) floater;

//Converting: fails if info gets lost, aka its not 1:1 transformation
string stringNow = Convert.ToString(floater);

//############################################################################
// Basic Methods
//############################################################################
//Math:
Math.MIN(5,10);
Math.Abs(-5);
Math.Floor(5.9);

//String:
name.Length;
name.ToUpper();
string NewName = string.Concat(name, name);
char CharAtIndex1 = name[1];
int IndexPos = name.IndexOf('e'); 

string firstName = "John";
string lastName = "Doe";
string name = $"My full name is: {firstName} {lastName}";
//############################################################################
//"using" is a Namespace, allows usage of everything within this Namespace
//############################################################################
//Version with  
using System;
Console.WriteLine("With");

//without using
System.Console.WriteLine("without");

//Import stuff from other C# files by calling the relevant Namespaces (not file)
using ImportedNameSpace;

ImportedClass.ImportedMethod();
ImportedNameSpace.ImportedClass.ImportedMethod();

//############################################################################
//Namespace = grouping code and make it calluable by referencing namespace
//############################################################################
namespace NamespaceName
{
    public class ExampleClass
    {
        public static void ExampleMethod()
        {
            Console.WriteLine("FK u");
        }
    }
}

//Object calling using Namespaces, Classes and Objects
namespace ActualProgram
{
    public class ExecutionClass
    {
        public static void CallOtherMethod()
        {
            NamespaceName.ExampleClass.ExampleMethod();
        }
    }
}

//############################################################################
//Methods
//############################################################################
//simple param
//VOID = does not have a return
static void ParamMethod(string param = "Default", int param2)
{
    Console.WriteLine(param + param2);
}

ParamMethod("CallWithParameter",69);

//named param, key: value (ignore order)
static void NamedParamMethod(int p1, int p2, int p3)
{
    Console.WriteLine("The last param is" + p3); 
}

NamedParamMethod(p3: 69);

//return 
static void ReturnMethod(int ret)
{
    return ret + 69;
}

int mf = ReturnMethod(420);

//Overloading: methods can have the same name if number and/or type of parameters are different
static void Adding(int x, int y)
{
    return x + y;
}

static void Adding(double x, double y)
{
    return x + y;
}

Adding(69+420);
Adding(1.1 + 2.2);


//############################################################################
//Classes
//############################################################################
//Simple class without constructor
class Base
{
    public int x = 69;
}
Base obj = New Base();
obj.x;

//Simple class with constructor function to overwrite base constructor 
class Base
{
    //Fieldlist
    public int F1;
    public int F2;

    //classname = constructor name
    public Base(string P1, string P1)
    {
        this.F1 = P1;
        this.F2 = P2;
    }
}

Base obj1 = new Base(69, 420);

//Getter and Setter
namespace SetupClass
{
    class Person
    {   //use the property to change the filed, inderect acess
        private string name; // field
        public string Name   // property
        {
            get { return name; }
            set { name = value; }
        }
        //Conditional set
        public int yearOfBirth
        {
            get { return yearOfBirth; }
            set
            {
                if (value > 1900 || value < 3000)
                { yearOfBirth = value; }
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {   //call of getter/setter of the Property "Name" influences field "name"
            Person myObj = new Person();
            myObj.Name = "Liam";
            Console.WriteLine(myObj.Name);
            //Public field can be altered even later one
            myObj.yearOfBirth = 420;
            //Does not work because private
            //Console.WriteLine(myObj.name);
        }
    }

//Inheritance
class Vehicle  // base class (parent) 
{
    public string brand = "Ford";  // Vehicle field
    public void honk()             // Vehicle method 
    {
        Console.WriteLine("Tuut, tuut!");
    }
}

class Car : Vehicle  // derived class (child)
{
    public string modelName = "Mustang";  // Car field
    public override honk()
        {
            Console.WriteLine("Do NAT Tuut, tuut!");
            base.honk(); //Uses the original honk version
        }
    }

Car vroom = new Car();
vroom.modelName;
vroom.brand;
vroom.honk();

//############################################################################
//Static
//############################################################################
//Accessing:
//Static can be accesed without any class instanciation
//Non Static can be accessed once the class has been instanciated
namespace StaticNonStaticDemo
{
    class Example
    {
        int x; // Non-Static Variable
        static int y = 200; //Static Variable
        public Example(int x)
        {
            //Initializing Non-Static Variable
            this.x = x;
        }
        static void Main(string[] args)
        {
            //Static
            Console.WriteLine(Example.y);

            //Non Static
            //Creating Object1
            Example obj = new Example(50);
            Console.WriteLine(obj.x);
        }
    }
}

//############################################################################
// Control Flow
//############################################################################
//if
if (time < 10)
{
    Console.WriteLine("Good morning.");
}
else if (time < 20)
{
    Console.WriteLine("Good day.");
}
else
{
    Console.WriteLine("Good evening.");
}

//switch
switch (day)
{
    case 1:
        Console.WriteLine("Monday");
        break;
    case 2:
        Console.WriteLine("Tuesday");
        break;
}


//while
while (i < 5)
{
    Console.WriteLine(i);
    i++;
}

//for loop with a break (ends loop), continue (skips iteration)
for (int i = 0; i < 10; i++)
{
    if (i == 4)
    {
        break;
    }
    Console.WriteLine(i);
}

//for each 
string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
foreach (string i in cars)
{
    Console.WriteLine(i);
}

//############################################################################
//Error Handling
//############################################################################
try
{
    //Dividing, not through 0
    public int res;
    res = 5 / 0;
}
catch
{
    Console.WriteLine("Can not Divide through 0")
}
finally
{
    //Optional, always executed after try or catch
    Console.WriteLine("Prog Over")

}