from flask import Flask, request
from user_methods.pf_manage import PFManage

cds_api = Flask(__name__)

@cds_api.route("/pfuser", methods=['POST', 'GET'])
def pfuser_route():
    respose = PFManage(request).direct_method()
    return respose
    
@cds_api.route("/pjuser", methods=['POST', 'GET'])
def pjuser_route():
    return 'None'

cds_api.run()