global self


class book():
    def __init__(self, Name, ISBN, Author):
        self.Name = []
        self.ISBN = []
        self.Author = []


class Shelf():
    def add_books(Name, ISBN, Author):
        self.Name.append(Name)
        self.ISBN.append(ISBN)
        self.Author.append(Author)

    def show_catalog(self):
        print("Name \t \t ISBN \t \t Author")
        for i in range(n):
            print(self.Name[i], "\t", "\t", self.ISBN[i],
                  "\t", "\t", self.Author[i])


n = int(input("Enter the number of books to be added : "))
for i in range(n):
    Name = input("Book Name : ")
    ISBN = int(input("ISBN Number : "))
    Author = input("Author's Name : ")
    Shelf.add_books(Name, ISBN, Author)
