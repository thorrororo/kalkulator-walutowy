from requests import get
print("KURSY WALUT")
a = input("Podaj walutę (USD/JPY/EUR/CHF/GBP): ")
page = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{a}/today/?format=json")
d = page.json()
k = d["rates"][0]["mid"]
print(f"1 {a} = {k} PLN")