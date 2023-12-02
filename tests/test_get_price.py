from scripts.get_price import get_curve_swap_price
from scripts.utils import get_real_amount_in


def test_get_dai_usd_swap_price(get_tokens, user):
    tokens = get_tokens

    amount_in = 100
    real_amount_in = get_real_amount_in(
        amount_in=amount_in, input_token=tokens[0], output_token=tokens[-1]
    )

    amounts_out = get_curve_swap_price(user, tokens, real_amount_in)

    assert amounts_out > 0, "Opps Test Failed!!"
