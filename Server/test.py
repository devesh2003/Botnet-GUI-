botnet = open("bots.txt","r")
bots = botnet.read()
print(bots.split('\n'))
botnet.close()