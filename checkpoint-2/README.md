# Checkpoint #2 - Serviço de mensagens assíncronos
  
o projeto tem o objetivo de criar um arquivo <id>.txt no bucket CLoud Storage,quando for enviado uma requisição ao tópico criado no Google Pub/Sub. 

## Provedor Utilizado  
* Google Cloud Pub/Sub  
  
## Como rodar localmente  
  
1 - Execute o comando abaixo para enviar mensagem para o tópico, que irá gerar um arquivo <id_evento>.txt no bucket do Cloud Storage  
  
`gcloud pubsub topics publish images-topic --message="Teste Pub/Sub!"`  
  
2 - Quando o comando finalizar, será exibido uma mensage, contendo um ID. Salve esse ID;  
  
3. Digite o comando, que será enviado pelo Canvas, para identificar se o arquivo foi criado no bucket (<id.txt>).  
  
  
## Pré requisitos  
  
Flask==3.0.0  
gunicorn==21.2.0  
google-cloud-storage==2.14.0   
  
### Passo a passo  
  
1. Clone o repositório para sua máquina:  
   `git clone https://github.com/angmaximo/pucminas-checkpoint2.git`  
  
2. Entre na pasta do projeto   
   `cd pucminas-checkpoint2`  
 
  
. 




