MIN_DISCOUNT_PERCENT = 30

def is_good_deal(deal):
    discount = deal.get("discount_percent", 0)
    return discount >= MIN_DISCOUNT_PERCENT
