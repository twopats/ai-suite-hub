import autogen
import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

load_dotenv()



from openai import OpenAI

# config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
# assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
# user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

from fastapi import FastAPI


client = OpenAI(
)

file = open("PasswordStore.sol", "r")

thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": file.read(),
    }
  ]
)

print(f"new thread created: {thread.id}")

# run = client.beta.threads.runs.create(
#   thread_id=thread.id,
#   assistant_id='asst_SyIj641ROGRHXivIxLeOAbf2',
#     model="gpt-3.5-turbo-1106",
# )
#
# run = client.beta.threads.runs.retrieve(
#   thread_id=thread.id,
#   run_id=run.id
# )
#
# messages = client.beta.threads.messages.list(
#   thread_id=thread.id
# )
#
# print(messages)


# app = FastAPI()
#
# @app.get("/")
# def read_root():
#     return {"Trust": "Bytes"}
#
# @app.get("/api/v1/analyze")
#
# if __name__ == "__main__":
#     import uvicorn
#
#     # Run the FastAPI app using Uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
