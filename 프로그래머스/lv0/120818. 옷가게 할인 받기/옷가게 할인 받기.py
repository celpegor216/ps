def solution(price):
    if price < 100000:
        return price
    elif price < 300000:
        return price * 0.95 // 1
    elif price < 500000:
        return price * 0.9 // 1
    else:    
        return price * 0.8 // 1