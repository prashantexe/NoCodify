from solana.account import Account
from solana.rpc.api import Client
from solana.
# Connect to the Solana network
solana = Client("https://api.mainnet-beta.solana.com")

# Create a new account
new_account = Account.generate()

# Print the public key and secret key for the new account
print(f"Public key: {new_account.public_key()}")
print(f"Secret key: {new_account.secret_key()}")

# Check the balance of the new account
balance = solana.get_balance(new_account.public_key())
print(f"Account balance: {balance['result']['value'] / 10**9} SOL")

# Send tokens to another address
recipient_address = "<INSERT RECIPIENT ADDRESS HERE>"
amount = 1_000_000_000  # 1 SOL
transaction = solana.transfer(new_account, recipient_address, amount)

# Print the transaction ID
print(f"Transaction ID: {transaction['result']}")
