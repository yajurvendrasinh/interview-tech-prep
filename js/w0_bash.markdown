### A few bashisms to remember

#### How to kill an open port

- What ports are open right now?

```
$ lsof -i -P | grep -i "listen"
ruby      51893 psoshnin    7u  IPv4 0x9ce737c076eff159      0t0  TCP *:4567 (LISTEN)
```

```
$ sudo lsof -i :4567
COMMAND   PID     USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
ruby    50898 psoshnin    7u  IPv4 0x9ce737c076ee6e19      0t0  TCP *:tram (LISTEN)
```

```
$ sudo kill -9 50898
```