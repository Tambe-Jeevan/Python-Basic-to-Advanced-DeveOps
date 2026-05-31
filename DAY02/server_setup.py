server_name = input("Enter the server name: ")

print(f"The server is {server_name}")


ram_gb_string = input("How many GB of RAM does the server have? ")
ram_gb = int(ram_gb_string)

if ram_gb >= 16:
    print("Requirement met: Server is approved for database installation.")
else:
    print("Error: Minimum 16 GB RAM required. Installation aborted.")
