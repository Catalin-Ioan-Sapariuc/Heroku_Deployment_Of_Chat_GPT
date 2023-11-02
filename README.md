# Website

This website is built using Flask, HTML, CSS, SQL and OpenAI GPT3 

### Pre-requisites:

OPENAI_API_KEY can be set with export OPENAI_API_KEY = value (command line) 
or use openai.api_key = key as a local variable straight into the app.py file 

### Name of the project: "

Creating a Flask WebApp for the OpenAI GPT3 engine"

### Idea of the project:

I used Flask, HTML, CSS, SQL and OpenAI GPT3 to create a Web App (an interface) to the OpenAI GPT3 Engine.
This web app has a nice interface beautified with bootstrap and also has login, logout and regitration capabilities. 
There are 3 main directories in the project:
1. static, which holds the styles.css file
2. templates which holds the following html files:
answer.html, apology.html, index.html, layout.html, login.html and register.html. 
The use case of each pf these files should be obvious, especially if you are
familiar with Problem Set 9 of CS50. 
3. the main direvtory which contains the driver file app.py , the helper file helpers.py as well as the sqlite database database.db. 

In this database, which can be open with sqlite3 database.db or with PHPLiteAdmin (although the first method is prefered) we store the credentials for the registered users: in a table users with columns : id (primary key, username, and hash (a hashed password, for security purposes)). 

app.py creates the following routes: / (which points to the index page and the redirection page after the user ahs logged in, /login route which points to the login page, /logout route points to logout, the /register route which points to the registration page and finally the /answer route which points to the answer given by GPT3. 

To start the app, you do:
flask run in the main directory. 
Then you are given a chance to register, create a username , password and password confirmation. 
If password == confirmation, this will add a new user, password entry in the users table in database.db, and you will 
be redirected to the index.html in which you can ask a question. 

Example of questions are:
I. Who is Albert Camus? 
GPT3 answers: 
Albert Camus (1913-1960) was a French philosopher, author, and journalist. He is best known for his works of fiction, including The Stranger (1942), The Plague (1947), The Myth of Sisyphus (1942), and The Fall (1956). He was awarded the Nobel Prize in Literature in 1957. His philosophical views were heavily influenced by existentialism and absurdism, and he is often associated with the philosophy of nihilism.
II. Who is Klaus Johannis?
GPT3 answers:
Klaus Johannis is the current President of Romania. He was elected in 2014 and re-elected in 2019. He is a member of the National Liberal Party and has served as mayor of Sibiu from 2000 to 2014. 

Note that these answers are linked to my own OPENAI_API_KEY, therefore for your usage you shall create your own OPENAI_API_KEY from 
https://platform.openai.com/ . 
Note also that this technology (large language models) in this case developed by Open AI is constantly evolving and therefore 
you shall stay in touch and perhaps try other models as well (such as turbo-gpt-3.5 or gpt4) although I am not sure at this time about the costs. 

This particular APP which I have built here can be extended in a few directions (further work):
 -- allow user to control parameters of the openai.completion.create call such as :
 engine, max_tokens, temperature, top_p or presence_penalty . 
 You can read about the potential effect of each parameter on OPENAI 's site. 
 -- allow user to train a model on a particular topic in order to obtain better results .
 The best way to train a model in my experience is by doing a few shots training, as opposed 
 to fine-tuning. Few shots training means basically to pre-pend the actual query with a few (shots) examples
 of (prompt, completion) which ultimately has the effect of teaching the model how to best answer these 
 particular questions. More details on this matter can be found in the main GPT3 paper: 
"Language Models are Few-Shot Learners " by T. Brown and (many) others. 
-- extend the scope of the project through training or other directions and organize the site accordingly.
-- create more functionality or better esthetic for this site using bootstrap or Javascript as needed.  


Please let me know of your opinion regarding this project. Enjoy! 



