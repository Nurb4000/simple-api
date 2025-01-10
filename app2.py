# api.py

from flask import Flask
from routes import (
    list_dir,
    remove_file,
    upload_file,
    download_file,
    running_processes,
    execute_command,
    system_uptime,
)

app = Flask(__name__)

list_dir.register_routes(app)
remove_file.register_routes(app)
upload_file.register_routes(app)
download_file.register_routes(app)
running_processes.register_routes(app)
execute_command.register_routes(app)
system_uptime.register_routes(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)