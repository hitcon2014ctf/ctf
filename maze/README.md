# Description

Capture the flag in the maze!

```
telnet HOST PORT
```

# Setup

Put `a.raw` and `maze.py` in the same directory on the server.

xinetd config:

```
server      = /bin/busybox
server_args = telnetd -f /dev/null -K -i -l /PATH/TO/maze.py
```

score: 250

flag:

```
HITCON{QR MAZE IS COOL!}
```
