# Checkpoint #3 - Orquestrando fluxo de execução
  
Orquestrar o fluxo de mensagens de um tópico Pub/Sub e aplicação publicada no Cloud Run. 

## Provedor Utilizado  
* Google Cloud Workflows  
  
## Como rodar localmente  
  
1 - Execute o comando abaixo para enviar uma mensagem apra um tópico Pub/Sub:  
  `  gcloud pubsub topics publish images-topic --message="teste workflow"`  

2 - Após a execução, execute o comando abaixo para visualizar os logs da execução do Workflows:  
  `gcloud workflows executions list meu-workflow --location=us-central1` 
   
  
## Pré requisitos  
    
### Passo a passo  
  
1. Clone o repositório para sua máquina:  
   `git clone https://github.com/angmaximo/pucminas-checkpoint2.git`  
  
2. Entre na pasta do projeto   
   `cd pucminas-checkpoint3`  
 
  





