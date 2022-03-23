from flask import Flask

app = Flask(__name__)


@app.route('/')
def Index():
    return 'hola mundo'

@app.route('/add_info')
def add_info():
    return 'agregar informacion'

@app.route('/edit_info')
def edit_info():
    return 'editar informacion'

@app.route('/delete')
def delete_info():
    return 'eliminar informacion'

if __name__ == '__main__':
    app.run(port=9000, debug = True)