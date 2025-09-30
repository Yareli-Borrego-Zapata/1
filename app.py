from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return '''
    #inicio:
    <h1>Bienvenido mi calculadora de Python</h1>
    <p>para teclear escribe en el navegador: 127.0.0.1:5000/sumar/10/20</p>
<p>para sumar escribe en el navegador 127.0.0.1:5000/sumar/10/20</p>

<p>para restar escribe en el navegador 127.0.0.1:5000/restar/10/20</p>

<p>para obtener el numero maximo de dos valores,  escribe en el navegador 127.0.0.1:5000/max/10/20</p>


    '''
@app.route('/sumar/<int:n1>/<int:n2>')
def sumar(n1, n2):
    resultado = n1 + n2
    return f'<h1>{n1} + {n2} = {resultado}</h1>'


@app.route('/restar/<int:n1>/<int:n2>')
def restar(n1, n2):
    resultado = n1 - n2
    return f'<h1>{n1} - {n2} = {resultado}</h1>'


@app.route('/max/<int:n1>/<int:n2>')
def mayor(n1,n2 ):
    if n1 > n2:
        mayor = n1
    else:
        mayor = n2
    return f'<h1>El número mayor entre {n1} y {n2} es {mayor}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
