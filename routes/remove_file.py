# routes/remove_file.py

import os
from flask import Flask, request, jsonify
from utils.auth import Auth

auth = Auth()

def remove_file():
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):
        return "Unauthorized", 401
    
    file_path = request.args.get("path")
    
    try:
        os.remove(file_path)
        return jsonify({"message": f"File {file_path} removed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def register_routes(app: Flask):
    app.add_url_rule("/remove_file", view_func=remove_file, methods=["DELETE"])