def checkclass(ipaddress,mask,supermask):
    ipaddress=list(map(int,ipaddress.split('.')))
    ipstr=""
    if(ipaddress[0]>=0 and ipaddress[0]<=127):
        print("Class A")
    if(ipaddress[0]>=128 and ipaddress[0]<=191):
        print("Class B")
    if(ipaddress[0]>=192 and ipaddress[0]<=223):
        print("Class C")
    if(ipaddress[0]>=224 and ipaddress[0]<=239):
        print("Class D")
    if(ipaddress[0]>=240 and ipaddress[0]<=255):
        print("Class E")
    for i in ipaddress:
        ipstr=ipstr+"0"*(8-len(bin(i)[2:]))+bin(i)[2:]
    netip=ipstr[:mask]+"0"*(32-mask)
    firstip=ipstr[:mask]+"0"*(32-mask-1)+"1"
    lastip=ipstr[:mask]+"1"*(32-mask-1)+"0"
    bcastip=ipstr[:mask]+"1"*(32-mask)
    #maskstr="1"*(mask)+"0"*(32-mask)
    print("For mask ",mask)
    print("Network      IP : ",int(netip[:8],2),int(netip[8:16],2),int(netip[16:24],2),int(netip[24:],2))
    print("First        IP : ",int(firstip[:8],2),int(firstip[8:16],2),int(firstip[16:24],2),int(firstip[24:],2))
    print("Last         IP : ",int(lastip[:8],2),int(lastip[8:16],2),int(lastip[16:24],2),int(lastip[24:],2))
    print("Broadcast    IP : ",int(bcastip[:8],2),int(bcastip[8:16],2),int(bcastip[16:24],2),int(bcastip[24:],2))
    netip=ipstr[:supermask]+"0"*(32-supermask)
    """
    FOR SUPERMASK=28 
        NO OF SUBNET BITS=4
        SO WE HAVE 16 SUBNETWORKS
    """
    print("\nFor mask ",supermask)
    for netid in range(0,pow(2,supermask-mask)):
        netip=ipstr[:mask]+"0"*(supermask-mask-1)+bin(netid)[2:]+"0"*(32-supermask)
        firstip=ipstr[:mask]+"0"*(supermask-mask-len(bin(netid)[2:]))+bin(netid)[2:]+"0"*(32-supermask-1)+"1"
        lastip=ipstr[:mask]+"0"*(supermask-mask-len(bin(netid)[2:]))+bin(netid)[2:]+"1"*(32-supermask-1)+"0"
        bcastip=ipstr[:mask]+"0"*(supermask-mask-len(bin(netid)[2:]))+bin(netid)[2:]+"1"*(32-supermask)
        print("\nNetwork      IP : ",int(netip[:8],2),int(netip[8:16],2),int(netip[16:24],2),int(netip[24:],2))
        print("First        IP : ",int(firstip[:8],2),int(firstip[8:16],2),int(firstip[16:24],2),int(firstip[24:],2))
        print("Last         IP : ",int(lastip[:8],2),int(lastip[8:16],2),int(lastip[16:24],2),int(lastip[24:],2))
        print("Broadcast    IP : ",int(bcastip[:8],2),int(bcastip[8:16],2),int(bcastip[16:24],2),int(bcastip[24:],2))
    