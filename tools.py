from langchain_google_calendar_tools.helper_tools.get_current_datetime import GetCurrentDatetime
from langchain_google_calendar_tools.tools.update_exist_event.tool import UpdateExistEvent
from langchain_google_calendar_tools.tools.list_events.tool import ListEvents
from langchain_google_calendar_tools.tools.create_new_event.tool import CreateNewEvent
from langchain_google_calendar_tools.utils import build_resource_service, get_oauth_credentials
from langchain_google_community import GmailToolkit
import pytz


class Tools:
    def __init__(self):
        br_timezone = pytz.timezone('America/Sao_Paulo')
        # Monkey-patch em pytz.timezone para utilizar a timezone brasileira ao invés da vietnamita padrão da biblioteca langchain_google_calendar_tools
        pytz.timezone = lambda zone: br_timezone
        # Escopos da API do Google utilizados pela aplicação
        SCOPES = ["https://www.googleapis.com/auth/calendar.events",
                  "https://mail.google.com/"]

        # Configuração das Credenciais

        credentials = get_oauth_credentials(
            client_secrets_file="credentials_desktop.json",
            scopes=SCOPES
        )

        # Inicializa as ferramentas do Google Calendar

        api_resource = build_resource_service(credentials=credentials)

        calendar_tools = [
            ListEvents(api_resource=api_resource),
            CreateNewEvent(api_resource=api_resource),
            UpdateExistEvent(api_resource=api_resource),
            GetCurrentDatetime()]

        # Inicializa as ferramentas do Gmail

        toolkit = GmailToolkit()

        gmail_tools = toolkit.get_tools()

        self.tools = gmail_tools+calendar_tools

    def get_tools(self):
        return self.tools
