# app.py
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar-carrinho', methods=['POST'])
def adicionar_carrinho():
    data = request.json
    produto = data.get('produto')

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO carrinho (produto, quantidade) VALUES (?, ?)', (produto, 1))
    conn.commit()
    conn.close()

    return jsonify({'mensagem': f'{produto} adicionado ao carrinho!'})

if __name__ == '__main__':
    app.run(debug=True)
