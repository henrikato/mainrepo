# mainrepo

Repositório principal onde armazeno (quase) todos os arquivos, programas e códigos desenvolvidos por mim (e alguns com a ajuda de outros contribuidores colegas de faculdade e amigos) na faculdade ou no tempo livre.
Arquivo CSS de tema customizado do Slack

------------------------------------------------------------------------------------------------------------------------------------------

##Passos para utilizar temas customizados:
1. Procurar o arquivo `ssb-interop.js`
   Caminho do arquivo: `%homepath%\AppData\Local\slack\app-x.x.x\resources\app.asar.unpacked\src\static\ssb-interop.js`
   (procurar sempre a pasta app-* mais recente, exemplo: `\app-3.2.0\`)

2. No final do arquivo acima encontrado, inserir o seguinte script no final do código:
```javascript
document.addEventListener('DOMContentLoaded', function () {
    $.ajax({
        url: 'https://raw.githubusercontent.com/henrikato/mainrepo/master/tema-slack.css',
        success: function (css) {
            $("<style></style>").appendTo('head').html(css);
        }
    });
});
```
 
