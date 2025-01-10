# routes/list_dir.py

import os
from flask import Flask, request, jsonify
from utils.auth import Auth

auth = Auth()

def list_directory():
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):
        return "Unauthorized", 401
    
    folder_path = request.args.get("path")
    
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        return jsonify({"error": "Invalid directory path"}), 400

    files = os.listdir(folder_path)
    return jsonify(files)

def register_routes(app: Flask):
    app.add_url_rule("/list_dir", view_func=list_directory, methods=["GET"])