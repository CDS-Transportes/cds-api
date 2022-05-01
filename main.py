import imp
from flask import Flask, request
from flask_cors import cross_origin
from docs.init_docs import init_docs

from methods.register_method import register_method
from methods.login_method import login_method
from methods.register_perfil_method import register_perfil
from methods.get_perfil_method import get_perfil

cds_api = Flask(__name__)
init_docs(cds_api)

@cds_api.route("/api/v1/register", methods=['POST'])
@cross_origin()
def register_route():
    respose = register_method(request)
    return respose


@cds_api.route("/api/v1/login", methods=['GET'])
@cross_origin()
def login_route():
    respose = login_method(request)
    return respose


@cds_api.route("/api/v1/update_perfil", methods=['POST'])
@cross_origin()
def update_perfil_route():
    respose = register_perfil(request)
    return respose


@cds_api.route("/api/v1/get_perfil", methods=['GET'])
@cross_origin()
def get_perfil_route():
    respose = get_perfil(request)
    return respose



cds_api.run()