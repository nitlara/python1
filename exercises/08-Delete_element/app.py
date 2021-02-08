people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    hello=[]
    for i in people:
        if (i != person_name):
            hello.append(i)
    return(hello)

           


print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))


