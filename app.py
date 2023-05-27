from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
	return "assignment4 Let's go"

if __name__=='__main__':
	app.run()
