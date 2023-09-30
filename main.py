import kaggle
import os
import chatgptData
import openai

openai.api_key = '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'

firstStringList  = ""


independentList = (kaggle.api.dataset_list(search=chatgptData.independentVariable))
fullExperiment = (chatgptData.independentVariable + " vs " + chatgptData.dependentVariable)

for i in independentList:
    i = str(i)
    firstStringList += i + ", "

kaggleCompare = ("Find the list " + fullExperiment + "with one of the names in the list:" + firstStringList + ". Only return the name that matches best. Just find the best name, even if you think nothing matches. I only want the name, no other words")


completion = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role': 'assistant', 'content': kaggleCompare}
  ],
  temperature = 0  
)

print(completion['choices'][0]['message']['content'])
