import sys
import random

def subnet_calc():
    try:
        print("\n")
        while True:
            ip = raw_input("Enter an ip address: ")
            ip_octets= ip.split('.')
            #print(ip_octets)
            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break

            else:
                print("\n Invalid ip address. Retry \n")
                continue

        masks=[255,254,252,248,240,224,192,128,0]

        while True:
            subnet=raw_input("\nEnter the subnet mask: ")
            mask_octets=subnet.split(".")
            if((len(mask_octets)==4)and(int(mask_octets[0])==255)and(int(mask_octets[1]) in masks)and(int(mask_octets[2]) in masks)
            and(int(mask_octets[3]) in masks)and(int(mask_octets[0])>=int(mask_octets[1])>=int(mask_octets[2])>=int(mask_octets[3]))):
                break

            else:
                print("\n invalid subnet mask")
                continue

        mask_binary=[]

        for octet in mask_octets:
            bin_octet=bin(int(octet)).lstrip("0b")
            mask_binary.append(bin_octet.zfill(8))

        binarymask="".join(mask_binary)
            #we get binary mask as 11111111111111111111110000000
        #print(binarymask)
        #print(mask_octets)

        num_zeros=binarymask.count("0")
        num_ones=32-num_zeros
        num_hosts= abs(2** num_zeros-2)

        #wildcard mask calculation

        wildcard_octets=[]

        for octets in mask_octets:
            wildcard_octets.append(str(255-int(octets)))

        wildcardmask=".".join(wildcard_octets)
        #print(wildcardmask)
        ip_binary=[]

        for octet in ip_octets:
            binary_octet=bin(int(octet)).lstrip("0b")
            ip_binary.append(binary_octet.zfill(8))

        binaryip="".join(ip_binary)
        #print(binaryip)
        network_addr_bin= binaryip[:num_ones]+"0"*num_zeros
        broadcast_addr_bin= binaryip[:num_ones]+"1"*num_zeros
        #print(network_addr_bin)
        #print(broadcast_addr_bin)

        #converting back to decimal -network address
        network_octet=[]

        for bit in range(0,32,8):
            net_octet=network_addr_bin[bit:bit+8]
            network_octet.append(net_octet)
        # we get octets in binary in the network_octet list
        #print(network_octet)
        #converting to number
        net_ip_add=[]

        for octet in network_octet:
            network_ip_int = int(octet,2)
            net_ip_add.append(str(network_ip_int))

        network_ip_address=".".join(net_ip_add)
        #print(network_ip_address)
        #converting back to decimal -broadcast address
        broadcast_octet=[]

        for bit in range(0,32,8):
            bst_octet=broadcast_addr_bin[bit:bit+8]
            broadcast_octet.append(bst_octet)
        # we get octets in binary in the network_octet list

        #converting to number
        broadcast_ip_add=[]

        for octet in broadcast_octet:
            broadcast_ip_int = int(octet,2)
            broadcast_ip_add.append(str(broadcast_ip_int))

        broadcast_ip_address="".join(broadcast_ip_add)
        print(broadcast_ip_address)
        print("\n")
        print("Network Address is: %s\n" %network_ip_int)
        print("Broadcast Address is: %s\n" %broadcast_ip_int)
        print("Number of valid hosts per network: %s\n"%num_hosts)
        print("Wildcard mask is: %s\n"%wildcardmask)
        print("Mask bits: %s\n"%num_ones)
        print("\n")


        #generation of random ip Address
        while True:
            generate=raw_input("Do you want to generate random ip address: (y/n)")

            if generate == "y":
                generated_ip=[]
                for indexb,oct_bst in enumerate (broadcast_ip_add):
                    for indexn,oct_net in enumerate(net_ip_add):
                        if indexb==indexn:
                            if(oct_bst==oct_net):
                                generated_ip.append(oct_bst)
                            else:
                                generated_ip.append(str(random.randint(int(oct_net),int(oct_bst))))

                y_iadd=".".join(generated_ip)

                print("Random ip address is: %s" %y_iadd)
                print("\n")
                continue

            else:
                print("ok. Bye!")
                break

    except KeyboardInterrupt:
        print("\n Program aborted by user. Exiting...")
        sys.exit()

subnet_calc()
