def uah_to_usd(amount_uah, rate):
    usd = amount_uah * rate
    return usd

def usd_to_uah(amount_usd, rate):
    uah = amount_usd * 1/rate
    return uah
