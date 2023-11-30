# calculate real_amount_in based on token decimals
def get_real_amount_in(amount_in: int, input_token, output_token) -> int:
    if input_token.decimals() != output_token.decimals():
        real_amount_in = amount_in * 10 ** input_token.decimals()
    else:
        real_amount_in = amount_in * 10 ** output_token.decimals()

    return real_amount_in

#* need this for ape
def main():
    pass