myList = [1,2,3]
myString = "My string"

print(len(myList))
print(len(myString))
print(type(myString))
print(type(myList))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")
        
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Movie silindi.")

m = Movie("Film adı", "Yönetmen adı", 120)
print(str(m))
print(m)
print(len(m))

