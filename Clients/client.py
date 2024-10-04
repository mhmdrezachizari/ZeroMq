import zmq
import zmq.asyncio #the version of asyncio
import json
import asyncio #the important libary for manage the multiple task.

if hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
class AsyncClient:
    def __init__(self, host='127.0.0.1', port=4000):
        self.host = host
        self.port = port
        self.context = zmq.asyncio.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(f'tcp://{self.host}:{self.port}')
        self.lock = asyncio.Lock() #the async locker
#send a operations to Server
    async def send_command(self, command):
        async with self.lock:
            await self.socket.send_string(json.dumps(command))
            response = await self.socket.recv_string()
            print("Server Response:", response)
