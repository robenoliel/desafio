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
            int n_periods = 10;

            double deposit = deposit_calculator(fv, rate, n_periods);
            Console.WriteLine("Necessary deposit: {0}", deposit);
        }

        static double deposit_calculator(double fv, double rate, int n_periods)
        {
            return fv * rate / (Math.Pow(1 + rate, n_periods + 1) - 1);
        }
    }
}
