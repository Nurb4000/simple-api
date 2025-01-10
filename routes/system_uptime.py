# routes/system_uptime.py

import subprocess
from flask import Flask, request, jsonify
from utils.auth import Auth

auth = Auth()

def get_system_uptime():
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):
        return "Unauthorized", 401
    
    uptime = subprocess.run(["uptime"], stdout=subprocess.PIPE).stdout.decode()
    return jsonify({"uptime": uptime})

def register_routes(app: Flask):
    app.add_url_rule("/system_uptime", view_func=get_system_uptime, methods=["GET"])