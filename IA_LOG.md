Em meu projeto fastAPI, cujo objetivo é criar um sistema onde seja possível gerenciar Equipes e seus respectivos Membros (Usuários). Preencha o models.py para fazer a modelagem de dados com o seguinte padrão:

Projete os modelos para Equipes e a associação com Usuários.  
Regras de Negócio (Constraints):  
\- Uma Equipe deve ter obrigatoriamente um Líder (que é um Usuário já existente).   
\- Unicidade de Membro: Um Usuário só pode pertencer a uma única equipe por vez.   
\- Unicidade de Líder: Um Usuário só pode liderar uma única equipe por vez.

—------------------------------------------------------------------------------------------------------------------------

Usando o alembic, como posso garantir migrações que persistam o modelo no banco e assegurem integridade referencial (FKs e Constraints) para impedir estados inválidos (ex: usuário em duas equipes ao mesmo tempo)?

—----------------------------------------------------------------------------------------------------------------------

Implemente endpoints para: Criar, Listar, Editar e Remover Usuários

—----------------------------------------------------------------------------------------------------------------------

Crie testes de integração para o CRUD de usuários

Nesse momento, o copilot gerou testes de integração com SQLite, mas não sobrescreveu a função get\_session() em seu fixtures, o que faria os testes usarem o banco de dados real. Percebi ao analisar o fluxo dos testes e perceber que as rotas continuariam usando o get\_session() que faz referência ao banco real.

—------------------------------------------------------------------------------------------------------------------------

Implemente endpoints para: Criar, Listar, Editar e Remover Equipes.

Nesse momento, o copilot escreveu os schemas de equipe no mesmo arquivo em que os schemas de usuários haviam sido escritos. Então, eu criei uma pasta schemas e dividi os schemas de usuários em [user.py](http://user.py) e os schemas de equipes em [team.py](http://team.py)

Outros erros do copilot nesse momento: 

- Criou um schema de retorno de equipe que retornava atributos que não estavam sendo armazenados no database (tentou retornar o nome do líder junto da equipe, mas a equipe apenas está armazenando o id do líder), percebi enquanto lia o arquivo e notei inconsistências.  
-  Usar o comando errado para tentar deletar a equipe do database, ele tentou deletar usando “session.exec(select(TeamMember).where(TeamMember.team\_id \== team\_id)).delete()”, quando o comando correto era “session.exec(delete(TeamMember).where(TeamMember.team\_id \== team\_id))”

—------------------------------------------------------------------------------------------------------------------------

Preencha o test\_teams.py com testes para o CRUD de equipes.

Aqui o copilot preencheu vários testes tentando fazer um assert com atributos inexistentes no schema de equipe. Além disso, em outro teste, ele criou uma variável que não foi usada. Foi possível perceber através da leitura do arquivo gerado.

—------------------------------------------------------------------------------------------------------------------------  
Implemente endpoints para: Adicionar e Remover membros de uma equipe (respeitando a regra de que o sistema bloqueia que um usuário já presente uma equipe entre em outra). Faça um arquivo member.py em schema baseado na class TeamMember do models.py. Depois as rotas referentes a esse schema devem ser criadas em members.py lá na pasta routes.

Aqui na rota post de member, o copilot checa se o usuário a ser adicionado já não é o líder da equipe e depois checa se o usuário a ser adicionado já é membro de alguma equipe. Tornando a primeira verificação redundante.

—------------------------------------------------------------------------------------------------------------------------  
Na pasta tests, crie o arquivo test\_members.py para fazer os testes de integração dos endpoints criados em [members.py](http://members.py)

O Copilot tentou fazer asserts com atributos que não existiam e mensagem de erro que não estava nas rotas.

—------------------------------------------------------------------------------------------------------------------------

Crie um arquivo repositorie para cada arquivo de routes.  
—------------------------------------------------------------------------------------------------------------------------  
Crie uma página Users responsável pelo CRUD de usuários  
—-----------------------------------------------------------------------------------------------------------------------  
Crie uma página responsável por listar as equipes existentes, exibindo o nome das equipes e os nome dos seus líderes.  
—----------------------------------------------------------------------------------------------------------------------  
Crie uma página a ser exibida após clicar no nome de uma das equipes na página de equipes. Ela deve mostrar o nome das equipes, seus membros e permitir que membros sejam adicionados/removidos e que a equipe seja atualizada/excluída.

O copilot gerou páginas que criavam uma instância para se conectar a api, posteriormente lendo os critérios de avaliação do desafio, percebi que isso era algo a ser corrigido. Portanto, criei o arquivo [apiConfig.ts](http://apiConfig.ts) para centralizar as instâncias.  
—------------------------------------------------------------------------------------------------------------------------  
