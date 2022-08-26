# **args

# {
#     "id": 1,
#     "name": "Bruce",
#     "age": 40
# }

def save_users(**user):
    print(user)


save_users(id=1, name="Bruce", age="40")
save_users(id=1, name="Bruce", l_name="Wayen")
