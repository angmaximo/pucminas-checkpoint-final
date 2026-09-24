# Projeto Final / Portfólio Unificado - Pós-Graduação PUC Minas
**Arquitetura Serverless e Cloud Computing (Google Cloud Platform)**

Este repositório consolida a evolução prática desenvolvida ao longo da pós-graduação, estruturada em checkpoints incrementais. Cada pasta representa uma etapa do projeto, evoluindo desde os fundamentos de computação sem servidor até a orquestração, mensageria e observabilidade.

---

## 📂 Estrutura do Repositório

```text
.
├── checkpoint-1/     # Fundamentos e primeira função Serverless
├── checkpoint-2/     # Persistência de dados e integração com storage/banco
├── checkpoint-3/     # Processamento assíncrono e mensageria (Event-Driven)
├── checkpoint-4/     # Infraestrutura como Código (IaC) / Automação de deploy
└── checkpoint-5/     # Observabilidade, monitoramento e inspeção de logs
```

---

## 🚀 Visão Geral dos Checkpoints

### [Checkpoint 1: Primeira Função Serverless](./checkpoint-1)
- **Objetivo:** Introdução ao modelo de computação sem servidor.
- **Tecnologias:** Cloud Functions / Cloud Run, Python/Node.js.
- **Descrição:** Implementação de uma API minimalista orientada a eventos ou requisições HTTP, demonstrando as vantagens de elasticidade e ausência de gerenciamento de infraestrutura física.

### [Checkpoint 2: Persistência e Gerenciamento de Dados](./checkpoint-2)
- **Objetivo:** Integrar a camada serverless com serviços gerenciados de armazenamento.
- **Tecnologias:** Firestore / Cloud SQL / Cloud Storage.
- **Descrição:** Evolução da API para realizar operações de leitura, escrita e consulta em bancos de dados em nuvem, tratando variáveis de ambiente e segurança de credenciais.

### [Checkpoint 3: Processamento Assíncrono e Mensageria](./checkpoint-3)
- **Objetivo:** Desacoplar componentes utilizando arquitetura orientada a eventos (*Event-Driven Architecture*).
- **Tecnologias:** Google Cloud Pub/Sub, Cloud Functions.
- **Descrição:** Implementação de produtores e consumidores de mensagens para garantir resiliência, tolerância a falhas e escalabilidade horizontal em picos de acesso.

### [Checkpoint 4: Infraestrutura como Código (IaC) e Automação](./checkpoint-4)
- **Objetivo:** Automatizar o provisionamento de recursos e padronizar o ciclo de entrega.
- **Tecnologias:** Terraform ou scripts de automação de deploy.
- **Descrição:** Definição declarativa da infraestrutura na nuvem, garantindo reprodutibilidade, versionamento do ambiente e agilidade no fluxo de CI/CD.

### [Checkpoint 5: Observabilidade e Monitoramento](./checkpoint-5)
- **Objetivo:** Validar o ecossistema em produção e auditar o comportamento da aplicação.
- **Tecnologias:** Google Cloud Logging, Cloud Monitoring.
- **Descrição:** Monitoramento de métricas de desempenho, rastreamento de exceções e inspeção em tempo real dos logs gerados pelos serviços.

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