import getprice
import send_pricetoslack
import json

def notif_cond(price):
	for i in price:
		if i["item"] == "B016NA9Y4S" and i["price"] == "16.57":
			send_pricetoslack.slack(json.dumps(i))

def read_urlfile(data):
	 with open(data, "r", encoding="utf-8") as f:
	 	url = f.read().splitlines()
	 return url

def check_data(data):
	price_arr = []
	if "http" in data:
		return getprice.main(data)
	else:
		url_arr = read_urlfile(data)
		for i in url_arr:
			price_arr.append(getprice.main(i))
		return price_arr


def main():
	while True:
		data = input("enter the url or url dictionary file:\n")
		if 'exit' == data:
			break
		price = check_data(data)
		print(price)
		print("Done")
		notif_cond(price)

if __name__ == '__main__':
	main()