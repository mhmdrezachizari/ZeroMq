import asyncio
import zmq
import zmq.asyncio
import json
from CommandsFile.os_commands import execute_os_command
from CommandsFile.math_commands import evaluate_math_expression
#this code can check the Os(operation system) such as widows , etc
#Thats code check the Windows.
if hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class AsyncServer:
    #create a context , i think the context means a main objects
    def __init__(self, host='127.0.0.1', port=4000):
        self.host = host
        self.port = port
        self.context = zmq.asyncio.Context()
        self.socket = self.context.socket(zmq.REP)
        self.socket.bind(f'tcp://{self.host}:{self.port}')
        print(f"Hello server its running on port {self.port} and is listening on Localhost:{self.port}")
        #handel a request and raedy for recive a json :)
    async def handle_request(self):
        while True:
            message = await self.socket.recv_string()
            asyncio.create_task(self.process_command(message))
#that name its procces and the function can proccessing
    async def process_command(self, command):
        try:
            command_data = json.loads(command)
            command_type = command_data.get("command_type")

            if command_type == "os":
                response = await execute_os_command(command_data)
            elif command_type == "compute":
                response = await evaluate_math_expression(command_data)
            else:
                response = {"error": "Unknown command type"}

            await self.socket.send_string(json.dumps(response))
            #Handel Error :
        except Exception as e:
            await self.socket.send_string(json.dumps({"Error you app means :": str(e)}))

    async def start(self):
        await self.handle_request()
#Start project with py server.py
if __name__ == "__main__":
    server = AsyncServer()
    asyncio.run(server.start())
