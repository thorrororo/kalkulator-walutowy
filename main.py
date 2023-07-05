from requests import get

print("KURSY WALUT")
print("-----------------------------------------------------------------------------")
print("Pamiętaj, aby przeczytać plik README.md")
print("-----------------------------------------------------------------------------")
a = input("Podaj walutę: ")
b = float(input("Podaj ilość PLN: "))
page = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{a}/today/?format=json")
d = page.json()
k = d["rates"][0]["mid"]
results = k*b
print("-----------------------------------------------------------------------------")
print(f"{b} " +  a.upper() +  f" = {results} PLN")
print("-----------------------------------------------------------------------------")