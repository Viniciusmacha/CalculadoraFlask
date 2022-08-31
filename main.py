from flask import Flask, render_template
from flask import request, redirect
from calculadora import calculadora
import this


app = Flask(__name__)#Referencia ao objeto Flask, criando uma variavel APP que guarda os elementos Flask
calc = calculadora()
this.resultadoFinal= ""

@app.route("/")#Página de Qualquer Site
def homepage():
    return render_template("index.html")

@app.route("/soma", methods=['POST','GET'])
def soma():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.somar(numero1,numero2)
    return render_template("soma.html", titulo= "soma", resultado=this.resultadoFinal)

@app.route("/subtracao", methods=['POST','GET'])
def subt():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.subtrair(numero1,numero2)
    return render_template("subtracao.html", titulo= "subtrair", resultado=this.resultadoFinal)   


@app.route("/divisao", methods=['POST','GET'])
def div():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.dividir(numero1,numero2)
    return render_template("divisao.html", titulo= "dividir", resultado=this.resultadoFinal)

@app.route("/multiplicacao", methods=['POST','GET'])
def mult():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.multiplicar(numero1,numero2)
    return render_template("multiplicacao.html", titulo= "multiplicar", resultado=this.resultadoFinal)


@app.route("/potencia", methods=['POST','GET'])
def pot():
    if request.method == 'POST':
        numero1 = request.form['num1']
        numero2 = request.form['num2']
        this.resultadoFinal = calc.potencia(numero1,numero2)
    return render_template("potencia.html", titulo= "potencia", resultado=this.resultadoFinal)   


@app.route("/raiz", methods=['POST','GET'])
def rai():
    if request.method == 'POST':
        numero1 = request.form['num1']

        this.resultadoFinal = calc.raiz(numero1)
    return render_template("raiz.html", titulo= "raiz", resultado=this.resultadoFinal)    

@app.route("/tabuada", methods=['POST','GET'])
def tabu():
    if request.method == 'POST':
        numero1 = request.form['num1']
        this.resultadoFinal = calc.tabuada(numero1)
    return render_template("tabuada.html", titulo= "tabuada", resultado=this.resultadoFinal)        

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

