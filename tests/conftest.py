import pytest
from ape.api.accounts import AccountAPI

from scripts.get_price import TOKENS, get_curve_swap_price
from scripts.utils import get_real_amount_in, setup_account


@pytest.fixture
def get_tokens() -> list:
    DAI = TOKENS["DAI"]
    USDC = TOKENS["USDC"]

    tokens = []
    # replace with the addresses of the respective tokens
    tokens.append(DAI)
    tokens.append(USDC)

    return tokens


@pytest.fixture
def user() -> AccountAPI:
    return setup_account()
