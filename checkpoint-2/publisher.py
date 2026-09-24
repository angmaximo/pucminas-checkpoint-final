from azure.servicebus import ServiceBusClient, ServiceBusMessage
import os

conn = os.getenv("SERVICE_BUS_CONNECTION_STRING")
queue = os.getenv("SERVICE_BUS_QUEUE_NAME")

client = ServiceBusClient.from_connection_string(conn)

with client:
    sender = client.get_queue_sender(queue)
    with sender:
        msg = ServiceBusMessage("UPLOAD_REALIZADO")
        sender.send_messages(msg)
        print("Mensagem enviada!")
