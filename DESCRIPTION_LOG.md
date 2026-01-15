**MODELAGEM DE DADOS (POSTGRES/ALEMBIC)**

Após preencher o .env, no ubuntu através do wsl, tentei usar o make para buildar e iniciar os containers. No entanto, o backend não iniciou corretamente, o seu log indicou que o [config.py](http://config.py)  faltava a definição da variável SENTRY\_DSN, que em seguida foi adicionada.

A fim de seguir a ordem sugerida no README do projeto, comecei criando as tabelas User, Team e TeamMember. A tabela Team possui o campo leader\_id como único e obrigatório que é uma FK da tabela User para garantir que toda equipe tenha um líder e que esse líder só possa liderar uma equipe por vez.

A tabela TeamMember possui uma chave primária composta contendo um user\_id e  um team\_id, o user\_id é único para garantir que cada membro pertença a apenas uma equipe.

**BACKEND (FASTAPI)**

Primeiramente, criei a função get\_session() em [db.py](http://db.py) para automatizar o início de sessões das rotas. Em seguida, criei os schemas para usuários baseados no models criado para o postgreSQL. Após isso, criei as rotas para o CRUD de usuários no [users.py](http://users.py).

Para fazer os testes do CRUD de usuários, primeiro foi criado o [conftest.py](http://conftest.py) para realizar um setup inicial de testes, usando o SQLite para tornar os testes mais leves. Depois, criei 8 testes de integração para o CRUD de usuário, incluindo casos de sucesso e de falha.

Em seguida, fiz o CRUD de equipes, criando os schemas e rotas correspondentes. Modularizando as rotas e os schemas de equipes e usuários em arquivos diferentes. Além disso, criei um \_init\_.py dentro da pasta schemas para exportar os schemas de uma forma geral para os outros arquivos. Depois, criei 12 testes de integração para o CRUD de equipe, incluindo casos de sucesso e de falha.

A seguir, criei schema de criação e leitura de membro baseado na class TeamMember criada no models. Criei rotas de post e delete para membro de equipe e 9 testes de integração incluindo casos de sucesso e falha.

Para remover das routes a lógica de acesso ao banco de dados, criei 3 arquivos de repositories, um para cada arquivo de rotas e depois os refatorei para usar os repositories.

A seguir, usei o generator client do OpenAPI para exportar a tipagem do backend para o front, gerando automaticamente a pasta ‘api-client’.

Criei o arquivo [exceptions.py](http://exceptions.py) para padronizar erros como erros not found e erros de regras de negócio. Além disso, criei o arquivo exception\_handlers.py para centralizar o tratamento de erros do backend e poder reduzir código repetidos com try/except nas rotas.

**FRONTEND (REACT)**

Descrevi o projeto para o lovable e ele criou um projeto com as telas necessárias. No entanto, não consegui usar, pois tive muitos problemas tentando integrar o projeto criado pelo lovable ao projeto base do processo seletivo. Portanto, optei por criar as telas com o copilot.

Alterei o app.tsx para que ele inclua as novas páginas necessárias para o desafio (UsersPage, TeamsPage, TeamDetailPage) e uma MainPage que permite acessar tanto as quests quanto as páginas do desafio.

A userPage faz o CRUD de usuário, a Teamspage exibe as equipes existentes, ao clicar em uma das equipes, o usuário é levado para a TeamDetailPage daquela equipe específica

Criei a pasta frontend/api para conter os arquivos gerados automaticamente pelo openAPI juntamente com um arquivo de instâncias de configs da api, o objetivo desse arquivo é centralizar a comunicação com a api para que as páginas apenas importem essas instâncias.

Criei também uma pasta services que importa os métodos da api para serem usados pelas páginas. Além disso, criei uma pasta errors responsável por traduzir as  mensagens de erro em inglês geradas pelo backend para mensagens em português a serem exibidas pelo frontend.  
