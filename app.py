from flask import Flask, render_template, request, redirect
import json


app = Flask(__name__)

ARQUIVO = 'database/dados.json'


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():

    if request.method == 'POST':

        contatos = ler_contatos()

        novo_contato = {
            'nome': request.form['nome'],
            'telefone': request.form['telefone'],
            'email': request.form['email']
        }

        contatos.append(novo_contato)

        salvar_contatos(contatos)

        return redirect('/listar')

    return render_template('cadastrar.html')



@app.route('/listar')
def listar():

    contatos = ler_contatos()

    return render_template('listar.html', contatos=contatos)



@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    contatos = ler_contatos()

    if request.method == 'POST':

        contatos[id]['nome'] = request.form['nome']
        contatos[id]['telefone'] = request.form['telefone']
        contatos[id]['email'] = request.form['email']

        salvar_contatos(contatos)

        return redirect('/listar')

    contato = contatos[id]

    return render_template('editar.html', contato=contato, id=id)



@app.route('/remover/<int:id>')
def remover(id):

    contatos = ler_contatos()

    contatos.pop(id)

    salvar_contatos(contatos)

    return redirect('/listar')


if __name__ == '__main__':
    app.run(debug=True)
