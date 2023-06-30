banco_produtos = []


def inserir_produto(produto):
    banco_produtos.append(produto)


def listar_produtos():
    return banco_produtos


def listar_produto(codigo):
    for produto in banco_produtos:
        if produto['codigo'] == codigo:
            return produto
    return {'Status': 'Produto não cadastrado'}


def deletar_produto(codigo):
    for produto in banco_produtos:
        if produto['codigo'] == codigo:
            pos = banco_produtos.index(produto)
            banco_produtos.pop(pos)
            return {'Status': 'Produto deletado com sucesso'}
    return {'Status': 'Produto não cadastrado'}


def alterar_produto(codigo, nome, preco, quantidade):
    for produto in banco_produtos:
        if produto['codigo'] == codigo:
            produto['nome'] = nome
            produto['preco'] = preco
            produto['quantidade'] = quantidade
            return {'Status': 'Produto atualizado com sucesso'}
    return {'Status': 'Produto não cadastrado'}
