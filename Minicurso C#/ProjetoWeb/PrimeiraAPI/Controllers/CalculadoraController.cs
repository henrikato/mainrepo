using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace PrimeiraAPI.Controllers
{
    [Route("/api/[controller]")]
    public class CalculadoraController : Controller
    {
        [HttpPost]
        public double Somar([FromBody] Dictionary<string, string> valores)
        {
            var numero1 = double.Parse(valores["numero1"]);
            var numero2 = double.Parse(valores["numero2"]);
            return numero1 + numero2;
        }
    }
}
