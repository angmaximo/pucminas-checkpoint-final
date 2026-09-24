# Projeto Final / Portfólio Unificado - Pós-Graduação PUC Minas
**Arquitetura Serverless e Cloud Computing (Google Cloud Platform)**

Este repositório consolida a evolução prática desenvolvida ao longo da pós-graduação, estruturada em checkpoints incrementais. Cada pasta representa uma etapa do projeto, evoluindo desde os fundamentos de computação sem servidor até a orquestração, mensageria e observabilidade.

---

## 📂 Estrutura do Repositório

```text
.
├── checkpoint-1/     # Primeira função Serverless
├── checkpoint-2/     # Serviços de Mensageria Assíncronos
├── checkpoint-3/     # Orquestração de Fluxos (Event-Driven)
├── checkpoint-4/     # Monitoramento de Eventos
└── checkpoint-5/     # Deploys usando CI/CD
```

---

## 🚀 Visão Geral dos Checkpoints

### [Checkpoint 1: Primeira Função Serverless](./checkpoint-1)
- **Objetivo:** Introdução ao modelo de computação sem servidor.
- **Tecnologias:** Cloud Run, Cloud Storage, Python/Node.js.
- **Descrição:** Implementação de uma aplicação minimalista, parfa atender requisições HTTP, demonstrando as vantagens de elasticidade e ausência de gerenciamento de infraestrutura física.

### [Checkpoint 2: Serviços de Mensagens Assíncronos](./checkpoint-2)
- **Objetivo:** Criar a aplicação do checkpoint1 para responder a requisições event-driven, atráves de mensageria.
- **Tecnologias:** Pub/Sub
- **Descrição:** Evolução da API para gerar requisições acionadas por eventos.

### [Checkpoint 3: Orquestração de Fluxos](./checkpoint-3)
- **Objetivo:** Orquestrar fluxo tópico pub/sub e da aplicação publicada no Cloud Run. (*Event-Driven Architecture*).
- **Tecnologias:** Google Cloud Pub/Sub, Workflows.
- **Descrição:** Implementação de produtores e consumidores de mensagens para garantir resiliência, tolerância a falhas e escalabilidade horizontal em picos de acesso.

### [Checkpoint 4: Monitoramento de Eventos](./checkpoint-4)
- **Objetivo:** Monitorar os eventos gerados pela aplicação e nos tópicos de mensagens, usando serviços de observabilidade.
- **Tecnologias:** Google CLoud Monitoring e Logging.
- **Descrição:** Definição declarativa da infraestrutura na nuvem, garantindo reprodutibilidade, versionamento do ambiente e agilidade no fluxo de CI/CD.

### [Checkpoint 5: Deploy usando CI/CD](./checkpoint-5)
- **Objetivo:** Criar uma esteira CI/CD para publicação e realilzações de testes de estrtura e segurança do código.
- **Tecnologias:** Github Actions.
- **Descrição:** Publicar o código no repositório e realizar as validações de segurança, gerando artefatos..

---

## ☁️ Comandos Úteis no Google Cloud (GCP)

### 1. Deploy do Serviço (Exemplo com Cloud Run)
Para publicar ou atualizar qualquer um dos módulos conteinerizados no Google Cloud Run:
```bash
gcloud run deploy NOME_DO_SERVICO \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

### 2. Visualização de Logs no Terminal
Para acompanhar os logs gerados pela aplicação e validar o funcionamento do sistema em tempo real:

* **Leitura rápida dos últimos logs:**
  ```bash
  gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=NOME_DO_SERVICO" --limit 30 --format json
  ```

* **Streaming de logs ao vivo (modo cauda):**
  ```bash
  gcloud beta logging tail "resource.type=cloud_run_revision AND resource.labels.service_name=NOME_DO_SERVICO"
  ```