from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket
import os


# Current folder ko server root banaye
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Computer ka IP address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


# Remote access ke liye 0.0.0.0
server = HTTPServer(
    ("0.0.0.0", 8000),
    SimpleHTTPRequestHandler
)


print("--------------------------------")
print("Python File Server Started")
print("--------------------------------")

print("Local:")
print("http://localhost:8000")

print("\nRemote PC:")
print(f"http://{local_ip}:8000")

print("\nAvailable:")
print("- chapter_20")
print("- chapter_21")
print("- gamma")
print("- LEARNINGS")
print("- Python files")
print("- Images")

print("--------------------------------")


server.serve_forever()