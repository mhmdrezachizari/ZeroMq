import zmq
import json


class AsyncClient:
    def __init__(self, host='127.0.0.1', port=4000):
        self.host = host
        self.port = port
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)  # استفاده از REQ برای ارسال درخواست به سرور
        self.socket.connect(f'tcp://{self.host}:{self.port}')

    def send_command(self, command):
        self.socket.send_string(json.dumps(command))  # ارسال درخواست به سرور
        response = self.socket.recv_string()  # دریافت پاسخ از سرور
        print("Server Response:", response)  # چاپ پاسخ سرور


if __name__ == "__main__":
    client = AsyncClient()

    os_command = {
        "command_type": "os",
        "command_name": "ping",
        "parameters": ["127.0.0.1", "-n", "4"]
    }

    math_command = {
        "command_type": "compute",
        "expression": "(2 + 2) * 10"
    }

    # ارسال دستور OS
    client.send_command(command=os_command)

    # ارسال دستور ریاضی
    client.send_command(command=math_command)

    # ارسال چندین درخواست
    for i in range(5):
        client.send_command(command={
            "command_type": "compute",
            "expression": f"({i} + {i}) * 10"
        })
