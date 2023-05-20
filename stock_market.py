import os
import pickle

if os.path.exists('stk_market.sav'):
    with open('stk_market.sav', 'rb') as f:
        corps = pickle.load(f)
else:
    corps = {"disk-orb": {"count": 10, "mr_split": "time", "worth": 0}, "minisoft": {"count": 10, "mr_split": "time", "worth": 0}, "mogang": {"count": 10, "mr_split": "time", "worth": 0}}

def dent_calc(c_name, amount_sold, amount_paid):
	ogw = corps[c_name]["worth"]
	dw = amount_sold/corps[c_name]["count"]
	ogww = 1-dw
	fw = (amount_paid*dw+ogw*ogww)
	return fw

def save_market_data():
    with open('stk_market.temp', 'wb') as f:
        pickle.dump(corps, f)
    os.replace('stk_market.temp', 'stk_market.sav')

def stock_bought(c_name, amount_sold, amount_paid):
	corps[c_name]["worth"] = dent_calc(c_name, amount_sold, amount_paid)

def stock_split_req(c_name, stock_owned):
	if corps[c_name]/stock_owned >= 10:
		corps[c_name]["count"] = corps[c_name]["count"]*2
