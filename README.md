# dummy packet
send dummy packet(UDP)
## function
send(ip, port, size=1000, interval=1, times=10, index=False)
- ip: to ip address,
- port: to port address,
- size: packet data length(Byte),
- interval: send interval(s),
- times: number of sending,
- index: True => add index to data, False=>zero fill
