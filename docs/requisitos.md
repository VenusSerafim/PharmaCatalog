PharmaCatalog
Requisitos Funcionais e Não Funcionais
Versão: 0.1.0
Status: Em desenvolvimento
Tecnologias: Python, FastAPI e MongoDB
Categoria inicial: Gerenciamento de antimicrobianos

1. Introdução
Este documento apresenta os requisitos funcionais e não funcionais do PharmaCatalog, estabelecendo as funcionalidades, restrições e características de qualidade esperadas para a primeira versão do sistema.
O PharmaCatalog será desenvolvido como uma API REST destinada ao gerenciamento e à padronização de informações farmacêuticas, inicialmente concentrada em antimicrobianos.
Os requisitos aqui definidos servirão como referência para o desenvolvimento, os testes e a criação das Issues no GitHub.
2. Requisitos Funcionais (RF)
Os requisitos funcionais descrevem as operações que o sistema deverá disponibilizar aos seus usuários ou sistemas integrados.
2.1. Gerenciamento de medicamentos
[RF01] Cadastrar antimicrobianos
O sistema deverá permitir cadastrar novos antimicrobianos, armazenando suas informações de identificação e características farmacêuticas.
[RF02] Consultar antimicrobianos
O sistema deverá permitir consultar individualmente os medicamentos cadastrados, utilizando um identificador único.
[RF03] Listar antimicrobianos
O sistema deverá disponibilizar uma listagem dos medicamentos registrados no banco de dados.
[RF04] Atualizar informações
O sistema deverá permitir atualizar as informações cadastrais de um medicamento existente.
[RF05] Inativar medicamentos
O sistema deverá permitir inativar registros sem necessariamente excluir seus dados permanentemente.
2.2. Pesquisa e organização
[RF06] Pesquisar por nome
O sistema deverá permitir localizar medicamentos utilizando seu nome genérico ou denominação cadastrada.
[RF07] Filtrar por apresentação
O sistema deverá permitir filtrar medicamentos conforme sua apresentação farmacêutica.
[RF08] Filtrar por categoria
O sistema deverá permitir organizar e consultar medicamentos conforme categorias previamente cadastradas.
[RF09] Consultar por concentração
O sistema deverá permitir localizar medicamentos conforme sua concentração registrada.
2.3. Gerenciamento financeiro
[RF10] Registrar preços
O sistema deverá permitir cadastrar o preço de aquisição associado a um medicamento e à sua apresentação.
[RF11] Atualizar preços
O sistema deverá permitir atualizar os preços cadastrados, preservando a integridade das informações.
[RF12] Consultar informações financeiras
O sistema deverá disponibilizar os preços registrados para consulta por usuários ou aplicações autorizadas.
3. Requisitos Não Funcionais (RNF)
Os requisitos não funcionais estabelecem condições de qualidade e funcionamento que deverão ser respeitadas pela aplicação.
3.1. Desempenho
[RNF01] Tempo de resposta
A API deverá responder às operações comuns de consulta em até 2 segundos em condições normais de utilização e com volume de dados de teste definido.
[RNF02] Organização das consultas
O sistema deverá utilizar mecanismos adequados de consulta e indexação no MongoDB para facilitar a recuperação dos registros.
3.2. Segurança
[RNF03] Validação de dados
O sistema deverá validar os dados recebidos antes de armazená-los no banco de dados.
[RNF04] Proteção de acesso
A arquitetura deverá permitir a implementação de autenticação e autorização para operações administrativas.
[RNF05] Proteção das informações
O sistema deverá evitar a exposição de credenciais, configurações privadas e informações sensíveis em respostas da API ou no repositório.
3.3. Persistência e integridade
[RNF06] Persistência dos registros
As informações cadastradas deverão permanecer armazenadas no MongoDB, mesmo após o encerramento e reinicialização da aplicação.
[RNF07] Integridade cadastral
O sistema deverá impedir o armazenamento de registros que não atendam às regras de validação estabelecidas.
[RNF08] Identificação única
Cada medicamento cadastrado deverá possuir um identificador único.
3.4. Usabilidade e documentação
[RNF09] Documentação da API
A aplicação deverá disponibilizar documentação interativa dos endpoints utilizando os recursos do FastAPI, como Swagger UI.
[RNF10] Padronização das respostas
A API deverá apresentar respostas estruturadas e consistentes, incluindo mensagens de erro compreensíveis.
3.5. Portabilidade e manutenção
[RNF11] Organização do código
O código-fonte deverá ser organizado em módulos com responsabilidades separadas, facilitando sua manutenção e expansão.
[RNF12] Configuração do ambiente
As configurações de conexão com o MongoDB deverão ser externas ao código-fonte, utilizando variáveis de ambiente.
[RNF13] Expansibilidade
A estrutura deverá permitir a inclusão futura de outras categorias de medicamentos sem exigir a reconstrução completa da aplicação.
4. Regras de Negócio (RN)
As regras de negócio complementam os requisitos e estabelecem condições específicas para o funcionamento do PharmaCatalog.
[RN01] Todo medicamento deverá possuir um identificador único.
[RN02] O nome genérico do medicamento será obrigatório.
[RN03] A concentração deverá ser registrada com seu respectivo valor e unidade de medida.
[RN04] A apresentação farmacêutica deverá ser informada no cadastro.
[RN05] Os preços deverão possuir valores numéricos não negativos e moeda identificada.
[RN06] A inativação de um medicamento não deverá apagar seu histórico cadastral.
[RN07] Medicamentos inativos não deverão aparecer na listagem padrão, salvo quando solicitada sua inclusão.
[RN08] A inclusão de novos grupos de medicamentos deverá respeitar a estrutura de padronização adotada pelo sistema.
5. Dados principais do sistema
Na primeira versão, cada medicamento deverá possuir os seguintes campos:
Campo
Descrição
id
Identificador único
nome_generico
Nome genérico do medicamento
nome_comercial
Nome comercial, quando aplicável
categoria
Categoria farmacológica
concentracao
Valor e unidade da concentração
apresentacao
Forma de apresentação farmacêutica
unidade_medida
Unidade utilizada no cadastro
preco_aquisicao
Preço registrado
moeda
Moeda utilizada
status
Ativo ou inativo
data_criacao
Data de criação do registro
data_atualizacao
Última atualização

6. Rastreabilidade dos requisitos
Os requisitos deverão ser utilizados como referência para a criação das tarefas de desenvolvimento e testes.
Requisito
Funcionalidade relacionada
RF01
Cadastro
RF02
Consulta individual
RF03
Listagem
RF04
Atualização
RF05
Inativação
RF06–RF09
Pesquisa e filtros
RF10–RF12
Gerenciamento financeiro
RNF01–RNF02
Desempenho
RNF03–RNF05
Segurança
RNF06–RNF08
Persistência e integridade
RNF09–RNF10
Documentação e respostas
RNF11–RNF13
Manutenção e expansão

7. Considerações finais
Os requisitos apresentados estabelecem a base funcional e técnica da primeira versão do PharmaCatalog.
Durante o desenvolvimento, eles poderão ser refinados conforme novas necessidades sejam identificadas, mantendo a rastreabilidade entre documentação, implementação, testes e Issues do GitHub.
O projeto deverá priorizar a organização dos dados, a consistência cadastral e a possibilidade de integração futura com o Kronos AI.
Documento: Requisitos Funcionais e Não Funcionais
Projeto: PharmaCatalog
Versão documental: 0.1.0


