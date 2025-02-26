Como Rodar o Sistema Distribuído Localmente com Docker

Este documento descreve os passos necessários para executar o sistema distribuído utilizando Docker e Docker Compose, garantindo a replicabilidade do ambiente sem configurações manuais.

Requisitos

Antes de iniciar, certifique-se de ter os seguintes softwares instalados:

Docker: https://docs.docker.com/get-docker/

Docker Compose: https://docs.docker.com/compose/install/

Estrutura do Projeto

O sistema é composto por três serviços executados em containers:

VM1 (porta 8000): Interface principal do sistema.

VM2 (porta 8001): Processamento intermediário.

VM3 (porta 8002): Base de dados e informações.

Configuração e Execução

1. Clonar o Repositório

Abra um terminal e execute os seguintes comandos:

 git clone https://github.com/kaykyvasconcelos/sistema-distribuido.git  
 cd sistema-distribuido  

2. Construir e Iniciar os Containers

Para iniciar o sistema distribuído, execute:

 docker-compose up --build -d  

Esse comando realiza os seguintes passos:

Cria a rede de comunicação entre os serviços.

Constrói as imagens do Docker para cada VM.

Inicia os containers em segundo plano (-d).

3. Testar os Endpoints

Verifique se os serviços estão funcionando corretamente executando as seguintes requisições:

VM1 (Interface Principal)

curl -i http://localhost:8000/mensagem/autores  

VM2 (Processamento)

curl -i http://localhost:8001/processar/autores  

VM3 (Base de Dados)

curl -i http://localhost:8002/dados/autores  

Se as respostas retornarem os autores do sistema, a configuração está funcionando corretamente.

4. Parar os Containers

Caso precise interromper a execução, utilize:

 docker-compose down  

Solução de Problemas

Erro: "port already in use"

Se uma porta já estiver sendo utilizada, pare os processos em execução com:

 docker stop $(docker ps -q)  
 docker rm $(docker ps -aq)  

Depois, tente rodar novamente:

 docker-compose up --build -d  

Erro: "Could not resolve host"

Se um serviço não conseguir se comunicar com outro, reinicie a rede Docker:

 docker network prune -f  
 docker-compose up --build -d  

Considerações Finais

Este guia permite que qualquer pessoa execute o Sistema Distribuído localmente com Docker, garantindo um ambiente padronizado e fácil de replicar.

Caso tenha dúvidas, consulte a documentação oficial do Docker ou entre em contato com os responsáveis pelo projeto.
