contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
def mydict(dict):
    for item in dict.items():
        print(item)
    
print(mydict(contact))
