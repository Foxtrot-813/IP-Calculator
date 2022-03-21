# import ipaddress
while True:
    try:
        ip = input("Please enter the IP address or Q for Quit: ")
        if ip.upper() == 'Q':
            break
        sub = input("Please choose one of the options: \n1- Prefix \n2- Subnet\n3- Quit \n")
        prefix = 0
        if sub == '3':
            break
        elif sub == '1':
            prefix = int(input("Pleas input the prefix number: \n"))
        elif sub == '2':
            sub = input("Pleas input the Subnet: \n").split('.')
            for i in sub:
                if i == '255':
                    prefix += 8
                else:
                    x = f"{int(i):08b}"
                    for i in x:
                        if i == '1':
                            prefix += 1
            print(f"Prefix: /{prefix}")

        ip = ip.split('.')
        binary_ip = []
        binary_subnet = []
        network_binary = []
        network_ip = []
        broadcast_binary = []
        broadcast_ip = []


        def ip_address(ip):
            for i in ip:
                b = f'{int(i):08b}'
                n = 8 - len(b)
                binary_ip.append(f"{b}{'0' * n}")
            print(f"Binary IP:        {'.'.join(binary_ip)}")


        def subnet(num):
            n = 32 - num
            s = f"{'1' * num}{'0' * n}"
            x = 0
            for i in range(8, 40, 8):
                binary_subnet.append(s[x:i])
                x += 8
            # print(*binary_subnet, sep='.')
            print(f"Binary Subnet:    {'.'.join(binary_subnet)}")


        def network_address(a, b):
            for i in range(4):
                k = a[i]
                m = b[i]
                address = ''
                for x, y in zip(k, m):
                    if x == '1' and y == '1':
                        address += '1'
                    else:
                        address += '0'
                network_binary.append(address)
                network_ip.append(f"{int(address, 2)}")
            print(f"Binary Network:   {'.'.join(network_binary)}")


        def broadcast_address():
            n = 32 - prefix
            network = "".join(network_binary)
            s = network[:-n] + ('1' * n)
            x = 0
            for i in range(8, 40, 8):
                z = s[x:i]
                broadcast_binary.append(z)
                broadcast_ip.append(f"{int(s[x:i], 2)}")
                x += 8
            print(f"Binary Broadcast: {'.'.join(broadcast_binary)}")


        def network_range():
            n = 0
            k = 0
            if binary_ip[0].startswith('0'):
                for i in binary_subnet[1:]:
                    for j in i:
                        if j == '1':
                            n += 1
                        elif j == '0':
                            k += 1
                print("Class: A")
            elif binary_ip[0][:2] == '10':
                for i in binary_subnet[2:]:
                    for j in i:
                        if j == '1':
                            n += 1
                        elif j == '0':
                            k += 1
                print("Class: B")
            elif binary_ip[0][:3] == '110':
                for i in binary_subnet[-1]:
                    for j in i:
                        if j == '1':
                            n += 1
                        elif j == '0':
                            k += 1
                print("Class: C")
            max_subnets = 2 ** n
            print(f"Maximum Subnets:  {max_subnets}")
            print(f"Hosts per Subnet: {(2 ** k) - 2}")


        def general_info():
            first_ip = network_ip[:]
            last_ip = broadcast_ip[:]
            # first_ip = copy.deepcopy(network_ip)
            # last_ip = copy.deepcopy(broadcast_ip)
            first_ip[-1] = str(int(first_ip[-1]) + 1)
            last_ip[-1] = str(int(last_ip[-1]) - 1)
            print(f"Network Address:  {'.'.join(network_ip)}")
            print(f"First IP Address: {'.'.join(first_ip)}")
            print(f"Last IP Address:  {'.'.join(last_ip)}")
            print(f"Broadcast IP:     {'.'.join(broadcast_ip)}")


        ip_address(ip)
        subnet(prefix)
        network_address(binary_ip, binary_subnet)
        broadcast_address()
        general_info()
        network_range()
    except ValueError:
        print(ValueError)
