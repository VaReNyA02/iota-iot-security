import random
import string

def generate_seed():
    charset = string.ascii_uppercase + '9'
    seed = ''.join(random.choices(charset, k=81))
    return seed

if __name__ == "__main__":
    seed = generate_seed()
    print(f"Generated IOTA Seed: {seed}")
