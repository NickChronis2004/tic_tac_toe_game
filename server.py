import socket
import threading

def handle_client(client_socket, addr, other_client, turn, wins):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            if message == b'RESET':
                turn[0] = 'X'
            other_client.send(message)
        except:
            break
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(2)
    print("Server listening on port 9999")

    client1, addr1 = server.accept()
    print(f"Accepted connection from {addr1}")
    client1.send(b"Welcome Player 1:X")

    client2, addr2 = server.accept()
    print(f"Accepted connection from {addr2}")
    client2.send(b"Welcome Player 2:O")

    turn = ['X']
    wins = {'X': 0, 'O': 0}

    threading.Thread(target=handle_client, args=(client1, addr1, client2, turn, wins)).start()
    threading.Thread(target=handle_client, args=(client2, addr2, client1, turn, wins)).start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Server shutting down")
