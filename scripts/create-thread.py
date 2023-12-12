
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


client = OpenAI()
solFile = open("PasswordStore.sol", "r")
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": solFile.read(),
    }
  ]
)
threadsFile = open("threads.txt\n", "w")
threadsFile.write(thread.id)

