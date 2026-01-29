def generate_hint(deviation, smoothness):
    if deviation > 0.05:
        return "reduce lateral hand deviation"
    if smoothness > 0.025:
        return "slow down wrist movement"
    return "maintain current technique"
