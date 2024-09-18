class Person:
    pass
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print("İnit metdou çalıştı.")

p1 = Person("Ali", 1992)
p2 = Person("Ayşe", 2003)

print(f"name: {p1.name}, year: {p1.year}")
print(f"name: {p1.name}, year: {p2.year}")

