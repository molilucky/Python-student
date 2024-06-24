from email.mime import application

import requests
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
code = r.status_code
print(code)
type1 = r.headers['content-type']
print(type1)



