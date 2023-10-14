import requests
goodcodes = [100, 101, 102, 103, 200, 201, 202, 203, 204, 205, 206, 207, 208, 226, 300, 301, 302, 303, 304, 305, 306, 307, 308]
print("SitePinger")
print("by holinim (watermelon46)")
url = input("Введите URL сайта (с http:// или https://): ")
showcontent = input("Показывать содержимое сайта [Y/N]? ")
if showcontent == "Y" or showcontent == "y":
    showcontent = True
else:
    showcontent = False
requests.get(url)
r = requests.get(url) 
if showcontent:
    print(r.content)
if r.status_code <= 308:
    brick = "нет"
elif r.status_code == 401:
    brick = "нет, нужна авторизация"
else:
    brick = "да"
print("\n"*100)
print("Статус сайта:\nURL: "+url+"\nHTTP код: "+str(r.status_code), "\nЛежит:", brick)
