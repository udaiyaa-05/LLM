from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
message=[
    SystemMessage(content="you are a rude person")
    ,HumanMessage(content="Hello, how are you?")
]
response = llm.invoke(message)
print(response.content)