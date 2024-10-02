import asyncio
import zmq
import zmq.asyncio
import json
from commands.os_commands import execute_os_command
from commands.math_commands import evaluate_math_expression

# تنظیم policy برای Windows
if hasattr(asyncio, 'WindowsSelectorEventLoopPolicy'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class AsyncServer:
    def __init__(self, host='127.0.0.1', port=4000):
        self.host = host
        self.port = port
        self.context = zmq.asyncio.Context()
        self.socket = self.context.socket(zmq.REP)  # سوکت REP برای دریافت درخواست
        self.socket.bind(f'tcp://{self.host}:{self.port}')
        print("Server is running with asyncio...")

    async def handle_request(self):
        while True:
            message = await self.socket.recv_string()  # دریافت پیام به صورت async
            asyncio.create_task(self.process_command(message))  # پردازش درخواست به صورت همزمان

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

            await self.socket.send_string(json.dumps(response))  # ارسال پاسخ به کلاینت
        except Exception as e:
            await self.socket.send_string(json.dumps({"error": str(e)}))

    async def start(self):
        await self.handle_request()  # شروع پردازش درخواست‌ها

if __name__ == "__main__":
    server = AsyncServer()
    asyncio.run(server.start())  # اجرای سرور به صورت async
