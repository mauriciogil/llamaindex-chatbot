import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.chat_engine import SimpleChatEngine

# Configura tu clave de API de OpenAI
os.environ["OPENAI_API_KEY"] = "TU_CLAVE_API"

# Carga y procesa los documentos en la carpeta 'datos'
documents = SimpleDirectoryReader("datos").load_data()

# Crea un índice vectorial a partir de los documentos
index = VectorStoreIndex.from_documents(documents)

# Inicializa el motor de chat
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

# Bucle de interacción con el usuario
print("Asistente IA listo. Escribe 'salir' para terminar.")
while True:
    pregunta = input("Tú: ")
    if pregunta.lower() == "salir":
        break
    respuesta = chat_engine.chat(pregunta)
    print(f"Asistente: {respuesta.response}")
