from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel
from langchain_groq import ChatGroq
llmm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
class llm_schema(BaseModel):
    setup:str
    punchline:str
object=llm_schema("setup","some setup","punchline","some punchline")
print(object)    