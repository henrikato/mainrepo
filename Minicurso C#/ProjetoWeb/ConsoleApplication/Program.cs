using System;

namespace ConsoleApplication
{
    class Program
    {
        static void Main(string[] args)
        {
            var a = new Aluno(); // chama o construtor
            a.Nome = "Rodrigo Gonçalves"; // chama o método set da propriedade Nome
            a.DataNascimento = new DateTime(1998, 1, 5); // chama o método set da propriedade DataNascimento
            Console.WriteLine($"A idade de { a.Nome} { a.Idade}");
            
            //var cal = new Calculadora();
            //var x = cal.Somar(10, 5);
            //cal.Alertar(x);

            //Console.WriteLine("Hello World!");
            //int x;
            //x = int.Parse(Console.ReadLine());
            //var nome = Console.ReadLine();
            //Console.WriteLine("Seu nome é {1}. E você digitou o número {0}.", x, nome);
            //Console.ReadLine();
        }
    }
}
