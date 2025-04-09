from iota import Iota

iota_node = 'https://nodes.devnet.iota.org:443'
seed = 'YOUR_TEST_SEED_HERE'  # Replace with your test seed as needed  # Replace this with your new seed
api = Iota(iota_node, seed)

def generate_address():
    gna_result = api.get_new_addresses(index=0, count=1, security_level=2)
    address = gna_result['addresses'][0]
    print(f"Generated IOTA Address: {address}")

if __name__ == "__main__":
    generate_address()
