import os
import base64
from flask import Flask, request
from google.cloud import storage

app = Flask(__name__)

# Usa o mesmo bucket já existente
GCP_BUCKET_NAME = os.getenv("GCP_BUCKET_NAME")

def get_storage_client():
    return storage.Client()

@app.route("/", methods=["POST"])
def receive_event():
    envelope = request.get_json(silent=True)

    if not envelope:
        print("Evento inválido recebido.")
        return ("Bad Request", 400)

    msg = envelope.get("message", {})
    data = msg.get("data")

    if data:
        payload = base64.b64decode(data).decode("utf-8")
        print(f"[EVENTARC PUBSUB] Mensagem recebida: {payload}")

        # Evento: criar arquivo no bucket existente
        try:
            storage_client = get_storage_client()
            bucket = storage_client.bucket(GCP_BUCKET_NAME)
            blob = bucket.blob(f"evento_pubsub_{msg.get('messageId')}.txt")
            blob.upload_from_string(f"Evento recebido: {payload}")
            print("Arquivo de evento criado no bucket existente.")
        except Exception as e:
            print(f"Erro ao criar arquivo no bucket: {e}")
    else:
        print("[EVENTARC PUBSUB] Evento sem payload.")

    return ("", 204)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
