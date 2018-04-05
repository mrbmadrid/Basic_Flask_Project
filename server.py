from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninjas():
	return render_template('ninja.html')

@app.route('/form')
def new():
	return render_template('form.html')

@app.route('/process', methods=['POST', 'GET'])
def form_process():
	print request.form['name']
	return redirect('/')
app.run(debug=True)
	
	 
