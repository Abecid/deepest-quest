import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Define the OpenAI API parametersx
# openai.api_key = '<YOUR_OPENAI_API_KEY>'
openai.api_key = os.environ.get('OPENAI_API_KEY')

def chatGPT(chat_history):
    engine = "gpt-3.5-turbo"
    system = "You are a helpful assistant. You classify the likelihood of whether the given tweets are spam or not by outputing a number from 0 to 100 where 0 is the least likely to be spam and 100 is the most likely to be spam. Refer to the examples below and return your classification values for the given tweets."
    messages = [
        {"role": "system", "content": system},
    ]
    
    messages = messages + chat_history
    
    response = openai.ChatCompletion.create(
        model = engine,
        messages = messages,
    )
    answer = response.choices[0].message.content
    return answer

class customChatGPT:
    def __init__(self, engine, system):
        self.engine = engine
        self.system = system
        self.messages = [{"role": "system", "content": self.system}]

    def chat(self, message):
        # print(self.messages)
        self.messages.append({"role": "user", "content": message})
        
        # print(self.messages)

        response = openai.ChatCompletion.create(
            model = self.engine,
            messages = self.messages,
        )
        answer = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": answer})
        return answer