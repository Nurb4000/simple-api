# routes/shutdown_device.py  
import subprocess  
from flask import Flask, request, jsonify  
from utils.auth import Auth  

auth = Auth()  

def shutdown_device():  
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):  
        return "Unauthorized", 401  
    
    try:
        # Execute the shutdown command
        subprocess.run(["sudo", "shutdown", "-h", "now"], check=True)
        return jsonify({"message": "Shutdown initiated successfully"}), 200  
    except subprocess.CalledProcessError as e:  
        return jsonify({"error": f"Failed to initiate shutdown: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def register_routes(app: Flask):  
    app.add_url_rule("/shutdown_device", view_func=shutdown_device, methods=["GET"])