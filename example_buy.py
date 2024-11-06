from pump_fun import buy
import utils
# Buy Example

mint_str = "FMeZhmV8Jrb7KNsRRNxPDo6na336DppW56ixehypump"

sol_in = 0.1
slippage = 25
buy(mint_str, sol_in, slippage)

# utils.get_token_price(mint_str)