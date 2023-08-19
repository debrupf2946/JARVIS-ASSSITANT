import os
import openai
from config import apikey



openai.api_key = apikey
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an email to boss for resignation\n\nSubject: Resignation\n\nDear [Name],\n\nI am writing to formally inform you that I am resigning from my position as [position] effective [date]. This decision was not made easily, but it is the best decision for my career and personal growth.\n\nWorking for [organization] has been an invaluable experience for me, and I am grateful for the professional development and opportunities I have been able to receive.\n\nI am more than willing to assist with the transition process, and I am available to answer any questions you may have.\n\nThank you for this wonderful opportunity.\n\nSincerely,\n[Your Name]",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)