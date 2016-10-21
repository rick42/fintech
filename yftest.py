from yahoo_finance import Share


# Get data about Apple share
a = raw_input()
apple = Share(a)

# Get the share price
print (apple.get_price())
# OUTPUT: 116.16

# Since data is changing constantly, you can refresh the share and get the new data
apple.refresh()
print (apple.get_price())
# OUTPUT: 116.3811

# You can access the full share dataset  
print (apple.data_set)

print (apple.get_200day_moving_avg())

print (apple.get_50day_moving_avg())

print (apple.get_avg_daily_volume())

print (apple.get_book_value())

print (apple.get_change())

print (apple.get_days_high())

print (apple.get_days_low())

print (apple.get_dividend_share())

print (apple.get_dividend_yield())

print (apple.get_earnings_share())

print (apple.get_ebitda())

#print (apple.get_historical())

print (apple.get_info())

print (apple.get_market_cap())

print (apple.get_name())

print (apple.get_open())

print (apple.get_percent_change())

print (apple.get_prev_close())

print (apple.get_price())

print (apple.get_price_book())

print (apple.get_price_earnings_growth_ratio())

print (apple.get_price_earnings_ratio())

print (apple.get_price_sales())

print (apple.get_short_ratio())

print (apple.get_stock_exchange())

#print (apple.get_trade_datetime())

print (apple.get_volume())

print (apple.get_year_high())

print (apple.get_year_low())