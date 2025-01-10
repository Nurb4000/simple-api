# routes/running_processes.py

import subprocess
from flask import Flask, request, jsonify
from utils.auth import Auth

auth = Auth()

def get_running_processes():
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):
        return "Unauthorized", 401
    
    processes = subprocess.run(["ps", "-ef"], stdout=subprocess.PIPE).stdout.decode()
    return jsonify(processes.split("\n"))

def register_routes(app: Flask):
    app.add_url_rule("/running_processes", view_func=get_running_processes, methods=["GET"])