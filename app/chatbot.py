from mistralai.client import Mistral
from app.config import MISTRAL_API_KEY, MODEL_NAME


class ChatBot:

    def __init__(self):

        self.client = Mistral(
            api_key=MISTRAL_API_KEY
        )

        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert coding assistant."
                    "Help users with Python, AI, ML, and programming."
                )
            }
        ]

    def get_response(self, user_input):

        # add user message
        self.messages.append({
            "role": "user",
            "content": user_input
        })

        # API request
        response = self.client.chat.complete(
            model=MODEL_NAME,
            messages=self.messages
        )

        # extract response
        assistant_message = response.choices[0].message.content

        # save response
        self.messages.append({
            "role": "assistant",
            "content": assistant_message
        })

        return assistant_message
