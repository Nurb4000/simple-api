# routes/__init__.py

from .list_dir import register_routes as list_dir_register
from .remove_file import register_routes as remove_file_register
from .upload_file import register_routes as upload_file_register
from .download_file import register_routes as download_file_register
from .running_processes import register_routes as running_processes_register
from .execute_command import register_routes as execute_command_register
from .system_uptime import register_routes as system_uptime_register

def register_all_routes(app):
    list_dir_register(app)
    remove_file_register(app)
    upload_file_register(app)
    download_file_register(app)
    running_processes_register(app)
    execute_command_register(app)
    system_uptime_register(app)