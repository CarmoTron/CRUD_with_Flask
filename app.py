from flask import Flask, render_template, request, redirect, url_for
from model import db, Empregado

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_table():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

# CREATE
@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        id_empregado = request.form['id_empregado']
        nome = request.form['nome']
        idade = request.form['idade']
        posicao = request.form['posicao']
        
        empregado = Empregado(id_empregado=id_empregado, nome=nome, idade=idade, posicao=posicao)

        try:
            db.session.add(empregado)
            db.session.commit()
            return redirect(url_for('find_data_list'))
        except Exception as e:
            return f"Houve um problema ao adicionar o empregado: {e}"
    
    return render_template('createpage.html')

# READ
@app.route('/data')
def find_data_list():
    empregados = Empregado.query.all()
    return render_template('datalist.html', empregados=empregados)

@app.route('/data/<int:id>')
def find_single_empregado(id):
    empregado = Empregado.query.get_or_404(id)
    return render_template('data.html', empregado=empregado)

# UPDATE
@app.route('/data/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    empregado = Empregado.query.get_or_404(id)
    if request.method == 'POST':
        empregado.nome = request.form['nome']
        empregado.idade = request.form['idade']
        empregado.posicao = request.form['posicao']
        
        try:
            db.session.commit()
            return redirect(url_for('find_single_empregado', id=id))
        except Exception as e:
            return f"Houve um problema ao atualizar o empregado: {e}"
    
    return render_template('update.html', empregado=empregado)

# DELETE
@app.route('/data/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    empregado = Empregado.query.get_or_404(id)
    if request.method == 'POST':
        try:
            db.session.delete(empregado)
            db.session.commit()
            return redirect(url_for('find_data_list'))
        except Exception as e:
            return f"Houve um problema ao eliminar o empregado: {e}"
    
    return render_template('delete.html', empregado=empregado)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
