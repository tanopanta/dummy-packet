"""
send dummy packet(UDP)
"""
import socket
import time

def send(ip, port, size=1000, interval=1, times=10, index=False):
    """
    send function

    ip: to ip address,
    port: to port address,
    size: packet data length(Byte),
    interval: send interval(s),
    times: number of sending,
    index: True => add index to data, False=>zero fill 
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    data = bytearray([0 for _ in range(size)])
    
    for i in range(times):
        if index:
            data[0] = i % 256
        sock.sendto(data, (ip, port))
        print("send to {0} ({1}Byte)".format(ip, size))
        time.sleep(interval)

def main():
    """main"""
    #send("127.0.0.1", 12321)
    send("127.0.0.1", 12345, index=True, interval=0.01, times=257)

if __name__ == '__main__':
    main()
