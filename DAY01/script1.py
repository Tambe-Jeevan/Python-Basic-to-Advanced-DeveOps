server_name = "web-server-1"
os_version = "Ubuntu 22.04"
cpu_core = 4
is_active = True

print("Checking Infrastructur...")
print(server_name)
print(os_version)
print(cpu_core)

# String Formatting (F-Strings) Printing variables one by one is messy. Let's use f-strings for simple, human-readable text. Modify your code:

print(f"The server:{server_name} running on os version:{os_version} with CPU Core:{cpu_core}")