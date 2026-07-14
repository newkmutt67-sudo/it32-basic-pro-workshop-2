quantity = int(input("quantity of gun :"))
cost_price = int(input("cost_price :"))
sell_price = int(input("sell_price :"))
team_members = int(input("team_members :"))

total_cost = cost_price*quantity
total_revenue = sell_price*quantity
net_profit = total_revenue - total_cost
boss_commission = net_profit*0.2
minnion = (net_profit - boss_commission)/team_members

print("--------------")
print("total_cost: " ,total_cost, "baht")
print("total_revenue: " ,total_revenue, "baht")
print("net_profit: " ,net_profit, "baht")
print("boss_commission: " ,boss_commission, "baht")
print("minnion: " ,minnion, "baht")