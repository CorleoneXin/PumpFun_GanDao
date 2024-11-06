from solana.rpc.api import Client
from solders.keypair import Keypair #type: ignore

# Dyw8nZe4AgbXQ6R7dySEEsegLejBnVsuyMxdpQ7aj7cQ
PRIV_KEY = "qA6ZME5AnRKcskssUMvKCpfX5pYrpv5swBiCdvwYDPEYBi3F96ohPqDJmVuUjH8B1ApMpLQZSU9jLwDTsvk4s3z"
RPC = "https://api.devnet.solana.com"
UNIT_BUDGET =  100_000
UNIT_PRICE =  1_000_000
client = Client(RPC)
payer_keypair = Keypair.from_base58_string(PRIV_KEY)