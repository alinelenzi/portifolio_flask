from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

@app.route('/curriculo')
def curriculo():
    return render_template("curriculo.html")

@app.route('/projetos')
def projetos():
    return render_template("projetos.html")

if __name__== 'main':
    app.run(debug=True)