https://www.w3schools.com/cs/cs_method_parameters.php

/*############################################################################
 Basics and Theory
############################################################################*/
/* C#
    Theory:
        -- Interpreted language like Python
        -- Microsoft developed language based on .net
        -- ObjectNamingConvention
    Execution:
        -- every line of executing code must be inside a class
        -- ; at the end of codelines
        -- Main Method is the entry point, aka first method to be called
        -- Operators: ==, !=, ||, &&, ! (not, aka is not reverse --> !(x=5))

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

string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
int[] myNum = { 10, 20, 30, 40 }; // myNum[0]


string UserInput = Console.ReadLine();

//Casting: tolerates data loss due to change of datatype
float floater = 69.8;
int iamnow69 = (int) floater;

//Converting: fails if info gets lost, aka its not 1:1 transformation
string stringnow = Convert.ToString(floater);

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
//Using is a Namespace, allows usage of everything within this Namespace
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