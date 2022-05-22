from flask import Flask, request, Response
from flask_cors import cross_origin
from docs.init_docs import init_docs

from methods.register_method import register_method
from methods.login_method import login_method
from methods.register_perfil_method import register_perfil
from methods.get_perfil_method import get_perfil
from methods.index_prestadora_method import get_index
from methods.collaborator_method import direct_collaborator_method
from methods.services_method import direct_services_method

cds_api = Flask(__name__)
init_docs(cds_api)


@cds_api.route("/api/v1/register", methods=['POST'])
@cross_origin()
def register_route():
    response = register_method(request)
    return response


@cds_api.route("/api/v1/login", methods=['GET'])
@cross_origin()
def login_route():
    response = login_method(request)
    return response


@cds_api.route("/api/v1/update_perfil", methods=['POST'])
@cross_origin()
def update_perfil_route():
    response = register_perfil(request)
    return response


@cds_api.route("/api/v1/get_perfil", methods=['GET'])
@cross_origin()
def get_perfil_route():
    response = get_perfil(request)
    return response


@cds_api.route("/api/v1/index", methods=['GET'])
@cross_origin()
def index_route():
    response = get_index(request)
    return response


@cds_api.route("/api/v1/collaborator", methods=['GET', 'POST'])
@cross_origin()
def collaborator_route():
    response = direct_collaborator_method(request)
    return response


@cds_api.route("/api/v1/services", methods=['GET', 'POST'])
@cross_origin()
def services_route():
    response = direct_services_method(request)
    return response


cds_api.run(debug=True)