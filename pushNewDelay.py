num = int(input("Delay value: "))
os.system("mosquitto_pub -h localhost -t test_channel -m 'delay:'"+str(num))