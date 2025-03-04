from google import genai
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = 'YOUR_API_KEY' #Use GEMINI AI's API KEY

def chatbot(prompt):
    client = genai.Client(api_key="YOUR_API_KEY") #Use GEMINI AI's API KEY

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response.text

@app.route('/', methods=['GET', 'POST'])
def bot():
    chat = None
    res = None
    if request.method == 'POST':

        chat = request.form.get('chat')
        if chat:
            res = chatbot(chat)
    return render_template('index.html', user_chat=chat, bot_response=res)


if __name__ == '__main__':
    app.run(debug=True)
