#This script uses python3
#REfer to requirements.txt for script requirements. 
#some features of this script may require administrative privilages.



# importing module
import platform
print("-----------------------------------------------------------------------")

print()

print("Platform Info:")

print()

# dictionary
info = {}
# platform details
platform_details = platform.platform()

# adding it to dictionary
info["platform details"] = platform_details

# system name
system_name = platform.system()

# adding it to dictionary
info["system name"] = system_name

# processor name
processor_name = platform.processor()

# adding it to dictionary
info["processor name"] = processor_name

# architectural detail
architecture_details = platform.architecture()

# adding it to dictionary
info["architectural detail"] = architecture_details

# printing the details
for i, j in info.items():
    print(i, " - ", j)


import psutil

print("-----------------------------------------------------------------------")

print()

print("System Process Info:")

print()

# Iterate over all running process
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        print(processName , ' ::: ', processID)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
print("-----------------------------------------------------------------------")

print()

print("System User Info:")



import psutil
print()
#print users
print(psutil.users())

print("-----------------------------------------------------------------------")


# print("System Network Info")
# More funtionluty will be added in future commits. Thank you.
