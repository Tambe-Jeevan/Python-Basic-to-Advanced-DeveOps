cpu_load = int(input("Enter current CPU load percentage (0-100): "))

if cpu_load >= 100:
    print("Please enter valid CPU Load %. (0-100)")
elif cpu_load >= 90:
    print(f"CRITICAL: CPU is at {cpu_load}%. Initiating autoscaling.")
elif cpu_load >= 70:
    print(f"WARNING: CPU is at {cpu_load}%. Pinging on call Desktop-Support Engineer.")
elif cpu_load >=0:
    print(f"OK: CPU is at {cpu_load}%. Operations normal.")
else:
    print("Invalid input. Load can not be negative.")