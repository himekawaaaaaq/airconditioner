import socket

from wifi import connect_wifi
from aircon import power_on,power_off

wlan = connect_wifi()

PORT = 8080

def create_response(body, status="200 OK"):
    return("HTTP/1.1 " + status + "\r\n"
        "Content-Type: application/json\r\n"
        "Connection: close\r\n"
        "\r\n"
        + body
        )

addr = socket.getaddrinfo("0.0.0.0",PORT)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

print("Server running")
print("Port:",PORT)

while True:
    client, address = server.accept()
    
    try:
        request = client.recv(1024).decode()
        
        print(request)
        
        first_line = request.split("\r\n")[0]
        method,path, _ =first_line.split(" ")
        
        if method == "POST" and path == "/aircon/on":
           
           power_on()
            
           response = create_response(
                '{"success":true,"power":"on"}'
                )
        
        elif method == "POST" and path == "/aircon/off":
        
           power_off()
        
           response = create_response(
               '{"success":true,"power":"off"}'
               )
        
        elif method == "GET" and path == "/health":
            
           response = create_response('{"status":"ok"}')
            
        else:
            
           response = create_response(
               '{"error":"not found"}',
               "404 Not Found"
               )
            
        client.send(response)
        
    except Exception as e:

        print("Error:", e)

    finally:

        client.close()
        
        
        
        
