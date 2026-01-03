import re

file_path1 = r"C:\Users\polak\OneDrive\Desktop\faker\faker_project\src\server_log.txt"
file_path2 = r"C:\Users\polak\OneDrive\Desktop\faker\faker_project\src\log_summary.txt"
ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
error_two = r'\b(2\d{2})\b'
error_three = r'\b(3\d{2})\b'
error_four = r'\b(4\d{2})\b'
error_five = r'\b(5\d{2})\b'


def analyze_logs(file_path):
    '''
    Calculate the Total number of IP address,
    Unique IP address,Repeated Ip address and
    Status Count
    '''
    unique_ips = set()
    repeated_ip = set()
    ip_counts = 0
    status_count = {
        "2xx": 0,
        "3xx": 0,
        "4xx": 0,
        "5xx": 0
    }
    with open(file_path, "r") as file:
        logs = file.readlines()
    for line in logs:
        ip_match = re.match(ip_pattern, line)
        if ip_match:
            ip_counts += 1
            ip = ip_match.group()
            if ip not in unique_ips:
                unique_ips.add(ip)
            else:
                repeated_ip.add(ip)
        # using dictionary key to get previous count and incrementing by 1
        if re.search(error_two, line):
            status_count["2xx"] += 1
        elif re.search(error_three, line):
            status_count["3xx"] += 1
        elif re.search(error_four, line):
            status_count["4xx"] += 1
        elif re.search(error_five, line):
            status_count["5xx"] += 1

    return ip_counts, unique_ips, repeated_ip, status_count


def write_report(file_path, ip_counts, unique_ips, repeated_ip, status_count):
    with open(file_path, 'w') as file:
        file.write("Log file summary report\n")
        file.write("------------------------\n")
        file.write(f"Total logs Count : {ip_counts}\n")
        file.write(f"Unique Ip address : {len(unique_ips)}\n")
        file.write(f"Duplicate Ip address : {len(repeated_ip)}\n\n")
        file.write("Status Code Summary:\n")
        file.write(f"2xx  Count : {status_count['2xx']}\n")
        file.write(f"3xx  Count : {status_count['3xx']}\n")
        file.write(f"4xx  Count : {status_count['4xx']}\n")
        file.write(f"5xx  Count : {status_count['5xx']}\n")
# call the analyze_logs function
ip_counts, unique_ips, repeated_ip, status_count = analyze_logs(file_path1)
write_report(file_path2, ip_counts, unique_ips, repeated_ip, status_count)

print("success")
