import threading
import os
from azure.servicebus import ServiceBusClient

SERVICE_BUS_CONNECTION_STRING = os.getenv("SERVICE_BUS_CONNECTION_STRING")
SERVICE_BUS_QUEUE_NAME = os.getenv("SERVICE_BUS_QUEUE_NAME")

def processar_evento(mensagem):
    print("Evento recebido:", mensagem)
    # Aqui você cria o cenário acadêmico:
    # - Enviar e-mail
    # - Criar log
    # - Criar arquivo no Blob
    # - Processar imagem
    # - Criar registro no banco
    # - Etc.

def iniciar_service_bus_listener():
    client = ServiceBusClient.from_connection_string(SERVICE_BUS_CONNECTION_STRING)

    with client:
        receiver = client.get_queue_receiver(queue_name=SERVICE_BUS_QUEUE_NAME)
        with receiver:
            for msg in receiver:
                processar_evento(str(msg))
                receiver.complete_message(msg)

def iniciar_thread_listener():
    thread = threading.Thread(target=iniciar_service_bus_listener, daemon=True)
    thread.start()
