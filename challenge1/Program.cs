using System;

namespace challenge1
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 3, b = 5; //dummy values
            Console.WriteLine("Initial values: a = {0}, b = {1}", a, b);

            a = a + b; //a = (a+b)
            b = a - b; //b = (a+b)-b = a
            a = a - b; //a = (a+b)-a = b

            Console.WriteLine("Final values: a = {0}, b = {1}", a, b);
        }
    }
}
