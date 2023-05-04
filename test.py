from solana.rpc.api import Client

# Connect to Solana devnet
client = Client("https://api.devnet.solana.com")

# Specify the address to check balance for
address = "0x042bDdB896fa2B4F5993e3926b7dD53B27f9321E"

# Get the balance for the specified address
balance = client.get_balance(address)

# Print the balance
print(f"Balance for {address}: {balance} lamports")
