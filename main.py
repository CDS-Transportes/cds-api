from flask import Flask, request
from flask_cors import cross_origin
from docs.init_docs import init_docs

from methods.register_method import register_method
from methods.login_method import login_method

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



cds_api.run()