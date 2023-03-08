Script para validação de CPF e CNPJ. Construído em Python 3.10

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/Felipedjn/validador_pfpj/blob/main/LICENSE)

## Instalação
Instalar usando pip
- pip install validate-docbr
- pip install colorama

## Uso
No arquivo "dados.txt" ficará os documentos a ser validados

![image](https://user-images.githubusercontent.com/114688883/223730263-690e9d7c-7630-4bc5-89ed-b63756560b2e.png)

Após isso, Execute o script.

O script irá retirar todos os documentos duplicados, caso tenha.

Caso todos os documentos sejam validos, iram aparecer no print

![image](https://user-images.githubusercontent.com/114688883/223731591-7a5f5837-6b82-4fe1-a583-627679ea088e.png)

no arquivo "saida.txt" irá aparecer "documento;tipo do documento"

![image](https://user-images.githubusercontent.com/114688883/223730682-b65db3e5-deec-4e5d-94fd-0f31f466e4a0.png)


Caso tenha algum documento inválido, o documento inválido ira aparecer no print:

![image](https://user-images.githubusercontent.com/114688883/223732385-da1db2f8-f9b5-4a77-b5ba-69c4bc6b222e.png)

e o mesmo será salvo no arquivo "dados_erro.txt"

![image](https://user-images.githubusercontent.com/114688883/223732835-3c1af254-3c55-4b40-bded-cb9b374b5664.png)
