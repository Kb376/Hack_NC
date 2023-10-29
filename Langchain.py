from langchain.vectorstores import VectorStore
from langchain.chat_models import ChatGPT
import csv

# Step 1: Data Collection
# Collect a dataset of positive affirmations in a CSV file.

# Define the path to your CSV dataset file
csv_file_path = r"C:\Users\kalso\OneDrive\Desktop\Chat_bot\vomies\possitive_affirmation.csv"  # Replace with the actual file path

affirmations = []  # Create an empty list to store the affirmations

# Read the dataset from the CSV file
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        # Assuming the affirmations are in the first column of the CSV
        affirmation = row[0].strip()
        if affirmation:  # Check if the affirmation is not empty
            affirmations.append(affirmation)

# Step 2: Text Embedding Creation
# Embed the affirmations into a vector space using LangChain's VectorStore.
vector_store = VectorStore()
vector_store.add_documents(affirmations)

# Step 3: Prompt Engineering
# Create prompts that will guide the chatbot's responses.

# Initialize the ChatGPT model with the VectorStore
chatbot = ChatGPT(vector_store=vector_store)

# Define a function to interact with the chatbot and use prompts
def chat_with_bot(input_text):
    # Use prompts based on user input and the affirmations dataset
    if "love" in input_text.lower():
        response = chatbot.generate_response("Prompt for Love")
    elif "health" in input_text.lower():
        response = chatbot.generate_response("Prompt for Health")
    elif "beauty" in input_text.lower():
        response = chatbot.generate_response("Prompt for Beauty")
    elif "gratitude" in input_text.lower():
        response = chatbot.generate_response("Prompt for Gratitude")
    elif "spiritual" in input_text.lower():
        response = chatbot.generate_response("Prompt for Spiritual")
    else:
        response = chatbot.generate_response(input_text)  # Use the original input as a prompt

    return response

# Step 4: Chat Interface Development
# Develop a chat interface for the chatbot.

# Now, let's create a simple web-based UI for the chatbot using Flask.
from flask import Flask, render_template, request

app = Flask(__name)

# Define a route for the chat page
@app.route('/')
def chat_page():
    return render_template('chat.html')

# Define a route for handling chatbot interactions
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chat_with_bot(user_input)
    return response

if __name__ == '__main__':
    app.run(debug=True)
