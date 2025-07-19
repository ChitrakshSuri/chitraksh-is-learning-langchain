from typing import TypedDict

class Person(TypedDict):
    name: str 
    age: int

new_person: Person={'name':'Ghanshyam', 'age': '32'}

print (new_person)