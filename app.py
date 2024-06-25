from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def fondo():
    return render_template('fondo.html')

@app.route('/animacion')
def animacion():
    return render_template('animacion.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/CV')  # Define una función de vista para '/CV'
def cv():
    return render_template('CV.html')

if __name__ == '__main__':
    app.run(debug=True)
