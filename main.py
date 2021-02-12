from requests_html import HTMLSession

s = HTMLSession()

url_template = r"https://www.tipranks.com/stocks/{}/forecast"
symbol = input("Symbol? ").upper()
lookup_url = url_template.format(symbol)

r = s.get(lookup_url)

r.html.render(timeout=180000)

symbol_name = r.html.xpath(r'/html/body/div[1]/div/div/div[2]/article/div[2]/div/main/div[1]/section/div[2]/div[2]/div[2]/div/p/strong[2]')[0].text
status = r.html.xpath('/html/body/div[1]/div/div/div[2]/article/div[2]/div/main/div[1]/section/div[2]/div[1]/div[2]/div/div[1]/p[1]')[0].text
current_price = r.html.xpath(r'/html/body/div[1]/div/div/div[2]/article/div[2]/div/main/div[1]/section/div[2]/div[2]/div[2]/div/p/strong[7]/span')[0].text
target = r.html.xpath(r'/html/body/div[1]/div/div/div[2]/article/div[2]/div/main/div[1]/section/div[2]/div[2]/div[2]/div/div[1]/div[1]/span')[0].text
direction = r.html.xpath(r'/html/body/div[1]/div/div/div[2]/article/div[2]/div/main/div[1]/section/div[2]/div[2]/div[2]/div/div[1]/div[2]/span/text()[2]')[0].strip(")").strip()
direction_percent = r.html.xpath(r'/html/body/div[1]/div/div/div[2]/article/div[2]/div/main/div[1]/section/div[2]/div[2]/div[2]/div/div[1]/div[2]/span/strong/text()[1]')[0]
buy_count = r.html.xpath(r'/html/body/div[1]/div/div/div[2]/article/div[2]/div/main/div[1]/section/div[2]/div[1]/div[2]/div/div[2]/div/ul/li[1]/span[2]/b')[0].text
hold_count = r.html.xpath(r'/html/body/div[1]/div/div/div[2]/article/div[2]/div/main/div[1]/section/div[2]/div[1]/div[2]/div/div[2]/div/ul/li[2]/span[2]/b')[0].text
sell_count = r.html.xpath(r'/html/body/div[1]/div/div/div[2]/article/div[2]/div/main/div[1]/section/div[2]/div[1]/div[2]/div/div[2]/div/ul/li[3]/span[2]/b')[0].text

s.close()

print(f"Name: {symbol_name} -- Stock: ${symbol} -- Current: {current_price} -- Target: {target}\nStatus: {status} -- Direction: {direction} -- Direction Percent: {direction_percent}\nBuy Count: {buy_count} -- Hold Count: {hold_count} -- Sell Count: {sell_count}")
