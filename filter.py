MIN_TEMPERATURE = 150  # Seulement les deals avec 150° ou plus

def is_good_deal(deal):
    return deal.get("temperature", 0) >= MIN_TEMPERATURE
