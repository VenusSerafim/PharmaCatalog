Histórias de Usuário — PharmaCatalog
US01 — Cadastrar antimicrobiano
Como administrador do catálogo,
quero cadastrar novos antimicrobianos,
para manter uma base organizada e padronizada de medicamentos.
Prioridade: Alta
Requisitos relacionados: RF01
Caso de uso relacionado: UC01
Critérios de aceitação
Cenário 1 — Cadastro realizado com sucesso
Dado que o administrador esteja realizando um novo cadastro;
E que os campos obrigatórios estejam preenchidos corretamente;
Quando solicitar o cadastro do antimicrobiano;
Então o sistema deverá validar as informações;
E registrar o medicamento no banco de dados;
E retornar uma confirmação da operação.
Cenário 2 — Cadastro com informações obrigatórias ausentes
Dado que o administrador esteja preenchendo um cadastro;
Quando deixar de informar um campo obrigatório;
Então o sistema deverá rejeitar a solicitação;
E informar quais campos precisam ser preenchidos.
Cenário 3 — Cadastro com preço negativo
Dado que o administrador esteja cadastrando um antimicrobiano;
Quando informar um preço de aquisição negativo;
Então o sistema deverá rejeitar o valor;
E apresentar uma mensagem de validação.

US02 — Consultar medicamento por identificador
Como administrador do catálogo,
quero consultar um medicamento utilizando seu identificador,
para visualizar suas informações individualmente.
Prioridade: Alta
Requisitos relacionados: RF02
Caso de uso relacionado: UC03
Critérios de aceitação
Cenário 1 — Medicamento encontrado
Dado que exista um medicamento cadastrado;
Quando o administrador informar um identificador válido;
Então o sistema deverá localizar o registro;
E apresentar suas informações.
Cenário 2 — Medicamento inexistente
Dado que o identificador informado não corresponda a nenhum registro;
Quando o administrador realizar a consulta;
Então o sistema deverá informar que o medicamento não foi encontrado.
Cenário 3 — Identificador inválido
Dado que o administrador informe um identificador em formato inválido;
Quando solicitar a consulta;
Então o sistema deverá retornar uma mensagem de erro apropriada.

US03 — Listar medicamentos cadastrados
Como administrador do catálogo,
quero visualizar os medicamentos cadastrados,
para acompanhar os registros disponíveis no sistema.
Prioridade: Alta
Requisitos relacionados: RF03
Caso de uso relacionado: UC02
Critérios de aceitação
Cenário 1 — Listagem de medicamentos ativos
Dado que existam medicamentos ativos cadastrados;
Quando o administrador solicitar a listagem;
Então o sistema deverá retornar os medicamentos ativos.
Cenário 2 — Catálogo vazio
Dado que não existam medicamentos cadastrados;
Quando o administrador solicitar a listagem;
Então o sistema deverá retornar uma lista vazia;
E informar que não existem registros disponíveis.
Cenário 3 — Consulta de registros inativos
Dado que existam medicamentos inativos;
Quando o administrador solicitar explicitamente a consulta desses registros;
Então o sistema deverá apresentar os medicamentos inativos.

US04 — Atualizar informações de medicamento
Como administrador do catálogo,
quero atualizar as informações de um medicamento,
para manter os registros corretos e atualizados.
Prioridade: Alta
Requisitos relacionados: RF04
Caso de uso relacionado: UC04
Critérios de aceitação
Cenário 1 — Atualização realizada com sucesso
Dado que exista um medicamento cadastrado;
Quando o administrador alterar uma ou mais informações válidas;
Então o sistema deverá salvar as modificações;
E atualizar a data de modificação do registro.
Cenário 2 — Atualização parcial
Dado que o administrador queira modificar apenas um campo;
Quando enviar a alteração;
Então o sistema deverá modificar somente o campo informado;
E preservar as demais informações.
Cenário 3 — Atualização de medicamento inexistente
Dado que o identificador informado não corresponda a um medicamento;
Quando o administrador solicitar a atualização;
Então o sistema deverá informar que o registro não foi encontrado.

US05 — Inativar medicamento
Como administrador do catálogo,
quero inativar um medicamento,
para impedir que registros desatualizados ou indisponíveis apareçam nas consultas convencionais sem perder seu histórico.
Prioridade: Alta
Requisitos relacionados: RF05
Caso de uso relacionado: UC05
Critérios de aceitação
Cenário 1 — Inativação realizada com sucesso
Dado que exista um medicamento ativo;
Quando o administrador solicitar sua inativação;
Então o sistema deverá alterar seu status para inativo;
E preservar o registro no banco de dados.
Cenário 2 — Medicamento inativo na listagem convencional
Dado que um medicamento esteja inativo;
Quando o administrador solicitar a listagem padrão;
Então o sistema não deverá apresentar esse registro.
Cenário 3 — Inativação de registro já inativo
Dado que o medicamento já esteja inativo;
Quando o administrador solicitar novamente sua inativação;
Então o sistema deverá informar que o registro já está inativo.

US06 — Pesquisar medicamento por nome
Como administrador do catálogo,
quero pesquisar medicamentos pelo nome genérico ou comercial,
para localizar rapidamente os registros desejados.
Prioridade: Alta
Requisitos relacionados: RF06
Caso de uso relacionado: UC06
Critérios de aceitação
Cenário 1 — Pesquisa por nome completo
Dado que exista um medicamento cadastrado;
Quando o administrador pesquisar pelo nome completo;
Então o sistema deverá retornar o registro correspondente.
Cenário 2 — Pesquisa por parte do nome
Dado que existam medicamentos com nomes correspondentes ao termo pesquisado;
Quando o administrador informar apenas parte do nome;
Então o sistema deverá retornar os registros compatíveis.
Cenário 3 — Pesquisa sem resultados
Dado que não existam medicamentos correspondentes ao termo informado;
Quando o administrador realizar a pesquisa;
Então o sistema deverá informar que nenhum resultado foi encontrado.

US07 — Filtrar por apresentação
Como administrador do catálogo,
quero filtrar os medicamentos por apresentação farmacêutica,
para localizar produtos com características específicas.
Prioridade: Média
Requisitos relacionados: RF07
Caso de uso relacionado: UC07
Critérios de aceitação
Cenário 1 — Filtro com resultados
Dado que existam medicamentos com diferentes apresentações;
Quando o administrador selecionar uma apresentação;
Então o sistema deverá retornar somente os registros correspondentes.
Cenário 2 — Filtro sem resultados
Dado que não existam medicamentos com a apresentação selecionada;
Quando o administrador aplicar o filtro;
Então o sistema deverá informar que nenhum registro foi encontrado.

US08 — Filtrar por categoria
Como administrador do catálogo,
quero filtrar medicamentos por categoria,
para organizar e localizar registros de acordo com sua classificação.
Prioridade: Média
Requisitos relacionados: RF08
Caso de uso relacionado: UC07
Critérios de aceitação
Cenário 1 — Categoria existente
Dado que existam medicamentos associados a uma categoria;
Quando o administrador selecionar essa categoria;
Então o sistema deverá apresentar os medicamentos correspondentes.
Cenário 2 — Categoria sem registros
Dado que não existam medicamentos associados à categoria selecionada;
Quando o administrador aplicar o filtro;
Então o sistema deverá retornar uma lista vazia.

US09 — Filtrar por concentração
Como administrador do catálogo,
quero filtrar medicamentos por concentração,
para localizar apresentações com concentrações específicas.
Prioridade: Média
Requisitos relacionados: RF09
Caso de uso relacionado: UC07
Critérios de aceitação
Cenário 1 — Concentração correspondente
Dado que existam medicamentos cadastrados com diferentes concentrações;
Quando o administrador selecionar uma concentração;
Então o sistema deverá retornar os registros correspondentes.
Cenário 2 — Concentração inexistente
Dado que não existam registros com a concentração selecionada;
Quando o administrador aplicar o filtro;
Então o sistema deverá informar que nenhum resultado foi encontrado.

US10 — Cadastrar preço de aquisição
Como administrador do catálogo,
quero cadastrar o preço de aquisição de um medicamento,
para manter informações financeiras associadas aos registros farmacêuticos.
Prioridade: Alta
Requisitos relacionados: RF10
Caso de uso relacionado: UC08
Critérios de aceitação
Cenário 1 — Cadastro de preço válido
Dado que exista um medicamento cadastrado;
Quando o administrador informar um preço válido e sua moeda;
Então o sistema deverá associar as informações financeiras ao medicamento.
Cenário 2 — Preço negativo
Dado que o administrador esteja cadastrando um preço;
Quando informar um valor negativo;
Então o sistema deverá rejeitar a operação.
Cenário 3 — Moeda não informada
Dado que o administrador informe um preço;
Quando deixar de informar a moeda;
Então o sistema deverá solicitar o preenchimento desse campo.

US11 — Atualizar preço de aquisição
Como administrador do catálogo,
quero atualizar o preço de aquisição de um medicamento,
para manter os valores financeiros atualizados.
Prioridade: Alta
Requisitos relacionados: RF11
Caso de uso relacionado: UC09
Critérios de aceitação
Cenário 1 — Atualização de preço
Dado que um medicamento possua um preço cadastrado;
Quando o administrador informar um novo preço válido;
Então o sistema deverá atualizar o valor armazenado;
E confirmar a operação.
Cenário 2 — Novo preço inválido
Dado que o administrador esteja atualizando um preço;
Quando informar um valor negativo;
Então o sistema deverá rejeitar a alteração.
Cenário 3 — Medicamento inexistente
Dado que o medicamento não esteja cadastrado;
Quando o administrador tentar atualizar seu preço;
Então o sistema deverá informar que o registro não foi encontrado.

US12 — Consultar informações financeiras
Como administrador do catálogo,
quero consultar as informações financeiras de um medicamento,
para visualizar seu preço de aquisição e a moeda utilizada.
Prioridade: Média
Requisitos relacionados: RF12
Caso de uso relacionado: UC10
Critérios de aceitação
Cenário 1 — Informações financeiras disponíveis
Dado que um medicamento possua informações financeiras cadastradas;
Quando o administrador solicitar a consulta;
Então o sistema deverá apresentar o preço e a moeda correspondente.
Cenário 2 — Preço não cadastrado
Dado que o medicamento não possua preço registrado;
Quando o administrador solicitar a consulta financeira;
Então o sistema deverá informar que não existem informações financeiras disponíveis.

3. Considerações sobre as histórias de usuário
As histórias apresentadas representam as funcionalidades previstas para a primeira versão do PharmaCatalog.
As prioridades foram definidas considerando a importância de cada funcionalidade para o funcionamento do MVP:
Alta: funcionalidades essenciais para o gerenciamento do catálogo.
Média: funcionalidades que complementam a organização e a consulta dos dados.
4. Rastreabilidade
História
Requisitos
Caso de uso
US01
RF01
UC01
US02
RF02
UC03
US03
RF03
UC02
US04
RF04
UC04
US05
RF05
UC05
US06
RF06
UC06
US07
RF07
UC07
US08
RF08
UC07
US09
RF09
UC07
US10
RF10
UC08
US11
RF11
UC09
US12
RF12
UC10

5. Considerações finais
As histórias de usuário e seus critérios de aceitação servirão como referência para a implementação e os testes do PharmaCatalog.
Cada história poderá ser transformada em uma ou mais tarefas de desenvolvimento no GitHub, permitindo acompanhar o progresso do projeto e verificar se as funcionalidades foram implementadas conforme o esperado.


