using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Partial
{
     class Program
    {
        static void Main(string[] args)
        {
            Partialclass p = new Partialclass();
           
            p.Id = 10;
            p.Firstname = "monica";
            p.Lastname = "thummakuru";
            p.Salary = 50000;
            
            p.Display();
            
            Console.ReadLine();


        }
    }
}
