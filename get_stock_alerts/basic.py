from yahoo_fin import stock_info as si
import pprint as pp

symbol = 'HDFCBANK.NS'

print(si.get_live_price(symbol))


print(si.get_data(symbol))

pp.pprint(si.get_quote_table(symbol))

pp.pprint(si.get_stats(symbol))

pp.pprint(si.get_holders(symbol))

pp.pprint(si.get_analysts_info(symbol))

pp.pprint(si.get_income_statement(symbol))

pp.pprint(si.get_balance_sheet(symbol))

pp.pprint(si.get_cash_flow(symbol))
