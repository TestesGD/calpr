from flask import Flask, render_template, request, jsonify,url_for,session,redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from db import *
from app import Concreto

app = Flask(__name__)
app.secret_key = 'segredo'
"""""
limiter = Limiter(
    get_remote_address,app=app,default_limits=['2 per minute']
)
"""

@app.route('/')
def index():
    area_tri = session.pop('area_tri', None)
    area_ret = session.pop('area_ret', None)
    area_c = session.pop('area_c', None)
    pecas_result = session.pop('pecas_result', None)

    return render_template(
        'index.html',
        area_tri=area_tri,
        area_ret=area_ret,
        area_c=area_c,
        pecas_result=pecas_result
    )

@app.route('/area_tri' , methods=['POST'])
def home():
    base = request.form.get('base', type=float)
    altura = request.form.get('altura', type=float)
    
    if base is None or altura is None:
        return redirect(url_for('index'))

    try:
        concreto = Concreto(base=base, altura=altura)
        area = concreto.area_tri()
        session['area_tri'] = area  
        return redirect(url_for('index'))
    except ValueError:
        return jsonify({"error": "Dados inválidos ou tempo de resposta excedido."}), 400


@app.route('/area_ret', methods=['POST'])
def area_ret():
    base = request.form.get('base', type=float)
    altura = request.form.get('altura', type=float)

    if base is None or altura is None:
       return redirect(url_for('index'))
    
    
    concreto = Concreto(base=base, altura=altura)
    area = concreto.area_ret()
    session['area_ret'] = area  
    return redirect(url_for('index'))
@app.route('/area_c', methods=['POST'])
def area_c():
    raio = request.form.get('raio', type=float)
    
    if raio is None:
        return redirect(url_for('index'))
    
    concreto = Concreto(raio=raio)
    area = concreto.area_c()
    session['area_c'] = area  
    return redirect(url_for('index'))
@app.route('/pecas', methods=['POST'])
def calcular_pecas():
    area = request.form.get('area', type=float)
    largura = request.form.get('largura', type=float)
    altura = request.form.get('altura', type=float)
    tipo = request.form.get('tipo')

    if None in (area, largura, altura) or not tipo:
        return redirect(url_for('index'))

    resultado = Concreto.calcular_pecas(area, largura, altura, tipo)

    session['pecas_result'] = resultado  
    return redirect(url_for('index'))
@app.route('/db', methods = ['GET','POST'])
def db():
    if request.method == 'POST':
        nome = request.form.get('nome')
        
        email = request.form.get('email')

        adicionar(nome,email)
        return redirect(url_for('db'))
    lista =busca_usuarios()
    return render_template('segunda.html', usuarios= lista)
@app.route('/db/pesquisar', methods=['POST'])
def pesquisar_usuario():

    nome = request.form.get('nome')

    usuarios = pesquisa(nome)

    return render_template('segunda.html', usuarios=usuarios)
@app.route('/db/deletar/<int:id>')
def deletar(id):
    excluir(id)
    return redirect(url_for('db'))
@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):

    nome = request.form.get('nome')
    email = request.form.get('email')

    atualizar_usuario(id,nome,email)

    return redirect(url_for('db'))

@app.route('/editar/<int:id>')
def editar (id):
    usuario = editara(id)
    return render_template('editar.html', usuario=usuario)
if __name__ == '__main__':
    app.run(debug=True) 