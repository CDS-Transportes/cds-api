from flask import Flask, request
from flask_cors import cross_origin
from user_methods.pf_manage import PFManage
from user_methods.pj_manage import PJManage

cds_api = Flask(__name__)

@cds_api.route("/api/v1/pfuser", methods=['POST', 'GET'])
@cross_origin()
def pfuser_route():
    respose = PFManage(request).direct_method()
    return respose

@cds_api.route("/api/v1/pjuser", methods=['POST', 'GET'])
@cross_origin()
def pjuser_route():
    respose = PJManage(request).direct_method()
    return respose

cds_api.run()