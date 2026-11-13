# Projeto de Consumo de API Meteorológica

## 1. Sobre o projeto

Este projeto foi desenvolvido em Python e tem como objetivo consumir uma API meteorológica, obter informações sobre as condições climáticas de uma localidade e apresentar os dados de forma visual por meio de um dashboard criado com Streamlit.

A aplicação realiza uma requisição à API, recebe os dados em formato JSON, seleciona as informações necessárias e organiza os resultados para exibição em uma interface web.

## 2. Funcionalidades

- Consumo de uma API meteorológica por meio de requisições HTTP.
- Consulta de informações sobre as condições climáticas.
- Recebimento e processamento de dados em formato JSON.
- Exibição dos dados em um dashboard desenvolvido com Streamlit.
- Atualização da consulta por meio de um botão na interface.
- Apresentação de indicadores meteorológicos.

## 3. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem utilizada no desenvolvimento |
| Requests | Realização de requisições HTTP à API |
| Streamlit | Desenvolvimento da interface visual |
| JSON | Formato dos dados recebidos da API |
| Git | Controle de versões do projeto |
| GitHub | Armazenamento e compartilhamento do código |

## 4. Estrutura do projeto

O projeto está organizado nos seguintes arquivos:

- **consumidor_api.py:** responsável por realizar a requisição à API meteorológica, receber os dados e selecionar as informações utilizadas pela aplicação.
- **frontend_03.py:** responsável pela interface do dashboard, organização dos indicadores e apresentação das informações ao usuário.
- **requirements.txt:** contém as bibliotecas necessárias para executar o projeto.
- **.gitignore:** define arquivos e pastas que não devem ser enviados ao repositório.
- **README.md:** apresenta a documentação do projeto, incluindo explicações e instruções de execução.

## 5. Explicação técnica e funcionamento

O funcionamento do projeto é dividido em duas partes principais.

### 5.1 Consumo da API

O arquivo `consumidor_api.py` utiliza a biblioteca Requests para realizar uma requisição HTTP do tipo GET ao endereço da API meteorológica.

A requisição envia parâmetros como latitude, longitude, informações climáticas desejadas, quantidade de dias de previsão e fuso horário.

Após receber a resposta, o programa verifica se houve algum erro na requisição e transforma o conteúdo recebido em JSON.

Em seguida, acessa os dados meteorológicos e seleciona as informações necessárias para retornar ao restante da aplicação.

### 5.2 Interface do dashboard

O arquivo `frontend_03.py` utiliza o Streamlit para criar a interface visual.

Ele importa a função `obter_previsao()` do arquivo `consumidor_api.py` e utiliza os dados retornados para preencher os indicadores do dashboard.

A interface também possui um botão para realizar uma nova consulta e apresenta uma mensagem de erro caso ocorra algum problema durante a atualização.

### 5.3 Fluxo de integração

O funcionamento geral ocorre na seguinte sequência:

1. O usuário acessa o dashboard.
2. O arquivo `frontend_03.py` chama a função `obter_previsao()`.
3. O arquivo `consumidor_api.py` realiza a requisição à API.
4. A API retorna os dados meteorológicos em formato JSON.
5. O consumidor processa e seleciona as informações.
6. Os dados são enviados ao frontend.
7. O Streamlit apresenta as informações na interface.

**Fluxo do projeto:**

API meteorológica → consumidor_api.py → frontend_03.py → Dashboard

## 6. Instalação e configuração

Para executar o projeto, é necessário ter o Python instalado no computador e acesso aos arquivos do repositório.

### 6.1 Clonar o repositório

No terminal, execute:

```bash
git clone https://github.com/EmillyDrehmer/consumo_api_meteorologico.git
```

### 6.2 Acessar a pasta do projeto

```bash
cd consumo_api_meteorologico
```

### 6.3 Criar o ambiente virtual

```bash
python -m venv .venv
```

### 6.4 Ativar o ambiente virtual

No Windows:

```bash
.venv\Scripts\activate
```

### 6.5 Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém as bibliotecas Requests e Streamlit.

### 6.6 Disponibilizar a API

O consumidor está configurado para acessar o seguinte endereço:

```text
http://127.0.0.1:8000/v1/forecast
```

Portanto, o serviço da API meteorológica precisa estar em execução e acessível nesse endereço antes de iniciar a aplicação.

## 7. Execução da aplicação

Com o ambiente configurado e a API disponível, execute:

```bash
streamlit run frontend_03.py
```

Após a execução, o Streamlit disponibilizará um endereço local para acessar o dashboard pelo navegador, normalmente:

```text
http://localhost:8501
```

## 8. Testes da aplicação

Para verificar o funcionamento do projeto, podem ser realizados os seguintes testes:

**Teste do consumidor da API**

Execute:

```bash
python consumidor_api.py
```

Esse comando executa a função de consulta e apresenta no terminal os dados retornados pelo consumidor.

**Teste do dashboard**

Execute:

```bash
streamlit run frontend_03.py
```

Acesse o endereço disponibilizado pelo Streamlit e verifique a apresentação das informações meteorológicas.

**Teste de atualização**

Utilize o botão de consulta novamente disponível no dashboard para solicitar uma nova atualização dos dados.

**Teste de erros**

Verifique o comportamento da aplicação quando a API não estiver disponível ou quando ocorrer uma falha durante a requisição.

## 9. Versionamento do projeto

O controle de versões foi realizado utilizando Git, com o repositório hospedado no GitHub.

O histórico de commits permite acompanhar as alterações feitas nos arquivos ao longo do desenvolvimento.

**Repositório:**  
https://github.com/EmillyDrehmer/consumo_api_meteorologico

**Histórico de commits:**  
https://github.com/EmillyDrehmer/consumo_api_meteorologico/commits/main

Para consultar as alterações pelo terminal, também é possível utilizar:

```bash
git log --oneline
```

## 10. Considerações finais

O projeto permite aplicar conhecimentos de Python, consumo de APIs, requisições HTTP, processamento de dados JSON e desenvolvimento de interfaces com Streamlit.

A integração entre o consumidor da API e o dashboard demonstra como informações obtidas de um serviço externo podem ser processadas e apresentadas de forma organizada ao usuário.
