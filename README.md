Hello

Welcome to my repository!

First, I would like to describe my project:

My project consists of libraries such as ZMQ, JSON, SymPy, asyncio, and others.

  ZMQ (ZeroMQ) is a messaging library that acts as a message broker. It creates a context for the client and server sides, allowing them to communicate with each other.
  JSON library is used to handle and process JSON data types.
  SymPy library is used to compute mathematical commands.
  asyncio library provides tools for asynchronous programming, such as managing multiple processes with async/await functions.

Now, I want to describe the details of my project:
My project consists of three main parts: client, server, and operation files.
Server:

The server handles the ZMQ communication and listens for OS or math commands sent from the client.

The server starts on localhost (127.0.0.1) on port 4000. If port 4000 is busy, you can change it by editing Config with config.py

I have tried to implement the project using OOP. Here's a brief summary of my code:

  First part: I define a class named AsyncServer. In the __init__ method, I specify the port and host, create a context and a socket, and set the socket type to REP (Reply), because the server receives JSON from the client, processes it, and sends a response back.

  Second part: I define a method called handle_request. This method constantly listens for incoming requests because it contains a while True loop.

  Third part: I define a method called process_command, which receives a JSON command from the client, processes it based on the command type, and handles any errors if the processing fails.

  Fourth part: I create an instance (object) of AsyncServer and start the server.

Client:

The client sends and receives JSON data to/from the server. The client uses a REQ (Request) socket.

  First part: I define a class named AsyncClient. It's similar to the server, but the main difference is that the socket type is REQ.

  Second part: I define a method called send_command. This method sends a JSON command to the server and returns the response from the server.

  Third part: I define a function called FuctionForSendAsynchronousCommand, which tests the server and sends commands.

  Fourth part: I use asyncio.gather to handle multiple commands simultaneously.

Operation Files:

The operation files are divided into two parts: math and OS.

  The math file processes mathematical commands using the SymPy library.
  The OS file processes operating system commands (specifically for Windows) using the subprocess module.

Additional Notes:

This project uses asynchronous programming to handle multiple requests simultaneously and efficiently manage resources. If you encounter any issues with port availability or other settings, you can easily adjust them in the server and client configuration files


To get started with the project:

  First, run the server.py file using the following command:

    python ZeroMq.Servers.server.py

This will start the server and make it ready to receive requests from the client.

Then, run the clientTest using the following command:

    python ZeroMq.Client_Task_Test.client_task_test.py

This will connect the client to the server and send commands to it.

you can write youre test commands in this file


  
Programming Language and Required Libraries:

To run your project, you need to install the programming language Python and several libraries. Below is the list of the required language and libraries:
Programming Language:

  Python 3.6 or higher: Make sure you have one of the versions 3.6 or above installed.

Libraries:

  pyzmq: A library for using ZeroMQ in Python.
        Installation:

    pip install pyzmq

sympy: A library for mathematical computations.

  Installation:

    pip install sympy

asyncio: This library is included by default in Python 3.3 and higher, so no separate installation is needed. It is used for asynchronous programming.

json: This library is also included by default in Python and is used for working with JSON data.
