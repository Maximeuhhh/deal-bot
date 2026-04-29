MIN_DISCOUNT_PERCENT = 10
MIN_TEMPERATURE = 10

def is_good_deal(deal):
    discount = deal.get("discount_percent", 0)
    temperature = deal.get("temperature", 0)
    return discount >= MIN_DISCOUNT_PERCENT or temperature >= MIN_TEMPERATURE
