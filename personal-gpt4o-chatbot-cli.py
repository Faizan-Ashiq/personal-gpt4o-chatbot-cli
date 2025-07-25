
from openai import OpenAI
import os

# Use environment variable for the API key
key = os.getenv("OPENAI_API_KEY")
messages = []

client = OpenAI(
    api_key=key,
)

def completion(message):
    global messages
    messages.append(
        {
            'role': 'user',
            'content': message
        }
    )

    chat_completion = client.chat.completions.create(
        messages=messages,
        model='gpt-4o'
    )

    message = {
        'role': 'assistant',
        'content': chat_completion.choices[0].message.content
    }

    messages.append(message)
    print(f"Jarvis : {message['content']}")

if __name__ == '__main__':
    print('Jarvis : how may I help you.')

')
    while True:
        user_question = input()
        print(f'User: {user_question}')
        completion(user_question)
