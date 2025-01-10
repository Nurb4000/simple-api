# routes/download_file.py

import os
from flask import Flask, request, send_from_directory, jsonify
from utils.auth import Auth

auth = Auth()

def download_file():
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):
        return "Unauthorized", 401
    
    file_path = request.args.get("path")
    
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return jsonify({"error": "Invalid file path"}), 400

    folder_path, filename = os.path.split(file_path)
    return send_from_directory(folder_path, filename)

def register_routes(app: Flask):
    app.add_url_rule("/download_file", view_func=download_file, methods=["GET"])