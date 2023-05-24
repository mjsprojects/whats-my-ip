from flask import Flask, render_template, request, flash
import socket
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_ip_info():
    try:
        ip_address = request.remote_addr
        geo_info = requests.get(f'http://ip-api.com/json/{ip_address}').json()
        reverse_dns = socket.gethostbyaddr(ip_address)[0]
        user_agent = request.user_agent.string
        return render_template('index.html', ip=ip_address, geo_info=geo_info, reverse_dns=reverse_dns, user_agent=user_agent)
    except Exception as e:
        flash(f"An error occurred: {str(e)}")
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
