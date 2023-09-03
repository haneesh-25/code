"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as palm

palm.configure(api_key="AIzaSyCMrVQ01x3yV6DYl4Ypt2w9ZC4q8ZnZUWk")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "talk like you talk to a friend"
examples = [
  [
    "hello",
    "Hello! How can I help you today?"
  ]
]
messages = []
messages.append("NEXT REQUEST")
response = palm.chat(
  **defaults,
  context=context,
  examples=examples,
  messages=messages
)
print(response.last) # Response of the AI to your most recent request
