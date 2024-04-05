<<<<<<< HEAD
from flask import Flask, redirect, render_template, request, flash


app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')



@app.route('/guia_de_raca')
def guia_de_raca():
    return render_template('guia_de_raca.html')




@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    email = request.form.get('email')
    print(nome,senha,email)

    return redirect('/guia_de_raca')


if __name__ == '__main__':
    app.run(debug = True)

=======
>>>>>>> upstream/main
