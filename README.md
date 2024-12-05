**Teste de Performance (TP) 03**

**Disciplina:** Desenvolvimento de Data-Driven Apps com Python

**Aluno:** Miguel Belardinelli Prytoluk

**Data:** 05/12/2024


## Descrição do Projeto
**Assistente Pessoal Inteligente** é uma aplicação que utiliza LLMs para gerenciar emails e agendas.

### Definição do Problema
**Problema**: Usuários com agendas e caixas de entrada lotadas têm dificuldade em gerenciar compromissos e responder e-mails de forma eficiente.

**Objetivo da aplicação**: Desenvolver um assistente pessoal inteligente que permita consultar e gerenciar compromissos no Google Calendar e interagir com e-mails no Gmail de forma rápida e eficiente. A aplicação é capaz de facilitar a organização do usuário por meio de interação com Email e Calendário por meio de interface de chat, como um assistente pessoal.

**Público-alvo**: Profissionais e estudantes que precisam otimizar o uso de suas agendas e e-mails.

**Principais funcionalidades**:
- Consultar eventos no Google Calendar.
- Criar novos eventos no Google Calendar.
- Consultar e-mails do Gmail e responder a perguntas sobre eles.
- Redigir e enviar e-mails no Gmail.

**Casos de uso**:
- Perguntar sobre compromissos da semana e adicionar novos eventos.
- Localizar e-mails específicos (por remetente ou assunto) e enviar emails para seus remetentes.

## Testes Práticos
- **Solicitação**: *"Liste meus próximos eventos"*
    - **Resultado**: São retornados os próximos eventos do usuário.
- **Solicitação**: *"Crie um evento chamado 'Reunião' amanhã às 15h."*
    - **Resultado**: É criado o evento e fornecido um link para verificar no Google Calendar.
- **Solicitação**: *"Qual o último email que eu recebi?"*
    - **Resultado**: São retornadas as informações relativas ao último email recebido.
- **Solicitação**: *"Envie um email para 'exemplo@gmail.com' dizendo que a aplicação está funcionando corretamente"*
    - **Resultado**: Email enviado com sucesso.

## Requisitos

- Python 3.8 ou superior
- `virtualenv` para criação de ambiente virtual
- Os pacotes listados no arquivo `requirements.txt`
- Uma chave de API Open AI
- Uma conta na GCP (Google Cloud Platform)
- Uma conta Google com Gmail e Calendar

## Instruções para configurar o ambiente e rodar o projeto

### 1. Clonar o Repositório

Clone este repositório na sua máquina local.

```bash
git clone https://github.com/mprytolukinfnet/Miguel_Prytoluk_DR3_TP3_2024_2.git
```

### 2. Criar um Ambiente Virtual

No diretório do projeto, crie um ambiente virtual usando `virtualenv`:

```bash
virtualenv venv
```

### 3. Ativar o Ambiente Virtual
- No Windows:
```bash
venv\Scripts\activate
```

- No Linux/Mac:
```bash
source venv/bin/activate
```

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 5. Variáveis de ambiente

Criar um arquivo `.env` na raiz do projeto contendo sua chave de API Open AI no formato:
```env
OPENAI_API_KEY=chave-open-ai
```

### 6. Configurar GCP (1)

- Na GCP (https://console.cloud.google.com/), criar um projeto ou utilizar um existente
- Ativar as APIs do Gmail e Calendar:
https://console.cloud.google.com/apis/library/gmail.googleapis.com
https://console.cloud.google.com/apis/library/calendar-json.googleapis.com
- Na tela de Consent da API (https://console.cloud.google.com/apis/credentials/consent), registrar um APP externo. O único campo relevante para essa aplicação é **Test users**, onde você deve adicionar o seu email gmail que será utilizado na aplicação: exemplo: seu_email@gmail.com
### 7. Configurar GCP (2)
Na tela de Credentials (https://console.cloud.google.com/apis/credentials) você deve criar duas crendenciais do tipo `OAuth client ID`:
- A primeira de "Application type" do tipo `Web application`. No campo `Authorized redirect URIs`
você deve preencher `http://localhost/`. Salvar a credencial na raiz do projeto com o nome `credentials.json`.
- A segunda de "Application type" do tipo `Desktop app`. Salvar a credencial na raiz do projeto com o nome `credentials_desktop.json`.

### 8. Executar o Dashboard
Para rodar a aplicação, execute o seguinte comando no terminal:
```bash
streamlit run main.py
```

Ao rodar pela primeira vez, você precisará logar com sua conta Google e liberar as permissões solicitadas do Gmail e Calendar (marque Select all).

A aplicação estará disponível no seu navegador, normalmente acessível no endereço http://localhost:8501.

## Estrutura do Projeto
- **main.py**: Contém o código principal do dashboard.
- **agent.py**: Contém a lógica para criar um Agente ReAct.
- **tools.py**: Carrega e configura as ferramentas (tools) a serem utilizadas pelo Agente.
- **requirements.txt**: Lista de dependências necessárias para rodar o projeto.
