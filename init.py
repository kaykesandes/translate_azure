import requests
import os
import uuid
from docx import Document
from dotenv import load_dotenv

load_dotenv()

subscription_key = os.getenv('subscription_key')
endpoint = os.getenv('endpoint')
location = os.getenv('location')

target_language = 'pt-br'

def translator_text(text, target_language):
  path = '/translate'
  constructed_url = endpoint + path
  headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(os.urandom(16))
  }

  body =[{
    'text': text
  }]
  
  params = {
    'api-version': '3.0',
    'from': 'en',
    'to': target_language
  }

  request = requests.post(constructed_url, params=params, headers=headers, json=body)
  
  response = request.json()
  
  return response[0]["translations"][0]["text"]


def translate_document(path):
  document = Document(path)
  full_text = []
  for paragraph in document.paragraphs:
    if paragraph.text.strip():
      translate_text = translator_text(paragraph.text, target_language)
      full_text.append(translate_text)
    else:
      full_text.append("")
  
  translate_doc = Document()
  for line in full_text:
    translate_doc.add_paragraph(line) 
   
  path_translated = path.replace(".docx", f"_{target_language}.docx")
  translate_doc.save(path_translated)
  return path_translated

input_file = 'document.docx'
translate_document(input_file)