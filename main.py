from requests import get

print("\033[93m{}\033[00m".format("-----------------------------------------------------------------------------"))
print("WITAJ W KALKULATORZE WALUT")
print("\033[93m{}\033[00m".format("-----------------------------------------------------------------------------"))
a = input("Podaj walutę: ")
a = a.upper()

try:
    b = float(input(f"Podaj ilość {a}: "))

except:
    print("\033[91m{}\033[00m".format("-----------------------------------------------------------------------------"))
    print("Podana dana, powinna być liczbą.")
    print("\033[91m{}\033[00m".format("-----------------------------------------------------------------------------"))
    b = float(input(f"Podaj ilość {a}: "))

page = get(f"http://api.nbp.pl/api/exchangerates/rates/a/{a}/today/?format=json")

try:
    d = page.json()
    k = d["rates"][0]["mid"]
    results = k * b
    print("\033[94m{}\033[00m".format("-----------------------------------------------------------------------------"))
    print(f"{b} " + a.upper() + f" = {results} PLN")
    print("\033[94m{}\033[00m".format("-----------------------------------------------------------------------------"))

except:
    print("\033[91m{}\033[00m".format("-----------------------------------------------------------------------------"))
    print("Błąd podczas pobierania danych z API. Podana waluta nie znajduje się w API.")
    print("\033[91m{}\033[00m".format("-----------------------------------------------------------------------------"))
