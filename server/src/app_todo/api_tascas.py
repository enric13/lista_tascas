#!/usr/bin/python3

import flask
import app_tasques
import tasca
import json

app = flask.Flask(__name__)

core_app =app_tasques.App_tasques()
@app.route("/tasks/<id>", methods=["DELETE"])
def delete_task(id):
    resultat = core_app.esborra_tasca(id)
    return "", 204

@app.route("/tasks", methods=["POST", "GET", "PUT"])
def tasks():
    if flask.request.method == "POST":
        info_body = flask.request.get_data()    #info_body = '{"title": "hola"}' -> str
        tasca_nova = json.loads(info_body)      #tasca_nova = '{"title": "hola"}' -> diccionary
        objecte_tasca = tasca.Tasca(None, tasca_nova["title"]) #objecte_tasca -> tasca.Tasca
        resultat = core_app.afegeix_tasca(objecte_tasca)
        return "", 201
        llista_json = []
    elif flask.request.method == "PUT":
        info_body = flask.request.get_data()     #info_body = '{"title": "hola"}' -> str
        tasca_nova = json.loads(info_body)       #tasca_nova = '{"title": "hola"}' -> diccionary
        objecte_tasca = tasca.Tasca(
            None, tasca_nova["title"],
            tasca_nova["done"],
            tasca_nova["id"])
        resultat = core_app.modifica_tasca(objecte_tasca)
        return "", 204
        llista_json = []
    elif flask.request.method == "GET":
        llista_json = []
        llista_tasques = core_app.llegir_tasques()
        for t in llista_tasques:
            tasca_json = str(t)
            tasca_diccionary = json.loads(tasca_json)
            llista_json.append(tasca_diccionary)
        return flask.jsonify(llista_json), 200

app.run()
                                                
          