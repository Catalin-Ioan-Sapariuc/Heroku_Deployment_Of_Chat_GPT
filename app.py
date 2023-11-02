#from cs50 import SQL
from flask import Flask, render_template, request
# from flask_session import Session
import openai, os
# from dotenv import load_dotenv

#openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = "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"

app = Flask(__name__)

# this route takes you to the index (main) page to input the question
# it will forward the prompt through the action form to answer.html 

@app.route("/")
def mainroute():
    return render_template("index.html")

@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        print("prompt = \n", prompt)
        engine="text-davinci-003"
        max_tokens=550
        temperature=0.
        top_p=0
        presence_penalty=1
        response =openai.Completion.create(engine=engine,prompt=prompt,max_tokens=max_tokens,
                                       temperature=temperature,top_p=top_p,
                                       presence_penalty=presence_penalty,
                                       stream=False)
        offset=0
        hresponse=response['choices'][0]['text'][offset:]
        print("hresponse = \n", hresponse)
        return render_template('answer.html', prompt=prompt, response=hresponse)
    else:
        return render_template("index.html")        
    

