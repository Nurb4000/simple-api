# routes/upload_file.py

import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from utils.auth import Auth

auth = Auth()

def upload_file():
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):
        return "Unauthorized", 401
    
    folder_path = request.form.get("path")
    
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        return jsonify({"error": "Invalid directory path"}), 400

    file = request.files.get("file")
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(folder_path, filename)
        file.save(filepath)
        return jsonify({"message": f"File {filename} uploaded successfully to {folder_path}"}), 200
    else:
        return jsonify({"error": "No file part in the request"}), 400

def register_routes(app: Flask):
    app.add_url_rule("/upload_file", view_func=upload_file, methods=["POST"])