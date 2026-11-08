Casos de Uso — PharmaCatalog
1. Introdução
Este documento apresenta os casos de uso do PharmaCatalog, um sistema destinado ao gerenciamento e à padronização de informações farmacêuticas, inicialmente voltado para medicamentos antimicrobianos.
Os casos de uso descrevem as interações entre os usuários e o sistema, especificando os fluxos principais, alternativos e excepcionais de cada funcionalidade.
O objetivo é representar o comportamento esperado da aplicação e estabelecer uma ligação entre os requisitos funcionais e as operações que serão implementadas.
2. Atores do sistema
Um ator representa uma pessoa, organização ou sistema externo que interage com a aplicação.
Ator
Descrição
Responsabilidades
Administrador do catálogo
Responsável pela manutenção das informações farmacêuticas.
Cadastrar, consultar, atualizar e inativar medicamentos.
Sistema PharmaCatalog
A própria aplicação, responsável por processar as solicitações.
Validar informações, consultar o banco de dados e retornar respostas.
Sistema externo
Aplicação que poderá consumir os dados disponibilizados pelo PharmaCatalog.
Consultar informações por meio da API, em uma futura integração.

Observação: a integração com sistemas externos, incluindo o Kronos AI, não faz parte da implementação inicial. Ela representa uma possibilidade de expansão futura.
3. Diagrama geral de casos de uso
O diagrama abaixo representa as principais funcionalidades disponíveis para o administrador do catálogo.
flowchart LR
    A[Administrador do catálogo]

    subgraph P[PharmaCatalog]
        UC1((Cadastrar antimicrobiano))
        UC2((Listar medicamentos))
        UC3((Consultar medicamento))
        UC4((Atualizar medicamento))
        UC5((Inativar medicamento))
        UC6((Pesquisar por nome))
        UC7((Filtrar medicamentos))
        UC8((Cadastrar preço))
        UC9((Atualizar preço))
        UC10((Consultar informações financeiras))
    end

    A --> UC1
    A --> UC2
    A --> UC3
    A --> UC4
    A --> UC5
    A --> UC6
    A --> UC7
    A --> UC8
    A --> UC9
    A --> UC10
4. Especificação dos casos de uso
UC01 — Cadastrar antimicrobiano
Objetivo: permitir que o administrador registre um novo antimicrobiano no catálogo.
Ator principal: Administrador do catálogo.
Pré-condições: o sistema deve estar disponível.
Gatilho: o administrador solicita o cadastro de um novo medicamento.
Requisitos relacionados: RF01.
Fluxo principal:
O administrador solicita o cadastro de um antimicrobiano.
O sistema apresenta os campos necessários.
O administrador informa os dados do medicamento.
O sistema verifica se os campos obrigatórios foram preenchidos.
O sistema valida os formatos e os valores informados.
O sistema verifica a consistência das informações.
O sistema gera um identificador único.
O sistema registra o medicamento no MongoDB.
O sistema confirma o cadastro.
Fluxos alternativos:
A1 — Nome comercial não informado: o sistema permite continuar caso o nome genérico esteja preenchido, pois o nome comercial não é obrigatório.
A2 — Medicamento com outra apresentação: o sistema permite cadastrar outra apresentação do mesmo princípio ativo, desde que seja um registro distinto.
Fluxos de exceção:
E1 — Campo obrigatório ausente: o sistema informa qual campo precisa ser preenchido.
E2 — Concentração inválida: o sistema rejeita valores ou unidades incompatíveis com o formato esperado.
E3 — Falha no banco de dados: o sistema informa que não foi possível concluir o cadastro.
Pós-condição: o medicamento fica registrado no catálogo com status ativo.
UC02 — Listar medicamentos
Objetivo: apresentar os medicamentos cadastrados no catálogo.
Ator principal: Administrador do catálogo.
Pré-condições: o sistema deve estar disponível.
Gatilho: o administrador solicita a listagem.
Requisitos relacionados: RF03.
Fluxo principal:
O administrador solicita a listagem de medicamentos.
O sistema consulta os registros no MongoDB.
O sistema recupera os medicamentos ativos.
O sistema organiza os resultados.
O sistema apresenta a lista ao administrador.
Fluxos alternativos:
A1 — Nenhum medicamento cadastrado: o sistema apresenta uma mensagem informando que não existem registros disponíveis.
A2 — Solicitação de registros inativos: o sistema permite consultar os registros inativos quando essa opção for solicitada.
Fluxos de exceção:
E1 — Falha na consulta: o sistema informa que não foi possível recuperar os registros.
Pós-condição: os medicamentos encontrados são apresentados sem modificar os dados armazenados.
UC03 — Consultar medicamento por identificador
Objetivo: permitir a consulta individual de um medicamento cadastrado.
Ator principal: Administrador do catálogo.
Pré-condições: o medicamento deve estar cadastrado.
Gatilho: o administrador informa o identificador do medicamento.
Requisitos relacionados: RF02.
Fluxo principal:
O administrador informa o identificador.
O sistema recebe a solicitação.
O sistema pesquisa o registro correspondente no MongoDB.
O sistema recupera as informações.
O sistema apresenta os dados do medicamento.
Fluxos alternativos:
A1 — Medicamento inativo: o sistema apresenta o registro, identificando seu status como inativo.
Fluxos de exceção:
E1 — Identificador inválido: o sistema informa que o formato do identificador é inválido.
E2 — Registro inexistente: o sistema informa que não encontrou medicamento correspondente.
Pós-condição: as informações do medicamento são exibidas sem alteração no banco de dados.
UC04 — Atualizar informações do medicamento
Objetivo: permitir a alteração de informações de um medicamento já cadastrado.
Ator principal: Administrador do catálogo.
Pré-condições: o medicamento deve existir no catálogo.
Gatilho: o administrador solicita a atualização de um registro.
Requisitos relacionados: RF04.
Fluxo principal:
O administrador informa o identificador do medicamento.
O sistema localiza o registro.
O sistema apresenta as informações atuais.
O administrador seleciona os campos que deseja modificar.
O administrador informa os novos valores.
O sistema valida as alterações.
O sistema atualiza o registro no MongoDB.
O sistema atualiza a data de modificação.
O sistema confirma a operação.
Fluxos alternativos:
A1 — Nenhuma alteração realizada: o sistema informa que não existem modificações a salvar.
A2 — Atualização parcial: o sistema modifica somente os campos enviados, preservando os demais.
Fluxos de exceção:
E1 — Medicamento inexistente: o sistema informa que o registro não foi encontrado.
E2 — Dados inválidos: o sistema rejeita as alterações e apresenta os campos que precisam ser corrigidos.
E3 — Falha na persistência: o sistema informa que não foi possível salvar as modificações.
Pós-condição: o medicamento permanece cadastrado com as informações atualizadas.
UC05 — Inativar medicamento
Objetivo: permitir que um medicamento deixe de aparecer nas consultas e listagens convencionais sem que seu registro seja permanentemente excluído.
Ator principal: Administrador do catálogo.
Pré-condições: o medicamento deve existir e estar ativo.
Gatilho: o administrador solicita a inativação.
Requisitos relacionados: RF05.
Fluxo principal:
O administrador informa o identificador do medicamento.
O sistema localiza o registro.
O sistema apresenta as informações do medicamento.
O administrador solicita a inativação.
O sistema altera o status para inativo.
O sistema atualiza a data de modificação.
O sistema confirma a operação.
Fluxos alternativos:
A1 — Registro já inativo: o sistema informa que o medicamento já se encontra inativado.
Fluxos de exceção:
E1 — Medicamento inexistente: o sistema informa que não encontrou o registro.
E2 — Falha na atualização: o sistema informa que não foi possível alterar o status.
Pós-condição: o registro permanece armazenado, mas passa a ter status inativo e deixa de aparecer nas listagens convencionais.
UC06 — Pesquisar medicamento por nome
Objetivo: permitir que o administrador encontre medicamentos utilizando o nome genérico ou comercial.
Ator principal: Administrador do catálogo.
Pré-condições: o sistema deve estar disponível.
Gatilho: o administrador informa um termo de pesquisa.
Requisitos relacionados: RF06.
Fluxo principal:
O administrador acessa a pesquisa.
O administrador informa o nome ou parte do nome do medicamento.
O sistema recebe o termo pesquisado.
O sistema realiza a consulta no MongoDB.
O sistema identifica os registros correspondentes.
O sistema apresenta os resultados.
Fluxos alternativos:
A1 — Pesquisa parcial: o sistema permite encontrar medicamentos mesmo quando apenas parte do nome é informada.
A2 — Nenhum resultado: o sistema apresenta uma mensagem informando que nenhum medicamento foi encontrado.
Fluxos de exceção:
E1 — Termo vazio: o sistema solicita que o administrador informe um termo válido.
E2 — Falha na consulta: o sistema informa que não foi possível realizar a pesquisa.
Pós-condição: os resultados correspondentes são apresentados sem modificar os registros.
UC07 — Filtrar medicamentos
Objetivo: permitir a organização dos resultados de acordo com características específicas.
Ator principal: Administrador do catálogo.
Pré-condições: devem existir registros disponíveis para consulta.
Gatilho: o administrador seleciona um ou mais filtros.
Requisitos relacionados: RF07, RF08 e RF09.
Fluxo principal:
O administrador acessa a listagem de medicamentos.
O sistema disponibiliza os filtros.
O administrador seleciona a apresentação, a categoria ou a concentração desejada.
O sistema recebe os parâmetros.
O sistema consulta os registros correspondentes.
O sistema apresenta os resultados filtrados.
Fluxos alternativos:
A1 — Múltiplos filtros: o administrador combina diferentes critérios.
A2 — Remoção de filtros: o administrador remove os critérios e retorna à listagem geral.
Fluxos de exceção:
E1 — Nenhum resultado correspondente: o sistema informa que não existem medicamentos compatíveis com os filtros.
E2 — Parâmetro inválido: o sistema informa que o filtro não pode ser aplicado.
Pós-condição: os resultados são apresentados conforme os critérios selecionados.
UC08 — Cadastrar preço de aquisição
Objetivo: permitir o registro do preço de aquisição associado a um medicamento.
Ator principal: Administrador do catálogo.
Pré-condições: o medicamento deve estar cadastrado.
Gatilho: o administrador solicita o registro de um preço.
Requisitos relacionados: RF10.
Fluxo principal:
O administrador seleciona o medicamento.
O sistema apresenta os dados do registro.
O administrador informa o preço de aquisição.
O administrador informa a moeda utilizada.
O sistema valida o valor.
O sistema registra as informações financeiras.
O sistema confirma o registro.
Fluxos alternativos:
A1 — Atualização de preço existente: o administrador pode cadastrar um novo valor para substituir o preço atual, conforme a regra definida para o MVP.
Fluxos de exceção:
E1 — Preço negativo: o sistema rejeita o valor.
E2 — Moeda não informada: o sistema solicita o preenchimento.
E3 — Medicamento inexistente: o sistema informa que o registro não foi encontrado.
Pós-condição: o preço de aquisição fica associado ao medicamento.
UC09 — Atualizar preço de aquisição
Objetivo: permitir a atualização do preço de aquisição de um medicamento.
Ator principal: Administrador do catálogo.
Pré-condições: o medicamento deve possuir um registro cadastrado.
Gatilho: o administrador solicita a atualização do preço.
Requisitos relacionados: RF11.
Fluxo principal:
O administrador seleciona o medicamento.
O sistema recupera o preço atual.
O administrador informa o novo valor.
O sistema valida o preço e a moeda.
O sistema atualiza as informações financeiras.
O sistema confirma a alteração.
Fluxos alternativos:
A1 — Novo preço igual ao anterior: o sistema pode informar que não houve alteração efetiva.
Fluxos de exceção:
E1 — Valor inválido: o sistema rejeita o novo preço.
E2 — Registro inexistente: o sistema informa que não encontrou o medicamento.
E3 — Falha no banco de dados: o sistema informa que a atualização não foi concluída.
Pós-condição: o medicamento passa a apresentar o novo preço de aquisição.
UC10 — Consultar informações financeiras
Objetivo: permitir a consulta das informações financeiras registradas para um medicamento.
Ator principal: Administrador do catálogo.
Pré-condições: o medicamento deve estar cadastrado.
Gatilho: o administrador solicita a consulta financeira.
Requisitos relacionados: RF12.
Fluxo principal:
O administrador seleciona o medicamento.
O sistema recupera as informações financeiras.
O sistema identifica o preço registrado e a moeda correspondente.
O sistema apresenta os dados financeiros.
Fluxos alternativos:
A1 — Preço não cadastrado: o sistema informa que ainda não existem informações financeiras para o medicamento.
Fluxos de exceção:
E1 — Medicamento inexistente: o sistema informa que não encontrou o registro.
E2 — Falha na consulta: o sistema informa que não foi possível recuperar os dados financeiros.
Pós-condição: as informações financeiras são exibidas sem alteração nos registros.
5. Relação entre casos de uso e requisitos funcionais
Caso de uso
Funcionalidade
Requisitos relacionados
UC01
Cadastrar antimicrobiano
RF01
UC02
Listar medicamentos
RF03
UC03
Consultar por identificador
RF02
UC04
Atualizar medicamento
RF04
UC05
Inativar medicamento
RF05
UC06
Pesquisar por nome
RF06
UC07
Filtrar medicamentos
RF07, RF08, RF09
UC08
Cadastrar preço
RF10
UC09
Atualizar preço
RF11
UC10
Consultar informações financeiras
RF12

6. Considerações finais
Os casos de uso apresentados estabelecem uma representação funcional do PharmaCatalog e servem como referência para o desenvolvimento da aplicação.
A especificação permite compreender como as funcionalidades deverão se comportar, quais condições precisam ser atendidas e como o sistema deverá reagir diante de situações alternativas ou excepcionais.
Na primeira versão, o foco estará no gerenciamento de informações farmacêuticas e financeiras de antimicrobianos. A integração com sistemas externos, a expansão para outras categorias de medicamentos e novas funcionalidades poderão ser incorporadas em versões futuras.


