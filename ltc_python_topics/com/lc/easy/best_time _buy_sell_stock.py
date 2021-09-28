#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def buying_selling_best_time(Stock_data):
    max_profit = 0
    min_price = float('inf')

    for i in Stock_data:
        min_price = min(min_price, i)
        day_profit = i - min_price
        max_profit = max(max_profit, day_profit)
    return max_profit


our_data = [7,1,5,3,6,4]
print(buying_selling_best_time(our_data))




