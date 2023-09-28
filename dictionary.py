print("Create a dictionary in Python\n")
d1 = {"name":{"first name":"pavithri","second name":"apeksha"},"age":22,"profession":"student"}
print(d1)
print("\nAdding Elements")
d2={}
d2["one"]=1
d2["name"]="Apeksha"
print(d2)
print("Update dictionary")
d2["name"]="Pavithri"
print(d2)
print("\nAssecing element in dictionary")
print(d2.get("one"))
print(d2.get("name"))
print("\nDeleting elements in dictionary")
d2.pop("one")
print(d2)
