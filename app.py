from flask import Flask, request, jsonify
import repositorio as rp
import json

app = Flask(__name__)


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = json.loads(request.data)
    rp.inserir_produto(dados)
    return jsonify({'Status': 'Produto Cadastrado com Sucesso'})


@app.route('/produtos', methods=['GET'])
def produtos():
    return jsonify(rp.listar_produtos())


@app.route('/produto/<int:codigo>', methods=['GET'])
def buscar_produto(codigo):
    return jsonify(rp.listar_produto(codigo))


@app.route('/deletar/<int:codigo>', methods=['DELETE'])
def deletar_produto(codigo):
    return jsonify(rp.deletar_produto(codigo))


@app.route('/alterar/<int:codigo>', methods=['PUT'])
def alterar_produto(codigo):
    dados = json.loads(request.data)
    return jsonify(rp.alterar_produto(codigo, dados['nome'], dados['preco'], dados['quantidade']))


if __name__ == '__main__':
    app.run(debug=True)
