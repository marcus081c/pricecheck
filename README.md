# Pricecheck

Allows you to obtain the price of products from online shops programmatically and send notifications (i.e. slack) if a certain price condition is satisfied. The script will continue to query the prices **indefinitely** until exited.

**Currently only supports amazon.com and shopee**

Requirements: pip install slack_sdk, aiohttp, selenium, bs4, requests. chromedriver.exe is also needed on the same directory as the scripts.

How to run: 

**Windows**

- Run "Python pricecheck.py" in cmd
- Enter a url or a file name containing a list of urls separated by new lines.
