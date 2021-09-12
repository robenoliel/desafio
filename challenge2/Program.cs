using System;

namespace challenge2
{
    class Program
    {
        static void Main(string[] args)
        {
            float[,] timings = new float[3,3]; //timings = {bubble {n1, n2, n3}, quick {n1, n2, n3}, merge {n1, n2, n3}}
            int i;
            int[] n = {(int)10e1, (int)10e2, (int)10e3};
            var watch = System.Diagnostics.Stopwatch.StartNew();

            for (i = 0;i < 3; i++)
            {
                int[] source = new int[n[i]];
                source = generate_random_array(n[i]);
                int[] bubble_array = new int[n[i]];
                source.CopyTo(bubble_array,0);
                int[] quick_array = new int[n[i]];
                source.CopyTo(quick_array,0);
                int[] merge_array = new int[n[i]];
                source.CopyTo(merge_array,0);

                watch.Restart();
                bubble_array = bubble_sort(bubble_array);
                watch.Stop();
                timings[0, i] = watch.ElapsedMilliseconds;

                watch.Restart();
                quick_array = quick_sort(quick_array);
                watch.Stop();
                timings[1, i] = watch.ElapsedMilliseconds;

                watch.Restart();
                merge_array = merge_sort(merge_array);
                watch.Stop();
                timings[2, i] = watch.ElapsedMilliseconds;
            }
            

            for (i = 0; i <timings.Length; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    Console.WriteLine(timings[i,j]);
                }
                Console.WriteLine();
            }
        }

        static int[] generate_random_array(int n, int lower = -100, int upper = 100)
        {
            int i;
            int[] array = new int[n];
            Random rnd = new Random();
            for (i = 0; i < n; i++)
            {
                array[i] = rnd.Next(lower, upper);
            }
            return array;
        }
        static int[] bubble_sort(int[] array)
        {
            int i, temp;
            bool swapped = true;
            while (swapped)
            {  
                swapped = false;
                for (i = 0; i < array.Length - 1; i++)
                {
                    if (array[i] > array[i+1])
                    {
                        swapped = true;
                        temp = array[i];
                        array[i] = array[i+1];
                        array[i+1] = temp;
                    }
                }
            }
            return array;
        }

        static int[] quick_sort(int[] array, int start = 0, int end = -1)
        {
            if (end == -1) { end = array.Length - 1; }
            if (start >= end) { return array; }

            int pivot_position = partition(array, start, end);
            quick_sort(array, start, pivot_position - 1);
            quick_sort(array, pivot_position + 1, end);

            return array;
        }

        //Utility function for quick_sort
        static int partition(int[] array, int start, int end)
        {
            int temp, i;
            int j = start;

            for (i = start; i < end; i++)
            {
                if (array[i] <= array[end])
                {
                    temp = array[j];
                    array[j] = array[i];
                    array[i] = temp;
                    j++;
                }
            }

            temp = array[end];
            array[end] = array[j];
            array[j] = temp;

            return j;
        }

        static int[] merge_sort(int[] array)
        {   
            int length = array.Length;
            int middle = length / 2;
            int[] left = new int[middle];
            int[] right = new int[length - middle];
            int left_len = middle;
            int right_len = length - middle;

            //utility variables
            int i, j, k;

            //divides array by the middle
            for (i = 0; i < left_len; i++)
            {
                left[i] = array[i];
            }

            for (i = 0; i < right_len; i++)
            {
                right[i] = array[middle + i];
            }

            //sorts subarrays if their their lengths is greater than 1
            if (left_len > 1){
                left = merge_sort(left);
            }
            if (right_len > 1)
            {
                right = merge_sort(right);
            }

            //merge sorted arrays into greater one
            i = 0; j = 0; k = 0;
            int[] sorted = new int[left_len + right_len];
            while (i < left_len && j < right_len)
            {   
                if (left[i] <= right[j])
                {
                    sorted[k] = left[i];
                    i++;
                }
                else
                {
                    sorted[k] = right[j];
                    j++;
                }
                k++;
                
            }

            //ads remaining sorted elements
            while (i < left_len)
            {
                sorted[k] = left[i];
                i++; k++;
            }
            while (j < right_len)
            {
                sorted[k] = right[j];
                j++; k++;
            }

            return sorted;
            
        }
    }
}
