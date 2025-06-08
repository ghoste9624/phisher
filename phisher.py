import socket
import argparse
import sys
import datetime

def listen_and_save(ip, port, filename):
    """
    Listens for incoming traffic on the specified IP and port, and saves the data to a file.
    """
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the specified IP and port
        s.bind((ip, port))

        # Start listening for incoming connections
        s.listen(1)  # Listen for a maximum of 1 connection at a time

        print(f"[*] Listening on {ip}:{port}")

        # Accept a connection from a client
        conn, addr = s.accept()
        print(f"[*] Connection from: {addr[0]}:{addr[1]}")

        # Open the file for writing
        with open(filename, 'a') as f:
            while True:
                # Receive data from the connection
                data = conn.recv(1024)

                # If no data is received, the connection is closed
                if not data:
                    break

                # Write the received data to the file
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] Received from {addr[0]}:{addr[1]}: {data.decode()}\n")
                print(f"Received data: {data.decode()}")

        print("[*] Connection closed")
        conn.close()

    except socket.error as e:
        print(f"[!] Socket error: {e}")
    except Exception as e:
        print(f"[!] An error occurred: {e}")
    finally:
        s.close() # Close the socket

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-i", "--ip", help="IP address to listen on (e.g., 127.0.0.1)", required=True)
    parser.add_argument("-p", "--port", type=int, help="Port to listen on (e.g., 8080)", required=True)
    parser.add_argument("-o", "--output", help="Output file to save data (required)", required=True)

    print("\n\033[97mFor Detailed Usage And Examples Go To\n")
    print("\033[97m>>> \033[96mhttps://github.com/ghoste9624/phisher\n\033[97m")

    args = parser.parse_args()

    listen_and_save(args.ip, args.port, args.output)

if __name__ == "__main__":
    main()
