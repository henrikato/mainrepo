using System;
namespace ConsoleApplication
{
    public class Calculadora
    {
        public Calculadora()
        {
            Console.WriteLine("Iniciando a Calculadora...");
        }

        public double Somar(double x, double y)
        {
            return x + y;
        }

        public void Alertar(double x)
        {
            Console.WriteLine("O valor de X e: {0}", x);
        }
    }
}
