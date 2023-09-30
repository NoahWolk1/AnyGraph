'''import openai

openai.api_key = "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"

def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        tempeinstarature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

user_prompt = "Write a summary of the benefits of exercise."
chatbot_response = chat_with_chatgpt(user_prompt)
print(chatbot_response)'''
import openai
import os

openai.api_key = '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'

independentVariable = input("Independent Variable: ")
dependentVariable = input("Depedent Variable: ")
'''
completion = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role': 'assistant', 'content': 'What is the possible changing variable of this phrase: money spent on pokemon'}
  ],
  temperature = 0  
)

print(completion['choices'][0]['message']['content'])
'''
