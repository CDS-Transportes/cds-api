from flask import Flask, request
from flask_cors import cross_origin
from user_methods.pf_manage import PFManage

cds_api = Flask(__name__)

@cds_api.route("/pfuser", ethods=['POST', 'GET'])
@cross_origin()
def pfuser_route():
    respose = PFManage(request).direct_method()
    return respose

@cds_api.route("/pjuser", methods=['POST', 'GET'])
@cross_origin()
def pjuser_route():
    return 'None'

cds_api.run()