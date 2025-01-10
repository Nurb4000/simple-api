# routes/reboot_device.py
import subprocess
from flask import Flask, request, jsonify
from utils.auth import Auth

auth = Auth()

def reboot_device():
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):
        return "Unauthorized", 401
    
    try:
        # Execute the reboot command
        subprocess.run(["sudo", "reboot"], check=True)
        return jsonify({"message": "Reboot initiated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def register_routes(app: Flask):
    app.add_url_rule("/reboot_device", view_func=reboot_device, methods=["GET"])