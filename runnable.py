from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import StrOutputParser
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)