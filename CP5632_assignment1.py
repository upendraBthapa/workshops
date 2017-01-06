__author__ = 'jc449735'

# Initialize the constants,which can be used in the below functions as it is UNIVERSALLY defined

FILE = "books.csv"
MENU = "Menu: \nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"


def main():
    print("Reading List 1.0 - by Upendra B Thapa")
    booklist = []
    load_books(booklist)
    print(booklist)
    display()
    choice = input(">>>")
    while choice.lower() != 'q':
        if choice.lower() == 'r':
            required(booklist)
        elif choice.lower() == 'c':
            completed(booklist)
        elif choice.lower() == 'a':
            booklist = add()
        elif choice.lower() == 'm':
            complete_a_book(booklist)
        display()
        choice = input(">>>")
    print("{} books have been saved to {}".format(len(booklist), FILE))
    print("Have a nice day")


def display():
    """

"""
    print(MENU)


def load_books(list):
    """
   book_file <- open(FILE, 'r')
    for line in book_file:
        list.append(line.strip().split(','))
    ENDFOR
    book_file.close()
"""
    book_file = open(FILE, 'r')
    for line in book_file:
        list.append(line.strip().split(','))
    book_file.close()


def complete_a_book(list):
    """
 required_books(book_list)
    output "Enter the number of a book to mark as completed"
    try:
        input numbook
        IF list[numbook][3] = 'c':
            output "That book is already completed"
        ELSE:
            list[numbook][3] <- 'c'
            save_books(list)
            output title and author
    except ValueError:
        output "Invalid input; enter a valid number"
        complete_a_book(list)
"""
    required(list)
    print("Enter the number of a book to mark as completed")
    try:
        numbook = int(input(">>>"))
        if list[numbook][3] == 'c':
            print("That book is already completed")
        else:
            list[numbook][3] = 'c'
            book = open(FILE, 'w')
            for i in list:
                for j in i:
                    if j == "r" or j == "c":
                        print(j, end='', file=book)
                    else:
                        print(j, end=',', file=book)
                print(file=book)
            book.close()
            print("{} by {} is completed".format(list[numbook][0], list[numbook][1]))
    except ValueError:
        print("Invalid input; enter a valid number")
        complete_a_book(list)


def required(list):
    """

"""
    total = 0
    print("Required Books:")
    count = 0
    for i in list:
        if 'r' in list[count][3]:
            print("{}. {:<45s} by {:<15s} {:>10s} pages".format(count, list[count][0], list[count][1], list[count][2]))
            total += int(list[count][2])
        count += 1
    print("Total pages for {} books: {}".format(count - 1, total))


def completed(list):
    """

"""
    total_pages = 0
    print("Required Books:")
    count = 0
    for i in list:
        if 'c' in list[count][3]:
            print("{}. {:<45s} by {:<15s} {:>10s} pages".format(count, list[count][0], list[count][1],
                                                                list[count][2]))
            total_pages += int(list[count][2])
            count += 1
    print("Total pages for {} books: {}".format(count + 1, total_pages))


def add():
    """

"""
    list = []
    title = input("Title:")
    while title == "":
        print("Input can not be blank")
        title = input("Title:")
    author = input("Author:")
    while author == "":
        print("Input can not be blank")
        author = input("Author:")
    error = 1
    numpages = 0
    while error == 1:
        try:
            numpages = int(input("Pages: "))
            while numpages <= 0:
                print("Number must be >= 0")
                numpages = int(input("Pages: "))
            error = 0
        except ValueError:
            print("Invalid input; enter a valid number")
    print("{} by {}, ({} pages) added to reading list".format(title, author, numpages))
    book = [title, author, str(numpages), 'r']
    load_books(list)
    list.append(book)
    print(list)
    file = open(FILE, 'w')
    for i in list:
        for j in i:
            if j == "r" or j == "c":
                print(j, end='', file=file)
            else:
                print(j, end=',', file=file)
        print(file=file)
    file.close()


main()