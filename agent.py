from tools import Tools
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import datetime
load_dotenv()


class Agent():
    # Configura o agente
    def __init__(self) -> None:
        self.llm = ChatOpenAI(model="gpt-4o-mini")
        self.tools = Tools().get_tools()
        datetime_now = str(datetime.datetime.now())

        self.system_prompt = f"""Você é um assistente pessoal capaz de interagir com o email e a agenda do usuário.
Você deve interagir com o os componentes de email e agenda para auxiliar o usuário na sua organização pessoal.
Caso o usuário solicite a criação de um evento, saiba que o parâmetro "resumo" também pode ser referido como "título" ou "nome" do evento.
O dia e horário no momento são: "{datetime_now}". Leve esse dado em consideração caso o usuário queira executar alguma ação baseada no dia/horário atual (amanhã, por exemplo).
Caso você receba uma resposta da ferramenta dizendo "Fix your mistakes", você deve tentar fazer uma requisição consertando o que foi apontado.
Sempre que fizer uma chamada à tool "list_events" forneça uma "end_date", mesmo que seja daqui a 100 anos.
Se você não incluir uma "end_date" incorrerá em um erro."""

    # Cria o agente
    def create_agent(self):
        return create_react_agent(
            self.llm, tools=self.tools, state_modifier=self.system_prompt, checkpointer=MemorySaver())
