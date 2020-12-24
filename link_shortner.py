import pyshorteners as ps
a = input("Enter Url \n")
print(ps.Shortener().tinyurl.short(a))