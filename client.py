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
#send a few instructions
async def FuctionForSendAsynchronousCommand():
    client = AsyncClient()

    os_commands = [
        {
            "command_type": "os",
            "command_name": "ping",
            "parameters": ["127.0.0.1", "-n", "4"]
        },
        {
            "command_type": "os",
            "command_name": "dir",  # برای ویندوز
            "parameters": []
        }
    ]

    for command in os_commands:
        await client.send_command(command)

    math_commands = [
        {
            "command_type": "compute",
            "expression": "(2 + 2) * 10"
        },
        {
            "command_type": "compute",
            "expression": "5 * (3 + 2)"
        }
    ]
    #for math
    for command in math_commands:
        await client.send_command(command)
    tasks = []
    for i in range(100):
        task = client.send_command(command={
            "command_type": "compute",
            "expression": f"({i} + {i+1})*10"
        })
        tasks.append(task)

    await asyncio.gather(*tasks)
#Run with client.py
if __name__ == "__main__":
    asyncio.run(FuctionForSendAsynchronousCommand())
