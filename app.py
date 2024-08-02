from flask import Flask, jsonify, request
import socket
import platform
import requests

app = Flask(__name__)

def get_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
    except Exception as e:
        ip = f"Error: {e}"
    return ip

def get_system_info():
    return {
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'platform': platform.system(),
        'platform_version': platform.version(),
        'architecture': platform.machine(),
        'processor': platform.processor()
    }

@app.route('/info', methods=['GET'])
def get_info():
    ip = get_ip()
    system_info = get_system_info()
    return jsonify({
        'ip': ip,
        'system_info': system_info
    })

if __name__ == '__main__':
    app.run(debug=True)
