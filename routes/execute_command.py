# routes/execute_command.py

import subprocess
from flask import Flask, request, jsonify
from utils.auth import Auth

auth = Auth()

def execute_command():
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):
        return "Unauthorized", 401
    
    command = request.args.get("command")
    
    try:
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE).stdout.decode()
        return jsonify({"output": output}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def register_routes(app: Flask):
    app.add_url_rule("/execute_command", view_func=execute_command, methods=["GET"])