from ZeroMq.Clients.client import AsyncClient
import asyncio
#Test
async def FuctionForSendAsynchronousCommand():
    #create a object from abstract class
    client = AsyncClient()
#os test
    os_commands = [
        {
            "command_type": "os",
            "command_name": "ping",
            "parameters": ["127.0.0.1", "-n", "4"]
        },
        {
            "command_type": "os",
            "command_name": "dir",
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
#Run with client_task_test.py
if __name__ == "__main__":
    asyncio.run(FuctionForSendAsynchronousCommand())
