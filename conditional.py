from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import StrOutputParser
from langchain_core.runnables import RunnableLambda,RunnableBranch
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
parser=StrOutputParser()

classifier_prompt=ChatPromptTemplate.from_messages([
    {"system","answer only POSITIVE or NEGATIVE "},
    {"human","{input}"}])
classifier_chain=classifier_prompt|llm|parser
def clasify(text):
    sentiment=classifier_chain.invoke({"text":text}.strip().upper())