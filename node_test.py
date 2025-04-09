import requests
import socket
import ssl

def check_dns(url):
    try:
        hostname = url.split('//')[1].split(':')[0]
        socket.gethostbyname(hostname)
        return True
    except socket.gaierror:
        return False

def test_node(node_url):
    print(f"\nTesting node: {node_url}")
    
    if not check_dns(node_url):
        print(f"DNS resolution failed for {node_url}")
        return False

    print(f"DNS resolution successful for {node_url}")

    headers = {
        'User-Agent': 'IOTA Node Tester/1.0'
    }

    try:
        response = requests.get(f"{node_url}/api/core/v2/info", timeout=10, headers=headers, verify=True)
        if response.status_code == 200:
            print("Successfully retrieved node information:")
            print(response.json())
            return True
        else:
            print(f"Connected to {node_url} but received status code: {response.status_code}")
            print("Response content:", response.text)
            return False
    except requests.exceptions.RequestException as e:
        print(f"Failed to reach the IOTA node: {e}")
        if isinstance(e, requests.exceptions.SSLError):
            print("SSL certificate verification failed. This might be due to an expired or invalid certificate.")
        elif isinstance(e, requests.exceptions.ConnectionError):
            print("This might be due to network issues or the node being down.")
        elif isinstance(e, requests.exceptions.Timeout):
            print("The request timed out. The node might be overloaded or your internet connection might be slow.")
        elif isinstance(e, requests.exceptions.TooManyRedirects):
            print("Too many redirects. The node URL might be incorrect.")
        return False

# Updated list of Shimmer testnet nodes to test
nodes = [
    'https://api.testnet.shimmer.network',
    'https://api.hornet-0.testnet.shimmer.network',
    'https://api.hornet-1.testnet.shimmer.network',
    'https://api.hornet-2.testnet.shimmer.network',
    'https://api.hornet-3.testnet.shimmer.network'
]

# Test each node
working_nodes = []
for node in nodes:
    if test_node(node):
        working_nodes.append(node)

print("\nSummary:")
if working_nodes:
    print("Working nodes:")
    for node in working_nodes:
        print(f"- {node}")
else:
    print("No working nodes found.")

print("\nIf no nodes are working, consider the following steps:")
print("1. Check your internet connection")
print("2. Temporarily disable any firewalls or antivirus software")
print("3. Try running the script on a different network")
print("4. If the issue persists, you may need to set up a local node for testing")