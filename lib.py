class book():
    def __init__(self, Name, ISBN, Author):
        self.Name = Name
        self.ISBN = ISBN
        self.Author = Author

    def __str__(self):
        return f"{self.Name} {self.ISBN} {self.Author}"

    def borrow_book(self, borrower):
        if self.is_available():
            self.borrow = borrower
        else:
            print('book is not available right now. ')

    def return_book(self):
        pass


class Shelf():
    def __init__(self, genre):
        self.genre = genre
        self.Books = []

    def add_books(self, Name, ISBN, Author):
        self.Books.append(book(Name, ISBN, Author))

    def show_catalog(self):
        for i in self.Books:
            print(i)
        # print("Name \t \t ISBN \t \t Author")
        # for i in range(n):
        #     print(self.Name[i], "\t", "\t", self.ISBN[i],
        #           "\t", "\t", self.Author[i])

    def get_books_count(self, count):
        self.count = count
        return len(self.Books)

    def remove_book(self, Name):
        self.Books.remove(Name)

    def populate_book(self, file_name):
        workbook = xl.load_workbook(filename=file_name)
        sheet = workbook.active
        dim = sheet.calculate_dimension()
        for row in sheet[dim]:
            self.add_books(book(**tuple(row)))


n = int(input("Enter the number of books to be added : "))
for i in range(n):
    Name = input("Book Name : ")
    ISBN = int(input("ISBN Number : "))
    Author = input("Author's Name : ")
    sh = Shelf(input("Enter the Genre :"))
    sh.add_books(Name, ISBN, Author)

sh.show_catalog()
