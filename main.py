import streamlit as st
from agent import Agent

state = st.session_state

# Cria o agente e armazena no estado da aplicação
if 'graph' not in st.session_state:
    state.graph = Agent().create_agent()

# Cria uma config para possibilitar a memória do Agente
config = {"configurable": {"thread_id": "thread-1"}}

# Armazena o histórico de mensagens no estado da aplicação
if 'messages' not in st.session_state:
    state.messages = []

# Gerencia a habilitação/desabilitação do input no estado da aplicação
if "input_disabled" not in st.session_state:
    state.input_disabled = False

# Interface Streamlit
st.title("Assistente Pessoal Inteligente")
st.write("Este assistente gerencia sua agenda e responde a emails!")

# Desabilita o input após enviar uma mensagem
def disable_input():
    st.session_state.input_disabled = True

msg_container = st.container()

prompt = st.chat_input("Peça algo ao assistente:",
                       disabled=state.input_disabled, on_submit=disable_input)

# Gera o histórico de mensagens na interface
for msg in state.messages:
    with msg_container:
        chat_message = st.chat_message(msg['name'])
        chat_message.write(msg['msg'])

# Processa o prompt quando enviado
if prompt:
    # Adiciona o prompt do usuário no estado e na interface
    state.messages.append({"name": "user", "msg": prompt})
    with msg_container:
        user_message = st.chat_message('user')
        user_message.write(prompt)
    try:
        # Envia o prompt do usuário para o Agente 
        inputs = {"messages": [("user", prompt)]}
        response = state.graph.invoke(inputs, config)['messages']
        # Você pode fazer o Debug da resposta do agente aqui:
        # print(response, "\n\n")
        response = response[-1].content
        # Adiciona a resposta do Agente no estado e na interface
        state.messages.append({"name": "assistant", "msg": response})
        with msg_container:
            assistant_message = st.chat_message('assistant')
            assistant_message.write(response)
    except Exception as e:
        st.warning("Não foi possível gerar sua resposta.")
    # Reabilita o input após receber a resposta do modelo
    state.input_disabled = False
    st.rerun()
