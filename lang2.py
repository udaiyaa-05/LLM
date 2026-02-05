from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
load_dotenv()
llm=init_chat_model(model="llama3-8b-8192",temperature=0.7,model_provider="groq")
response = llm.invoke("Hello, how are you?")
print(response.content)