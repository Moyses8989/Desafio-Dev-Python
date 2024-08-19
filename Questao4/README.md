# Questão 4

- Nunca trabalhei com arquivos .jar, então, como essa foi a primeira vez, optei por uma forma mais simples para resolver essa questão.

    * **Passo 1** - Primeiramente pesquisar como poderia executar o projeto a fim de conseguir os dados solicitados, após algums  pesquisar na Web e também no Chat GPT, optei em utilizar um Java Decompiler (JD-GUI).

    * **Passo 2** - Após concluir a instalação do Java e do JD-GUI, obtive acesso  ao código fonte do projeto.

    * **Passo 3** - Através do arquivo Monitorar.class pelos métodos "iniciarPrograma" e "conectar" é possível localizar o host "52.200.142.116", o usuário "ctflteste" e uma parte da senha "YdrTXPK#m", mais abaixo, no mesmo arquivo, é possível localizar outra parte da senha (String senha = containfo.getSenha() + "cG7KU";) que traz a senha armazenada e concatena com o "cG7KU".

    ![Host, Usur e part_senha](Questao4/Imagens/Host_login_parte-senha.png)

    * **Passo 4** - No arquivo Conexao.class temos uma nova concateção com a senha no seguinte local (if (!this.ftp.login(usuario, senha + "T#H@$P"))), finalizando a senha como: YdrTXPK#mcG7KUT#H@$P.

    ![Parte final da senha](Questao4/Imagens/parte_final_senha.png)

    * **Passo 5** - Para acessar o servidor e poder localizar o arquivo, utilizei o Firezila para acessar o servidor FTP e assim acessar ao arquivo "Great Job.txt".

    ![Parte final da senha](Questao4/Imagens/Firezila.png)