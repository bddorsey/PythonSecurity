#!/usr/bin/python3

########################################
# Author: Brian Dorsey                 #
# Version: 1.0                         #
# Email: bdorsey327@gmail.com          #
# Maintainer = Brian Dorsey            #
# Date: 3/1/2023                       #
######################################## 



import socket





def main():

     target = input("\nProvide the IP ADDRESS of the target to scan or enter exit to close: ")

     while target:
         if target == "exit":
             print("\nYou have chosen to exit")
             break
         else:
             message = input("\nPlease provide a range of ports to be scanned (Press Enter to continue)")
             start = int(input("First port: \n"))
             last = int(input("Last port: \n"))
             print(f"\nScan for {target} will begin")

     targetIP = target
     print(f"\nScanning {targetIP}")

     OpenPorts = []

     print("####################################################################")

     starttime = time.time()  #start timing how long it takes to run scan

     try:
         for i in range(start, last): # ports to scan / range can be changed
             scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
             conn = scanner.connet_ex((targetIP, i))
             if conn == 0:
                 OpenPorts.append(i)
                 print(f"Port --> {i} is open")
                 scanner.close()
     except ConnectionRefusedError:
         print("Connection request not accepted")
         exit(1)

     endtime = time.time()
     totalTime = endtime - starttime
     print(f"\n Scan for {target} finished")
     print(f"\nThe total time to run this scan was {totalTime} seconds\n")
     print(f"Here's the list of the ports found open during the scan {OpenPorts}\n")
     print(f"{targetIP} had {len(OpenPorts)} ports open")
     print("###################################################################")

     Question = input("Would you like to save the results to a file y/n: ")
     if Question ==  'y':
         filename = input("Enter file name: ")
         with open(filename, 'w') as f:
             for item in (OpenPorts):
                 f.write(f"Port: {str(item)}" + "\n")
         print(f"{filename} created")
     elif Question == 'n':
         print("No file created")

     target = input("\nProvide the IP ADDRESS of the target to scan or enter exit to close: ")



if __name__ == "__main__":
    main()