
from fastapi import FastAPI, HTTPException


app = FastAPI()

usuario = [
    {"nome": "Dolly", "email": "dollyna@gmail.com", "id": 1}
]

produtos = [
    {"item" : "petisco", "item_id": 1, "descricao": None, "preco": 30, "qty" : 3},
    {"item" : "ração", "item_id": 2, "descricao": None, "preco": 210, "qty" : 1},
    {"item" : "patê", "item_id": 3, "descricao": None, "preco": 10, "qty" : 5}
]

carrinho = [
    {"user_id": 3, "item_id": 1, "qty": 2, "preco": 200},
    {"user_id": 3, "item_id": 2, "qty": 5, "preco": 100}
]

endereco = [
    {"rua": "rua da Dolly", "cep": "1234", "cidade": "Altinopolis", "estado": "SP", "address_id": 1, "user_id": 1},
    {"rua": "rua da Molly", "cep": "1234", "cidade": "Altinopolis", "estado": "SP", "address_id": 2, "user_id": 1}
]

#---------------------------------------------- Página inicial de saudações --------------------------
@app.get("/")
async def saudacoes():
    site = "Saudações! Sejam bem-vindas e bem-vindos :)"
    return site


#------------------------------------------------------- Usuario ----------------------------------------------
@app.post('/create_user/', status_code=201) #criando os usuários 
async def add_user(user : dict):

    for temp_user in usuario:
        if temp_user['nome'] == user['nome']:
            raise HTTPException(status_code=400, detail= f"{user['nome']} já existe!")

    usuario.append(user)
    
    return f"{user['nome']} adicionado (a) corretamente!"

@app.post('/users/{user_id}/endereco/{address_id}', status_code=201) #criando os endereços dos usuários 
async def add_user_address(user_address : dict) -> dict:
    endereco.append(user_address)
    return f"Endereço do usuário adicionado corretamente!"


@app.get('/users', status_code=200) #pegando todos usuários cadastrados
async def get_users() -> dict:
    return {"Usuários": usuario}

@app.get('/users/{user_id}', status_code=200) #pegando um usuario pelo id 
async def get_users(user_id: int):
    for temp_user in usuario:
        if temp_user['id'] == user_id:
            return f"Usário com id {user_id} existe"

    raise HTTPException(status_code=404, detail=f"Usuário com id {user_id} não encontrado!")

@app.get('/users/name/{user_name}', status_code=200) #pegando um usuario pelo nome
async def get_users_name(user_name: str):
    for temp_user in usuario:
        if temp_user['nome'] == user_name:
            return f"Usuário com nome {user_name} existe"

    raise HTTPException(status_code=404, detail=f"Usuário com nome {user_name} não encontrado!")

@app.delete('/delete/{user_id}',status_code=200) #removendo um usuário pelo id
async def delete_user(user_id: int):
    for temp_user in usuario:
        if temp_user['id'] == user_id:
            usuario.remove(temp_user)
            return f"Usuário com id {user_id} corretamente deletado!"

    raise HTTPException(status_code=404, detail=f"Usuário com id {user_id} não encontrado!")

@app.get('/users/{user_id}/endereco/{address_id}', status_code=200) #pegando um endereço de usuario
async def get_users_address(user_id: int):
    ends = []
    for i in endereco:
        if i['user_id'] == user_id:
            ends.append(i)
    return {"Endereços do usuário":ends}

@app.delete('/delete/usuario/{user_id}/endereco/{address_id}',status_code=200) #removendo um endereço de usuário pelo id
async def delete_endereco(address_id: int):
    for temp_address in endereco:
        if temp_address['address_id'] == address_id:
            endereco.remove(temp_address)
            return f"Endereço com id {address_id} corretamento deletado!"

    raise HTTPException(status_code=404, detail=f"Endereço com id {address_id} não encontrado!")


#----------------------------------------------------- Cadastro de items ---------------------------------------------------------
@app.post('/create_item', status_code=200) #cadastrando produtos
async def register_item(item : dict):

    for temp_item in produtos:
        if temp_item['item'] == item['item']:
            raise HTTPException(status_code=400, detail= f"{item['item']} já registrado!")

    produtos.append(item)
    
    return f"{item['item']} adicionado corretamente!"

@app.get('/items', status_code=200) #pegando todos os itens cadastrados
async def get_items():
    return {"Produtos": produtos}

@app.delete('/delete_item/{item_id}',status_code=200) #removendo um produto pelo código id
async def delete_item(item_id:int):
    for temp_item in produtos:
        if temp_item['item_id'] == item_id:
            produtos.remove(temp_item)
            return f"Item com id {item_id} corretamente deletado!"

    raise HTTPException(status_code=404, detail=f"Item com id {item_id} não encontrado!")


#------------------------------------------------------ Carrinho de compras ---------------------------------------------------------
@app.post('/carrinho/{user_id}/{item_id}/', status_code=201) #criando os carrinhos
async def add_cart(cart: dict):

    for temp_cart in carrinho:
        if temp_cart['user_id'] == cart['user_id']:
            raise HTTPException(status_code=400, detail= f"Carrinho já existe!")

    carrinho.append(cart)
    
    return f"Novo carrinho criado!"

@app.get('/carrinho/{user_id}', status_code=200) #pegando o carrinho de compra associado ao id do usuario 
async def get_carrinho(user_id: int):
    total = 0
    itens = []
    for i in carrinho:
        if i['user_id'] == user_id:
            total += i['qty'] * i['preco']
            itens.append(i)
    return {"Carrinho":itens, "Preço total": total}

@app.post('/carrinho/{user_id}/{item_id}', status_code=200) #adicionando produtos ao carrinho
async def add_item_to_cart(cart : dict):
    carrinho.append(cart)
    
    return f"Novo produto adicionado!"

@app.put('/update_item', status_code=200) #alterando a quantidade dos produtos no carrinho
async def update_item(item_id: int, item_quantity:int, user_id: int):

    for i in carrinho:
        if i['item_id'] == item_id and i['user_id'] == user_id:
            i['qty'] = item_quantity
            return f"Item com id {item_id} corretamente modificado!"

    raise HTTPException(status_code=404, detail=f"Item com id {item_id} não encontrado!")

@app.delete('/carrinho/{user_id}/delete_item/{item_id}',status_code=200) #removendo um produto pelo código id
async def delete_item(user_id: int, item_id: int):
    for temp_item in carrinho:
        if temp_item['item_id'] == item_id and temp_item['user_id'] == user_id:
            carrinho.remove(temp_item)
            return f"Item {item_id} corretamente deletado!"

    raise HTTPException(status_code=404, detail=f"Item with id {item_id} não encontrado!")


@app.delete("/delete/carrinho/{user_id}/", status_code=200) #deletando o carrinho de compras 
async def delete_carrinho(user_id: int):
    for i in carrinho:
        if i['user_id'] == user_id:
            carrinho.remove(i)
            return f"Carrinho corretamente deletado!"
    
    raise HTTPException(status_code=404, detail=f"Usuário não tem carrinho.")