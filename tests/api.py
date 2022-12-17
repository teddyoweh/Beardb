import ssl
import socket
def check_https(host, port):
    context = ssl.create_default_context()
    try:
        with context.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.connect((host, port))
            return True
    except ssl.SSLError:
        return False

# Test the function
print(check_https('teddyoweh.net', 443))  # True
print(check_https('www.teddyoweh.net', 8080))  # False
