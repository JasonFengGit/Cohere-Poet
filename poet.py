import cohere
import os

api_key = os.environ["COHERE_API_KEY"]
co = cohere.Client(api_key)

message = input("Decription of the poem: ")

prompt = "I want you to act as a poet. You will create poems that evoke emotions and have the power to stir people’s soul. write concisely. answer me with just the poem and nothing else. Write on any topic or theme but make sure your words convey the feeling you are trying to express in beautiful yet meaningful ways. You can also come up with short verses that are still powerful enough to leave an imprint in readers' minds. My first request is a poem about "+ message

# Generate a response with the current chat history
response = co.chat(
    message=prompt,
    temperature=0.8
)
answer = response.text
    
print("Poet:\n"+answer)
print()


