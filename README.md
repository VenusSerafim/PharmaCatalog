# 💊 PharmaCatalog

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)

**Sistema de Gerenciamento e Padronização de Informações Farmacêuticas**

## 1. Sobre o projeto

O PharmaCatalog é um sistema desenvolvido para organizar, padronizar e gerenciar informações farmacêuticas por meio de uma API REST.

Inicialmente, o projeto será direcionado ao cadastro e gerenciamento de medicamentos antimicrobianos, permitindo armazenar informações como nome genérico, nome comercial, concentração, apresentação farmacêutica, categoria e preço de aquisição.

A proposta é construir uma base de informações estruturada, facilitando a consulta, a atualização e a integração futura com outros sistemas de tecnologia em saúde.

O PharmaCatalog também possui potencial para atuar como serviço complementar ao Kronos AI, disponibilizando informações farmacêuticas padronizadas para aplicações que necessitem desses dados.

## 2. Problema identificado

Informações farmacêuticas podem estar distribuídas em diferentes fontes e formatos, dificultando sua organização, padronização e consulta.

A ausência de uma estrutura centralizada pode gerar inconsistências cadastrais, dificuldades na atualização de preços e problemas na integração entre diferentes aplicações.

O PharmaCatalog busca contribuir para a resolução desse problema por meio de uma API centralizada para gerenciamento de informações farmacêuticas.

## 3. Objetivos

- Desenvolver uma API REST para gerenciamento de medicamentos.
- Padronizar o armazenamento das informações farmacêuticas.
- Facilitar a consulta e a pesquisa de medicamentos.
- Permitir o gerenciamento de preços de aquisição.
- Preparar uma estrutura que permita futuras integrações com outros sistemas.
- Possibilitar a expansão do catálogo para outras categorias de medicamentos.

## 4. Funcionalidades

### Funcionalidades previstas para o MVP

| Funcionalidade | Descrição |
|---|---|
| Cadastro | Registrar novos medicamentos antimicrobianos. |
| Consulta | Consultar medicamentos individualmente. |
| Listagem | Visualizar os medicamentos cadastrados. |
| Atualização | Modificar informações dos registros. |
| Inativação | Inativar medicamentos sem excluir permanentemente seus dados. |
| Pesquisa | Pesquisar medicamentos pelo nome. |
| Filtragem | Filtrar por categoria, apresentação e concentração. |
| Gestão de preços | Cadastrar e atualizar preços de aquisição. |
| Consulta financeira | Consultar informações financeiras dos medicamentos. |

### Funcionalidades futuras

- Expansão para outras categorias de medicamentos.
- Integração com o Kronos AI.
- Histórico de alterações de preços.
- Autenticação e controle de acesso.
- Relatórios e indicadores financeiros.
- Ampliação dos mecanismos de pesquisa e filtragem.

## 5. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem de programação principal. |
| FastAPI | Desenvolvimento da API REST. |
| MongoDB | Banco de dados NoSQL. |
| Git | Controle de versão. |
| GitHub | Hospedagem do código e gerenciamento do projeto. |
| Swagger / OpenAPI | Documentação e exploração dos endpoints da API. |

## 6. Arquitetura prevista

O PharmaCatalog utilizará uma arquitetura baseada em API REST, separando as responsabilidades de recebimento de requisições, processamento das regras de negócio e persistência dos dados.

Fluxo simplificado:

```text
Cliente / Aplicação externa
           |
           v
       FastAPI
           |
           v
   Camada de aplicação
           |
           v
    Camada de dados
           |
           v
       MongoDB
```

A comunicação será realizada por meio de requisições HTTP, utilizando JSON para troca de informações.

## 7. Estrutura do projeto

```text
PharmaCatalog/
│
├── docs/
│   ├── project-charter.md
│   ├── requisitos.md
│   ├── casos-de-uso.md
│   └── user-stories.md
│
├── src/
│   ├── main.py
│   ├── config/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   └── services/
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 8. Instalação e execução

### Pré-requisitos

Antes de executar o projeto, será necessário possuir:

- Python instalado.
- MongoDB instalado ou uma instância MongoDB Atlas.
- Git instalado.
- Um ambiente de desenvolvimento, como Visual Studio Code.

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta

```bash
cd PharmaCatalog
```

### 3. Criar um ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Configurar as variáveis de ambiente

Criar um arquivo `.env` na raiz do projeto, utilizando o `.env.example` como referência.

Exemplo:

```env
MONGODB_URI=mongodb://localhost:27017
DATABASE_NAME=pharmacatalog
```

### 7. Executar a aplicação

Quando a estrutura inicial da API estiver implementada:

```bash
uvicorn src.main:app --reload
```

### 8. Acessar a documentação da API

Após iniciar a aplicação:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 9. Documentação do projeto

A documentação técnica e de planejamento está disponível na pasta `docs/`.

| Documento | Descrição |
|---|---|
| [Project Charter](docs/project-charter.md) | Apresentação, justificativa, objetivos e escopo. |
| [Requisitos](docs/requisitos.md) | Requisitos funcionais, não funcionais e regras de negócio. |
| [Casos de Uso](docs/casos-de-uso.md) | Interações e fluxos de utilização do sistema. |
| [Histórias de Usuário](docs/user-stories.md) | Necessidades dos usuários e critérios de aceitação. |

## 10. Gerenciamento do projeto

O desenvolvimento será organizado utilizando Git Flow, com separação entre as branches principais e as branches de funcionalidades.

Branches principais:

- `main`: versão estável do projeto.
- `develop`: integração das funcionalidades em desenvolvimento.
- `feature/nome-da-funcionalidade`: implementação de novas funcionalidades.

O projeto também utilizará:

- Conventional Commits para padronização das mensagens de commit.
- GitHub Issues para organização das tarefas.
- Pull Requests para revisão e integração de código.
- Tags SemVer para identificação de versões.

## 11. Segurança e responsabilidade

O PharmaCatalog tem como finalidade organizar e disponibilizar informações farmacêuticas.

A aplicação não tem como objetivo realizar prescrições, recomendar tratamentos, modificar terapias ou tomar decisões clínicas automatizadas.

Os dados utilizados durante o desenvolvimento inicial serão dados fictícios ou demonstrativos, sem utilização de informações pessoais de pacientes.

## 12. Status do projeto

**Em desenvolvimento.**

O projeto encontra-se na etapa de planejamento e estruturação técnica. As funcionalidades descritas representam o escopo previsto para o MVP, não necessariamente recursos já implementados.

## 13. Licença

Licença ainda não definida.
