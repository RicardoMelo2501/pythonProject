from flask import Flask, app, request
from flask.json import jsonify
import json

app = Flask(__name__)

recepies = [
    {
        "title": "cake",
        "igredients": [
            "igredients01"
            "igredients02"
            "igredients03"
        ],

        "modo": "modo01",
        "Redimento": "Redimento01"

    },

]


@app.route("/cadastroRecepies", methods=["POST", "GET"])
def Cadastro():
    if request.method == "GET":
        return jsonify(recepies)
    elif request.method == "POST":
        newcadastro = json.loads(request.data)
        recepies.append(newcadastro)
        return jsonify({
            "menssagem": "Cadastrado",
            "newValue": newcadastro

        })


@app.route('/cadastroRecepies/<int:indice>', methods=['GET', 'PUT', 'DELETE'])
def cadastroID(indice):
    try:
        recepies[indice]
    except IndexError:
        message = 'Receita ID {} Não Encontrada'.format(indice)
        return jsonify({
            "message": message,
            "status": "Error!"
        })
    except:
        message = 'Aconteceu um erro inesperado'
        return jsonify({
            "message": message,
            "status": "Error!"
        })

    if request.method == 'GET':
        return recepies[indice]

    elif request.method == 'PUT':

        newValue = json.loads(request.data)

        recepies[indice] = newValue
        return jsonify({
            "message": "Updated!",
            "newValue": newValue
        })

    elif request.method == 'DELETE':
        print(indice)
        recepies.pop(indice)
        return jsonify({
            "message": "Deleted!",
            "arrayAtual": recepies
        })


if __name__ == '__main__':
    app.run(debug=True)
  
