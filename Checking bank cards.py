import requests
def summ(number_l):
    number_l = [num * 2 if index % 2 == 0 else num for index, num in enumerate(number_l)]
    for i in range(len(number_l)):
        if number_l[i] >= 10:
            number_l[i] = number_l[i] - 9
    n_sum = sum(number_l) / 2
    if int(n_sum) == n_sum:
        return("Verification: Verification successful")
    else:
        return("Verification: Verification failed")
number = (input("Number: "))
if len(number) == 16:
    print("Length: True")
else:
    print("Length: False")
number_l = list(map(int, number))
print(summ(number_l))
print("MII:", number_l[0],"    BIN:", " ".join(map(str, number_l[:6])),"    PAN:", " ".join(map(str, number_l[6:15])))
bin = int("".join(map(str, number_l[:6])))
url = "https://bin-ip-checker.p.rapidapi.com/"

querystring = {"bin":bin}

payload = { "bin": bin }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "4d7f9877e1mshc202c1b595631f2p13facfjsn2cdb5b9b1269",
	"X-RapidAPI-Host": "bin-ip-checker.p.rapidapi.com"
}

response = (requests.post(url, json=payload, headers=headers, params=querystring)).json()

print("Проверка bin-ip-checker:")
def print_values(dictionary):
    for key,value in dictionary.items():
        if isinstance(value,dict):
            print_values(value)
        else:
            print(f"{key}:{value}")
print(print_values(response))