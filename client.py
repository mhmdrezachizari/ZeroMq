import zmq
import json
class AsyncClient:
    def __init__(self, host='127.0.0.1', port=4000):
        self.host = host
        self.port = port
        #create context ...
        self.context = zmq.Context()
        # for requests
        self.socket = self.context.socket(zmq.REQ)\
        #connect with server with socket object
        self.socket.connect(f'tcp://{self.host}:{self.port}')
#send operations
    def send_command(self, command):
        #Send json to server
        self.socket.send_string(json.dumps(command))
        #get a response from the server
        response = self.socket.recv_string()
        print("server Response:", response)

#for run with client.py
if __name__ == "__main__":
    client = AsyncClient()

    os_command = {
        "command_type": "fa",
        "command_name": "ping",
        "parameters": ["127.0.0.1", "-n", "4"]
    }

    math_command = {
        "command_type": "compute",
        "expression": "(2 + 2) * 10"
    }

#test os
    client.send_command(command=os_command)

#test math
    client.send_command(command=math_command)

#send a multiple requests
    for i in range(5):
        client.send_command(command={
            "command_type": "compute",
            "expression": f"({i} + {i}) * 10"
        })
