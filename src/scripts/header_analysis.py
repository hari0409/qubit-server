from scapy.all import *

# Define a list of suspicious patterns as regular expressions
suspicious_patterns = [
    r'cmd\.exe \/c [a-zA-Z\.]+',
    r'powershell.exe -ExecutionPolicy Bypass -File [a-zA-Z0-9\.]+',
    r'<script[^>]>\s*eval\(.\)\s*<\/script>',
    r'<script[^>]>\s*document\.write\(.\)\s*<\/script>',
    r'[a-zA-Z0-9+/]{50,}',
    r'[a-zA-Z]\s?=\s?function\(\){[^\}]+}',
    r'\$\w+\s?=\s?New-Object [a-zA-Z\.]+;[^\$]+',
    r'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run',
    #r'http[s]?://[a-zA-Z0-9\.\-]+\/[a-zA-Z0-9\/]+',
    r'net\s+user\s+[a-zA-Z0-9_]+ [a-zA-Z0-9_]+ /add',
    r'VirtualProtect\(0x[0-9a-f]+, \d+, \d+, \d+\)',
    r'VirtualQuery\(0x[0-9a-f]+\)',
    r'CreateRemoteThread\(.LoadLibrary\(.\)\)',
    r'powershell\s+\-c\s+.*',
    
    # Suspicious process injection techniques
    r'CreateProcessInternalW\(.*\)',
    r'NtCreateThreadEx\(.*\)',
    r'RtlCreateUserThread\(.*\)',
    
    # Suspicious use of base64 decoding
    r'base64_decode\(.+\)',

    # Suspicious use of obfuscation techniques
    r'[a-zA-Z0-9]{20,}\s?=\s?[a-zA-Z0-9]{20,}',
    
    # Detection of credential manipulation
    r'Secur32\.CallPackage\(".*"\)',
    
    # Detection of lateral movement techniques
    r'Invoke\-WMICommand.*',
    
    # Suspicious use of Windows API functions
    r'GetProcAddress\(.*\)',
    
    # Detection of DLL loading techniques
    r'LoadLibrary\(.*\)',
    r'LoadLibraryEx\(.*\)',
    r'GetProcAddress\(.*\)',
    
    # Suspicious Registry manipulation
    r'RegOpenKeyEx\(.*\)',
    r'RegSetValueEx\(.*\)',
    
    # Suspicious scheduled tasks
    r'schtasks\s+/create\s+.*',
    
    # Suspicious COM object instantiation
    r'new\-object\s+\-comobject\s+.*'
]

def analyze_packet(packet):
    if packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors='ignore')
        
        for pattern in suspicious_patterns:
            matches = re.findall(pattern, payload)
            if matches:
                print("Suspicious pattern found in packet:")
                print("Packet Info:", packet.summary())
                print("Pattern:", pattern)
                print("Matches:", matches)
                print("="*40)


# Sniff network packets and analyze headers
packet = IP(dst="example.com") / TCP(dport=80) / Raw(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n cmd.exe /c calc.exe")
analyze_packet(packet)

"""def read_jpg_header(file_path, num_bytes=10):
    with open(file_path, 'rb') as file:
        header_bytes = file.read(num_bytes)
    
    header_string = ' '.join([f'{byte:02X}' for byte in header_bytes])
    for pattern in suspicious_patterns:
            matches = re.findall(pattern, header_string)
            if matches:
                print("Suspicious pattern found in packet:")
                print("Packet Info:", packet.summary())
                print("Pattern:", pattern)
                print("Matches:", matches)
                print("="*40)
    return header_string

# Example usage
file_path = '/home/kali/Desktop/mountain.jpeg'  # Replace with the actual file path

header = read_jpg_header(file_path)
print(f'JPG Header: {header}')


def modify_jpg_header(file_path, new_header):
    with open(file_path, 'r+b') as file:
        file.seek(0)
        file.write(new_header.encode())

file_path = 'stego.jpg'  # Replace with the actual file path
new_header = "\xFF\xD8\xFF cmd.exe /c calc.exe"  # New header bytes

modify_jpg_header(file_path, new_header)
new=read_jpg_header(file_path)
print(f'Modified JPG Header: {new}')
"""