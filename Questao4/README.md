# Projeto Questao4 - Conector FTP

Nunca trabalhei com arquivos .jar, então, como essa foi a primeira vez, optei por uma forma mais simples para resolver essa questão.

    * **Passo 1** - Primeiramente pesquisar como poderia executar o projeto a fim de conseguir os dados solicitados, após algums  pesquisar na Web e também no Chat GPT, optei em utilizar um Java Decompiler (JD-GUI).

    * **Passo 2** - Após concluir a instalação do Java e do JD-GUI, obtive acesso  ao código fonte do projeto.

    * **Passo 3** - Através do arquivo Monitorar.class pelos métodos "iniciarPrograma" e "conectar" é possível localizar o host "52.200.142.116", o usuário "ctflteste" e uma parte da senha "YdrTXPK#m", mais abaixo, no mesmo arquivo, é possível localizar outra parte da senha (String senha = containfo.getSenha() + "cG7KU";) que traz a senha armazenada e concatena com o "cG7KU".

         ![Host_login_parte-senha](https://github.com/user-attachments/assets/6fe102d7-f32d-4e65-82de-49a8312118e4)

    * **Passo 4** - No arquivo Conexao.class temos uma nova concateção com a senha no seguinte local (if (!this.ftp.login(usuario, senha + "T#H@$P"))), finalizando a senha como: YdrTXPK#mcG7KUT#H@$P.

         ![parte_final_senha](https://github.com/user-attachments/assets/c1142a43-1687-41b1-8fec-a57fa01de999)

    * **Passo 5** - Para acessar o servidor e poder localizar o arquivo, utilizei o Firezila para acessar o servidor FTP e assim acessar ao arquivo "Great Job.txt".

         ![Firezila](https://github.com/user-attachments/assets/7abc1f06-92d8-4ff2-8d1d-aebcbc9d8715)
