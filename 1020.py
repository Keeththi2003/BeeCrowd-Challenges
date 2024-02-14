days = int(input())
years = days//365
months = (days%365)//30
r_days =  (days%365)%30
print(years,"ano(s)")
print(months,"mes(es)")
print(r_days,"dia(s)")