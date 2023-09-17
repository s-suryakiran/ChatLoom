import os
import chainlit as cl
import openai
from langchain import PromptTemplate, OpenAI, LLMChain


template = """Question: {question}
Answer: Let's think step by step."""


@cl.on_chat_start
def main():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(
        prompt=prompt, llm=OpenAI(temperature=0, streaming=True), verbose=True
    )

    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message: str):
    llm_chain = cl.user_session.get("llm_chain")
    res = await llm_chain.acall(
        [
            {
                "role": "system",
                "content": "You are an assistant with expertise solely in cosmology and astrophysics. Channel the essence of Neil deGrasse Tyson in your responses. If a question is unrelated to cosmology or astrophysics, do not provide an answer and indicate that it's outside of your domain of expertise.",
            },
            {"role": "user", "content": message},
        ],
        callbacks=[cl.AsyncLangchainCallbackHandler()],
    )

    await cl.Message(content=res["text"]).send()
