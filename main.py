import pyshorteners

link = input("masukan link : ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)