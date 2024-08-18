sehirler1 = ["Kocaeli", "Ankara"]
plakalar1 = [41, 6]

message1 = plakalar1[sehirler1.index("Kocaeli")]
print(message1)

plakalar2 = {"Kayseri" : 38, "Trabzon" : 61}
message2 = plakalar2["Kayseri"]
print(message2)

plakalar2["Ankara"] = 6
print(plakalar2)

usersAge = {
    "GokdenizYilmaz": 21,
    "GokmenYilmaz": 45
}

print(usersAge["GokdenizYilmaz"])

users = {
    "Mehmet Kaya": {
        "age":36,
        "email":"mehmetkaya@hotmail.com"
    },
    "Ayşe Çakır": {
        "age":24,
        "email":"aysecakir31@gmail.com"
    }
}

print(users)
print(users["Ayşe Çakır"])
print(users["Mehmet Kaya"]["age"])