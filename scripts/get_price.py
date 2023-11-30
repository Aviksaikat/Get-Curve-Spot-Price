from ape import project
from ape.api.accounts import AccountAPI

from scripts.addresses import CURVE_POOL_Address
from scripts.tokens import *
from scripts.utils import get_real_amount_in

DAI = TOKENS["DAI"]
USDC = TOKENS["USDC"]
WETH = TOKENS["WETH"]
WBTC = TOKENS["WBTC"]
MATIC = TOKENS["MATIC"]


def get_curve_pool():
    return project.ICurvePool.at(CURVE_POOL_Address)


def curve_swap_in(
    pool, _from: AccountAPI, tokenIn: str, tokenout: str, amount: int = 0
) -> int:

    i = 0
    j = 0
    coinIdx = 0

    while i == j:
        coin = pool.coins(coinIdx)

        if coin == tokenIn:
            i = coinIdx
        elif coin == tokenOut:
            j = coinIdx

        if i != j:
            break

        coinIdx += 1

    amountsOut = pool.get_dy.call(i, j, amount, sender=_from)

    return amountsOut


def get_curve_swap_price(account: AccountAPI, tokens: list):
    curve_pool = get_curve_pool()
    amounts_out = curve_swap_in(curvePool, account, tokens[0], tokens[1], ETH_AMOUNT)

    print(
        f"Tokens swapped {tokens[0]} -> {tokens[1]}: ",
        amountsOutCurve // (10 ** WETH.decimals()),
    )


def main():
    tokens = []
    # replace with the addresses of the respective tokens
    tokens.append(DAI)
    tokens.append(USDC)

    amount_in = 100
    real_amount_in = get_real_amount_in(
        amount_in=amount_in, input_token=tokens[0], output_token=tokens[-1]
    )

    get_curve_swap_price(account, tokens)
