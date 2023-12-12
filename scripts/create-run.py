import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()

threadId = open("threads.txt", "r").read()


run = client.beta.threads.runs.create(
  thread_id=threadId,
  assistant_id='asst_SyIj641ROGRHXivIxLeOAbf2',
)

open("runs.txt", "w").write(run.id)
print(f"new run created: {run.id}, writing to runs.txt")
