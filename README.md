💊 PharmaCatalog







Sistema de Gerenciamento e Padronização de Informações Farmacêuticas

Sobre o projeto

O PharmaCatalog é uma API REST desenvolvida para organizar, padronizar e gerenciar informações farmacêuticas.

O projeto tem como foco inicial o cadastro e o gerenciamento de medicamentos antimicrobianos, armazenando informações como nome genérico, nome comercial, concentração, apresentação farmacêutica, categoria e preço de aquisição.

A proposta é oferecer uma estrutura centralizada para consulta e atualização desses dados, facilitando futuras integrações com outros sistemas de tecnologia em saúde.

O PharmaCatalog também possui potencial para atuar como serviço complementar ao Kronos AI, disponibilizando informações farmacêuticas padronizadas para aplicações que necessitem desses dados.

Problema identificado

Informações farmacêuticas podem estar distribuídas em diferentes fontes e formatos, dificultando sua organização, padronização e consulta.

A ausência de uma estrutura centralizada pode gerar inconsistências cadastrais, dificuldades na atualização de preços e problemas na integração entre diferentes aplicações.

O PharmaCatalog busca contribuir para a resolução desse problema por meio de uma API centralizada para gerenciamento de informações farmacêuticas.

Objetivos

Desenvolver uma API REST para gerenciamento de medicamentos.

Padronizar o armazenamento das informações farmacêuticas.

Facilitar a consulta e a pesquisa de medicamentos.

Permitir o gerenciamento de preços de aquisição.

Preparar uma estrutura que permita futuras integrações com outros sistemas.

Possibilitar a expansão do catálogo para outras categorias de medicamentos.

Funcionalidades

Implementadas

Cadastro de medicamentos.

Listagem de medicamentos.

Consulta individual de medicamentos por ID.

Atualização de informações cadastrais.

Inativação de medicamentos.

Pesquisa por nome genérico e nome comercial.

Verificação da disponibilidade da API.

Verificação da conexão com o banco de dados.

Testes automatizados das principais operações e respostas da API.

Planejadas

Filtros por apresentação farmacêutica.

Filtros por categoria.

Filtros por concentração.

Consulta financeira estruturada.

Paginação da listagem.

Ampliação da validação dos dados cadastrais.

Padronização adicional das respostas.

Melhorias de desempenho nas consultas ao MongoDB.

Ampliação da cobertura de testes.

Tecnologias utilizadas

Tecnologia

Finalidade

Python 3.12

Linguagem de programação

FastAPI

Desenvolvimento da API REST

MongoDB

Banco de dados NoSQL

PyMongo

Comunicação com o MongoDB

Pydantic

Validação e estruturação de dados

Pytest

Testes automatizados

Git

Controle de versão

GitHub

Hospedagem e gerenciamento do projeto

Swagger / OpenAPI

Documentação e exploração dos endpoints

Endpoints da API

A API disponibiliza atualmente os seguintes endpoints:

Método

Rota

Descrição

GET

/

Informações básicas da API

GET

/health

Verificação de disponibilidade

GET

/health/database

Verificação da conexão com o banco

POST

/medicamentos/

Cadastro de medicamento

GET

/medicamentos/

Listagem de medicamentos

GET

/medicamentos/buscar

Pesquisa por nome

GET

/medicamentos/{medication_id}

Consulta por ID

PUT

/medicamentos/{medication_id}

Atualização de medicamento

PATCH

/medicamentos/{medication_id}/inativar

Inativação de medicamento

A documentação interativa pode ser acessada pelo Swagger UI após iniciar a aplicação.

Arquitetura

O PharmaCatalog utiliza uma arquitetura baseada em API REST, separando as responsabilidades de recebimento de requisições, processamento e persistência dos dados.

Fluxo simplificado:

Cliente / Aplicação externa
           |
           v
         FastAPI
           |
           v
     Rotas da aplicação
           |
           v
       MongoDB

A comunicação ocorre por meio de requisições HTTP, utilizando JSON para troca de informações.

Estrutura do projeto

PharmaCatalog/
│
├── docs/
│   ├── project-charter.md
│   ├── requisitos.md
│   ├── casos-de-uso.md
│   └── user-stories.md
│
├── src/
│   ├── __init__.py
│   ├── config/
│   ├── database/
│   ├── routes/
│   ├── schemas/
│   └── main.py
│
├── tests/
│   ├── .gitkeep
│   └── test_api.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

Instalação e execução

Pré-requisitos

Python 3.12 ou superior compatível com as dependências.

MongoDB instalado localmente ou uma instância MongoDB Atlas.

Git instalado.

Um editor de código, como Visual Studio Code.

1. Clonar o repositório

git clone https://github.com/VenusSerafim/PharmaCatalog.git

2. Entrar na pasta

cd PharmaCatalog

3. Criar um ambiente virtual

python -m venv .venv

4. Ativar o ambiente virtual

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Linux / macOS:

source .venv/bin/activate

5. Instalar as dependências

pip install -r requirements.txt

6. Configurar as variáveis de ambiente

Crie um arquivo .env na raiz do projeto, utilizando o .env.example como referência.

Configure a URI de conexão e o nome do banco de dados conforme as variáveis esperadas pela aplicação.

Não compartilhe credenciais ou informações sensíveis no repositório.

7. Executar a aplicação

uvicorn src.main:app --reload

8. Acessar a documentação

Após iniciar a aplicação:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Testes automatizados

O projeto utiliza Pytest para verificar o comportamento dos endpoints e suas respostas.

Para executar os testes:

python -m pytest -v

Na última execução registrada, foram aprovados 9 testes automatizados.

Os testes atuais utilizam estruturas simuladas para verificar os comportamentos da API, não representando uma bateria completa de testes de integração com um MongoDB real.

Documentação do projeto

A documentação técnica e de planejamento está disponível na pasta docs/.

Documento

Descrição

Project Charter

Apresentação, justificativa, objetivos e escopo

Requisitos

Requisitos funcionais, não funcionais e regras de negócio

Casos de Uso

Interações e fluxos de utilização do sistema

Histórias de Usuário

Necessidades dos usuários e critérios de aceitação

Gerenciamento do projeto

O desenvolvimento é organizado utilizando um fluxo de trabalho inspirado no Git Flow.

Branches principais:

main: versão estável do projeto.

develop: integração das funcionalidades em desenvolvimento.

feature/nome-da-funcionalidade: implementação de novas funcionalidades.

docs/nome-da-documentacao: alterações na documentação.

fix/nome-da-correcao: correções.

O projeto também utiliza:

Conventional Commits para padronização das mensagens de commit.

GitHub Issues para organização e rastreabilidade das tarefas.

Pull Requests para revisão e integração de código.

Tags SemVer para identificação de versões.

As funcionalidades são desenvolvidas em branches específicas e integradas à develop por meio de Pull Requests.

Segurança e responsabilidade

O PharmaCatalog tem como finalidade organizar e disponibilizar informações farmacêuticas.

A aplicação não tem como objetivo realizar prescrições, recomendar tratamentos, modificar terapias ou tomar decisões clínicas automatizadas.

Os dados utilizados durante o desenvolvimento inicial devem ser fictícios ou demonstrativos, sem utilização de informações pessoais de pacientes.

Status do projeto

Em desenvolvimento.

A API já possui uma estrutura funcional, endpoints implementados para gerenciamento de medicamentos e testes automatizados. Novas funcionalidades, melhorias e documentação continuam sendo desenvolvidas e organizadas por meio de Issues e Pull Requests.

Licença

Licença ainda não definida.