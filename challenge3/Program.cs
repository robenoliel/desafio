using System;

namespace challenge3
{
    class Program
    {
        static void Main(string[] args)
        {
            //test values
            double fv = 1420.68;
            double rate = 0.05;
            int initial_age = 20;
            int final_age = 30;

            double deposit = deposit_calculator(fv, rate, initial_age, final_age);
            Console.WriteLine("Necessary deposit: {0}", deposit);
        }

        static double deposit_calculator(double fv, double rate, int initial_age, int final_age)
        {
            int n_periods = (final_age - initial_age) * 12;
            return fv * rate / (Math.Pow(1 + rate, n_periods + 1) - 1);
        }
    }
}
