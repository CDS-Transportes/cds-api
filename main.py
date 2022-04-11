from flask import Flask, request

from user_methods.pf_manage import Pf_User



cds_api = Flask(__name__)


@cds_api.route("/pfuser", methods=['POST', 'GET'])
def pfuser_route():
    respose = Pf_User(request).direct_method()
    return respose
    


cds_api.run()