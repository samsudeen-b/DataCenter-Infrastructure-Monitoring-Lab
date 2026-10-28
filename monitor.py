import psutil
import socket
from datetime import datetime

print("=" * 50)
print("DATA CENTER INFRASTRUCTURE HEALTH MONITOR")
print("=" * 50)

# System information
hostname = socket.gethostname()
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Collect infrastructure metrics
cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")
network = psutil.net_io_counters()

print("\nSYSTEM INFORMATION")
print("Hostname:", hostname)
print("Checked at:", current_time)

print("\nRESOURCE MONITORING")
print("CPU Usage:", cpu_usage, "%")
print("Memory Usage:", memory.percent, "%")
print("Disk Usage:", disk.percent, "%")

print("\nNETWORK STATISTICS")
print("Bytes Sent:", network.bytes_sent)
print("Bytes Received:", network.bytes_recv)

# Incident detection
print("\nHEALTH CHECK")

incidents = []

if cpu_usage >= 90:
    incidents.append("CRITICAL: CPU utilization exceeded 90%")
    print("CPU Status: CRITICAL")
else:
    print("CPU Status: HEALTHY")

if memory.percent >= 90:
    incidents.append("CRITICAL: Memory utilization exceeded 90%")
    print("Memory Status: CRITICAL")
else:
    print("Memory Status: HEALTHY")

if disk.percent >= 90:
    incidents.append("CRITICAL: Disk utilization exceeded 90%")
    print("Disk Status: CRITICAL")
else:
    print("Disk Status: HEALTHY")

# Save monitoring history
with open("monitoring.log", "a") as log:
    log.write(
        f"{current_time} | "
        f"Host={hostname} | "
        f"CPU={cpu_usage}% | "
        f"Memory={memory.percent}% | "
        f"Disk={disk.percent}%\n"
    )

# Save detected incidents
if incidents:
    with open("incidents.log", "a") as incident_file:
        for incident in incidents:
            incident_file.write(
                f"{current_time} | {hostname} | {incident}\n"
            )

    print("\nINCIDENTS DETECTED:")
    for incident in incidents:
        print("-", incident)
else:
    print("\nNo critical incidents detected.")

print("\nMonitoring data saved successfully.")
print("=" * 50)