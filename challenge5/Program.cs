using System;
using System.Threading.Tasks;

namespace challenge5
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] ns = {100000, 10000000, 1000000000};
            int[] ks = {1, 2, 4, 8, 16};
            double sum;
            double[][] arrays = new double[ns.Length][];
            var watch = System.Diagnostics.Stopwatch.StartNew();
            int i,j;

            for (i = 0; i < ns.Length; i++)
            {
                arrays[i] = generate_random_array(ns[i]);
                for (j = 0; j < ks.Length; j++)
                {
                    watch.Restart();
                    sum = multithread_sum(arrays[i], ks[j]);
                    watch.Stop();
                    Console.WriteLine("N: {0}, K: {1}, sum: {2}, time: {3}",i,j,sum,watch.ElapsedMilliseconds);
                }
                Console.WriteLine();
            }

        }

        static double multithread_sum(double[] array, int k)
        {
            int n_per_thread;
            int i, j;
            double sum = 0.0;

            if (array.Length % k > 0.0)
            {
                n_per_thread = array.Length/k + 1;
            }
            else
            {
                n_per_thread = array.Length/k;
            }

            double[][] partial_arrays = new double[k][];

            for (i = 0; i < k; i++)
            {
                partial_arrays[i] = new double[n_per_thread];
            }

            for (i = 0; i < k; i++)
            {
                for (j = 0; j < n_per_thread; j++)
                {
                    try
                    {
                        partial_arrays[i][j] = array[i*n_per_thread + j];
                    }
                    catch (Exception)
                    {
                        partial_arrays[i][j] = 0;
                    }
                }
            }

            double[] partial_array = new double[n_per_thread];
            for (i = 0; i < k; i++)
            {
                partial_array = partial_arrays[i];
                sum += Task.Run(() => partial_sum(partial_array)).Result;
            }

            //Task.WaitAll();

            return sum;
        }

        static double partial_sum(double[] array)
        {
            double sum = 0;
            for (int i = 0; i < array.Length; i++)
            {
                sum += array[i];
            }
            return sum;
        }

        static double[] generate_random_array(int n, int lower = -50, int upper = 50)
        {
            int i;
            double[] array = new double[n];
            Random rnd = new Random();
            for (i = 0; i < n; i++)
            {
                array[i] = rnd.NextDouble() * (upper - lower) + lower;
            }
            return array;
        }
        
    }
}
