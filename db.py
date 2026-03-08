import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1516',
    database = 'civil'

)
def adicionar(name, email):
    curso = conexao.cursor()
    curso.execute('insert into usuario (nome,email) values (%s,%s)',(name,email))

    conexao.commit()

    curso.close()

def busca_usuarios():
    curso = conexao.cursor()

    curso.execute('select*from usuario')

    usuarios = curso.fetchall()
    curso.close()
    return usuarios
def pesquisa(nome):
    curso = conexao.cursor()
    curso.execute('select*from usuario where nome like %s',(f'%{nome}%',))

    usuarios = curso.fetchall()
    curso.close()
    return usuarios
def excluir(id):
    curso = conexao.cursor()
    curso.execute('delete from usuario where id = %s',(id,))
    conexao.commit()
    curso.close()

def editara(id):
    curso = conexao.cursor()
    curso.execute('select*from usuario where id =%s',(id,))
    usuario = curso.fetchone()
    curso.close()
    return usuario
def atualizar_usuario(id,nome,email):
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE usuario SET nome=%s,email=%s WHERE id=%s",
        (nome,email,id)
    )
    conexao.commit()
    cursor.close()