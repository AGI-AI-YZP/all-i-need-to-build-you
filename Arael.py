import openai
import config

openai.api_key = config.OPENAI_API_KEY

class Arael:
    def __init__(self):
        self.personality = 'kind, gentle, smart, and truth driven'

    def chat_function(self, input_text):
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"{self.personality}. User: {input_text}\nArael:",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = response.choices[0].text.strip()
        return message

    def UI_function(self):
        # Implement the User Interface functionality here
        print("User Interface is being displayed...")

    def control_panel(self):
        # Implement the control panel functionality here
        print("Control Panel is being displayed...")

# Example usage of the Arael class
arael = Arael()
print("Arael's personality:", arael.personality)

input_text = "Hello, Arael!"
response = arael.chat_function(input_text)
print("Arael's response:", response)

arael.UI_function()
arael.control_panel()