#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import zmq
import threading

new_code = threading.Event()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GUIPyDebugger.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    if 'runserver' in sys.argv:
        sys.argv.append('--noreload')
        # add noreload every time to prevent zmq socket weirdness

    rep_thread = threading.Thread(target=create_rep_socket, name="REPSocketThread")
    req_thread = threading.Thread(target=create_req_socket, name="REQSocketThread")

    if not rep_thread.is_alive():
        rep_thread.start()
        req_thread.start()

    execute_from_command_line(sys.argv)

def create_req_socket():
    # create a ZMQ context
    context = zmq.Context()

    # Create a REQ (request) socket
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555") # connect to 5554
    socket.setsockopt(zmq.LINGER, 0)

    while True:
        try:
            code = ""
            # wait for user input to be sent
            new_code.wait()

            # copy code in file
            with open(r"./static/code_request.py", "r") as code:
                for line in code.readlines():
                    code += line

            # Temporary teardown logic
            if code.lower() == 'exit':
                context.destroy()
                break

            # Send the code to the server
            socket.send_string(code)

            # Handle response
            response = socket.recv_string()
            print(f"server response: {response}")

            new_code.clear()

        except KeyboardInterrupt:
            break

def create_rep_socket():
    # create a ZMQ context
    context = zmq.Context()

    # create a REP (reply) socket
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:5555') #bind to port 5555
    socket.setsockopt(zmq.LINGER, 0)

    while True:
        # wait for a message
        message = socket.recv_string()

        try:
            # Execute the received message
            result = eval(message) # use exec(message) for multi-line code
            socket.send_string(f"Result: {result}")
        except Exception as e:
            # send back the error message if execution fails
            socket.send_string(f"Error: {str(e)}")

if __name__ == '__main__':
    main()
