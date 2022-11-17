import getpriceamazon
import getpriceshopee

def main(url):
	if "amazon" in url:
		return getpriceamazon.getprice(url)
	if "shopee" in url:
		return getpriceshopee.getprice(url)

if __name__ == '__main__':
	#url = "https://www.amazon.com/Rain-X-5079281-2-Latitude-Water-Repellency/dp/B016NA9Y4S"
	#url = "https://shopee.ph/Landmark-Abaca-Sinamay-Angel-i.323186309.21459722511?sp_atk=04921085-9db5-4547-9a50-e48ebf138303"
	main(url)