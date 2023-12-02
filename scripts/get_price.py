import structlog
from ape import Contract, project
from ape.api.accounts import AccountAPI
from ape.contracts.base import ContractInstance
from eth_utils import to_wei

from scripts.colours import *
from scripts.constants import CURVE_META_REGISTRY_ADDRESS
from scripts.tokens import *
from scripts.utils import get_real_amount_in, setup_account

logger = structlog.getLogger(__name__)

DAI = TOKENS["DAI"]
USDC = TOKENS["USDC"]
WETH = TOKENS["WETH"]
WBTC = TOKENS["WBTC"]
MATIC = TOKENS["MATIC"]

# * cache the data first
# pool_count -> pool_list (will get address) -> get_coins -> get_meta_n_coins

# find_pool_for_coins -> get the pool address -> go to the pool ->


def get_meta_registry():
    return Contract(CURVE_META_REGISTRY_ADDRESS)


def curve_swap_from_pool(
    pool: ContractInstance,
    account: AccountAPI,
    token_in: str,
    token_out: str,
    amount: int = 0,
) -> int:
    i = 0
    j = 0
    coin_id_x = 0

    while i == j:
        coin = pool.coins(coin_id_x, sender=account)

        if coin == token_in:
            i = coin_id_x
        elif coin == token_out:
            j = coin_id_x

        if i != j:
            break

        coin_id_x += 1

    amounts_out = pool.get_dy(i, j, amount)

    return amounts_out


def curve_meta_pool(
    meta_pool: ContractInstance, account: AccountAPI, tokens: list, real_amount_in: int
) -> int:
    token_pool_address = meta_pool.find_pool_for_coins(tokens[0], tokens[1])

    if token_pool_address == "0x0000000000000000000000000000000000000000":
        logger.critical("Error: Pool not found")
        exit(-1)

    logger.info(f"Got pool: {token_pool_address}")

    pool_contract = Contract(token_pool_address)

    return curve_swap_from_pool(
        pool_contract, account, tokens[0], tokens[1], real_amount_in
    )


def get_curve_swap_price(account: AccountAPI, tokens: list, real_amount_in: int) -> int:
    meta_pool = get_meta_registry()
    amounts_out = curve_meta_pool(meta_pool, account, tokens, real_amount_in)
    input_token = project.IERC20.at(tokens[0])
    output_token = project.IERC20.at(tokens[1])

    print(
        f"{green}Tokens swapped: {yellow}{real_amount_in // 10 ** input_token.decimals()} {input_token.symbol()} {red}-> {blue}{amounts_out // (10 ** output_token.decimals())} {output_token.symbol()}",
        reset,
    )
    return amounts_out


def main():
    tokens = []
    # replace with the addresses of the respective tokens
    tokens.append(DAI)
    tokens.append(USDC)

    account = setup_account()

    amount_in = 100
    real_amount_in = get_real_amount_in(
        amount_in=amount_in, input_token=tokens[0], output_token=tokens[-1]
    )

    amounts_out = get_curve_swap_price(account, tokens, real_amount_in)
