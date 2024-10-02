import asyncio
import subprocess

async def execute_os_command(command_data):
    command_name = command_data.get("command_name")
    parameters = command_data.get("parameters", [])

    try:
        result = await asyncio.create_subprocess_exec(
            command_name, *parameters,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = await result.communicate()
        return {"result": stdout.decode() if result.returncode == 0 else stderr.decode()}
    except Exception as e:
        return {"error": str(e)}
