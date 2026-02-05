from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
str_parser = StrOutputParser()

good_news_prompt = ChatPromptTemplate.from_messages({
    ("system", "You are a positive news generator."),
    ("human", "Tell me some good news about BUSINESS.")
})

bad_news_prompt = ChatPromptTemplate.from_messages({
    ("system", "You are a realistic news generator."),
    ("human", "Tell me some bad news about BUSINESS.")
})

chain_good_news = good_news_prompt | llm | str_parser
chain_bad_news = bad_news_prompt | llm | str_parser


parallel_chain = RunnableParallel(
    branches={
        "good": chain_good_news,
        "bad": chain_bad_news
    }
)

results_parallel = parallel_chain.invoke({})

print("Good News:", results_parallel['good'])
print("Bad News:", results_parallel['bad'])