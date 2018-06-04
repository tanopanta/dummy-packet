import socket

def receive(port, size=1000, times=10, index=True):
    """
    receive function

    port: bind port address,
    size: packet data length(Byte) (or buffer size),
    times: number of receiving,
    index: True => check index 
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", port))
    
    index_buf = []
    
    for _ in range(times):
        buf = sock.recv(1024)
        
        if index:
            now_index = buf[0] + 256 * buf[1]
            print(now_index, end=",", flush=True)
            index_buf.append(now_index)
        else:
            print(".")
    if index:
        print("\n\nreceive {0} / {1} loss {2} %".format(len(index_buf), times, 1 - (len(index_buf)/times)))
    else:
        print("end")

def main():
    print("udp packet waiting...")
    receive(12345, times=555)

if __name__ == '__main__':
    main()