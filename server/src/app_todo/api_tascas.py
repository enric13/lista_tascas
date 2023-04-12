#!/usr/bin/python3

import flask
import app_tasques
import tasca
import json

app = flask.Flask(__name__)

core_app =app_tasques.App_tasques()

@app.route("/tasks", methods=["POST", "GET"])

def tasks():
    if flask.request.method == "POST":
        info_body = flask.request.get_data()    #info_
        tasca_nova = json.loads(info_body)
        objecte_tasca = tasca.Tasca(None, tasca_nova["title"])
        resultat = core_app.afegeix_tasca(objecte_tasca)
        return "", 201
    elif flask.request.method == "GET":
        llista_json = []
        llista_tasques = core_app.llegir_tasques()
        for t in llista_tasques:
            tasca_json = str(t)
            tasca_diccionary = json.loads(tasca_json)
            llista_json.append(tasca_diccionary)
        return flask.jsonify(llista_json), 200

app.run()
                                                
          