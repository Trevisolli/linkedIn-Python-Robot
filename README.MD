<p align="center">
  <a href="https://www.linkedin.com/in/Trevisolli">
    <img width="140" src="https://github.com/Trevisolli/linkedIn-Python-Robot/blob/master/images/04-LogoPythonLinkedIn.png"/>  
  </a>  
  <h2 align="center">Web Scraping no LinkedIn</h2>
  
   
  <p align="center">
  <a href="https://www.linkedin.com/in/Trevisolli">
    <img alt="Autor: Paulo Trevisolli" src="https://img.shields.io/badge/Autor-Paulo%20Trevisolli-green">
  </a>
  <img alt="Licença do Projeto" src="https://img.shields.io/badge/LICENSE-MIT-green"/>
<p>
  <p align="center">Repositório criado para manter os artefatos de resolução, ganho de conhecimento, de exercício de Python, realizando busca de vagas no LinkedIn.</p> 
  <p align="center"><b>(09/Janeiro/2023)</b></p>  
</p>


# Introdução 
Irei disponibilizar aqui os arquivos para reprodução e explicação dos principais assuntos para que o projeto funcione com sucesso.

Sugestões de melhoria, são sempre bem vindas!

## bibliotecas

Em anexo neste repositório, existe um arquivo, requirements.txt, que indica a lista de bibliotecas que utilizei, para que fosse obtido um resultado com sucesso. 


Para se instalar as demais bibliotecas, segue como exemplo, a instalação da bibiooteca <b>python-dotenv</b>, porém, se faz necessária a instalação das demais, citadas em <b> requirements.txt </b> etc:
```
pip install python-dotenv
```

## .env

Arquivo que especifica as características/propriedades para login no LinkedIN.
Este arquivo não é versionado, por conter informações sensíveis, dados sigilosos do teu login no LinkedIn.

Abaixo, segue a visualização do arquivo <b>.env</b> de exemplo, onde, as informações após o sinal de igual (=), são fictícias, devendo-se alterar para suas credenciais do LinkedIn.
<p align="center">
  <img width="250" src="https://github.com/Trevisolli/linkedIn-Python-Robot/blob/master/images/03-EnvFile.PNG"/>  
</p>

Lembrando que, este arquivo (<b>.env</b>) é essencial para que este projeto funcione corretamente, portanto, deve ser configurado exatamente de acordo com as suas credenciais do LinkedIN.

## <a href="https://github.com/Trevisolli/linkedIn-Python-Robot/blob/master/robo_linkedin.py">robo_linkedin.py</a>

Arquivo principal, que executa o processo de raspagem no LinkedIN. 
Resumidamente, ele executa as seguintes operações:
<ol>
  <li>Chama a página de Login do LinkedIN</li>
  <li>Caso existam registros nessas condições: </li>
  <li>Preenche os campos de Username e Password </li>
  <li>Clica em "Sign in"</li>
  <li>Clica em "Search" (Pesquisa) </li>
  <li>Escreve "Engenheiro de dados" e dá um Enter </li>
  <li>Clica em "Job" (Vagas) </li>
  <li>Faz um "loop" nas vagas da primeira página e, escreve um output no console.</li>  
</ol>

Imagem da execução do projeto (Pesquisa):

<p align="center">
  <img width="450" src="https://github.com/Trevisolli/linkedIn-Python-Robot/blob/master/images/01-Search.PNG"/>  
</p>

Produto final (Resultado):

<p align="center">
  <img width="250" src="https://github.com/Trevisolli/linkedIn-Python-Robot/blob/master/images/02-Results.PNG"/>  
</p>

