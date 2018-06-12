# mainrepo

Repositório principal onde armazeno (quase) todos os arquivos, programas e códigos desenvolvidos por mim (e alguns com a ajuda de outros contribuidores colegas de faculdade e amigos) na faculdade ou no tempo livre.

------------------------------------------------------------------------------------------------------------------------------------------
### Como usar o `tema-slack.css`
Criei este arquivo para utilizar como um tema customizado do aplicativo para Desktop do Slack.
#### Passo-a-passo:
##### 1. Procurar o arquivo `ssb-interop.js`
   Caminho do arquivo no Windows: `%homepath%\AppData\Local\slack\app-x.x.x\resources\app.asar.unpacked\src\static\ssb-interop.js`
   Caminho do arquivo no macOS: `/Applications/Slack.app/Contents/Resources/app.asar.unpacked/src`
   (procurar sempre a pasta app-* mais recente, exemplo: `\app-3.2.0\`)

##### 2. No final do arquivo acima encontrado, inserir o seguinte script no final do código:
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
 
