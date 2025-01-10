# routes/kill_process.py  
import subprocess  
from flask import Flask, request, jsonify  
from utils.auth import Auth  

auth = Auth()  

def kill_process():  
    if not auth.authenticate(request.args.get("username"), request.args.get("password")):  
        return "Unauthorized", 401  
    
    pid = request.args.get("pid")
    
    if not pid:
        return jsonify({"error": "PID is required"}), 400
    
    try:
        # Execute the kill command
        subprocess.run(["sudo", "kill", "-9", pid], check=True)
        return jsonify({"message": f"Process {pid} killed successfully"}), 200  
    except subprocess.CalledProcessError as e:  
        return jsonify({"error": f"Failed to kill process {pid}: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def register_routes(app: Flask):  
    app.add_url_rule("/kill_process", view_func=kill_process, methods=["GET"])