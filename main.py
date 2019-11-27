from tkinter import *
from SaveFileReadFile import *

def add():
      line = codeBook.get() + ";" + nameBooks.get() + ";" + yearOfManufacture.get()
      SaveFile(line)
      codeBook.set("")
      nameBooks.set("")
      yearOfManufacture.set("")
      showBooks()
def showBooks():
      arrBooks = ReadFile()
      listBox.delete(0, END)
      for item in arrBooks:
            listBox.insert(END, item)

def Sort():
      arrBooks = ReadFile()

      for i in range(len(arrBooks)):
            for j in range(len(arrBooks)):
                  a = arrBooks[i]
                  b = arrBooks[j]
                  if b[2]<a[2]:
                        arrBooks[j] = a
                        arrBooks[i] = b
      listBox.delete(0, END)
      for item in arrBooks:
            listBox.insert(END, item)

def Search():
      arrBooks = ReadFile()
      NameBook = nameBooks.get()
      NameBook = NameBook.lower()
      found = False
      searchBooks = []
      for books in arrBooks:
            OnlyName = books[1]
            arrName = OnlyName.split(" ")
            for i in arrName:
                  i = i.lower()
                  if i == NameBook:
                        found = True
                        searchBooks.append(books)
      if found == True:
            listBox.delete(0, END)
            for item in searchBooks:
                  listBox.insert(END, item)
      else:
            listBox.delete(0, END)
            item = "NOT FOUND"
            listBox.insert(END, item)
root = Tk()
root.title("Book store")
root.resizable(height=False, width=False)
root.minsize(height=450, width=500)

Label(root, text = "LIST BOOKS", fg = "blue",
      font = ("cambria", 25)).grid(row = 0, columnspan = 2)

scrollbar = Scrollbar()
scrollbar.grid(row = 1, column = 2, ipady = 100)

listBox = Listbox(root, height = 15, width = 90, yscrollcommand = scrollbar.set)
listBox.grid(row = 1, columnspan = 2)

scrollbar.config(command = listBox.yview)

showBooks()

Label(root, text = "Code:",
      font = ("cambria", 15)).grid(row = 2, column = 0)
codeBook = StringVar()
Entry(root, textvariable = codeBook,
      font = (20), width = 45).grid(row = 2, column = 1)

Label(root, text = "Name:",
      font = ("cambria", 15)).grid(row = 3, column = 0)
nameBooks = StringVar()
Entry(root, textvariable = nameBooks,
      font = (20), width = 45).grid(row = 3, column = 1)

Label(root, text = "Manufacture:",
      font = ("cambria", 15)).grid(row = 4, column = 0)
yearOfManufacture = StringVar()
Entry(root, textvariable = yearOfManufacture,
      font = (20), width = 45).grid(row = 4, column = 1)

FrameButton = Frame()
Button(FrameButton, text = "Add",font = ("cambria", 12),
       relief = GROOVE, command = add).pack(side = LEFT, padx = 1, pady = 8)
Button(FrameButton, text = "Search",font = ("cambria", 12),
       relief = GROOVE, command = Search).pack(side = LEFT, padx = 1, pady = 8)
Button(FrameButton, text = "Sort",font = ("cambria", 12),
       relief = GROOVE, command = Sort).pack(side = LEFT, padx = 1, pady = 8)
Button(FrameButton, text = "Close",font = ("cambria", 12),
       relief = GROOVE, command = root.quit).pack(side = LEFT, padx = 1, pady = 8)
FrameButton.grid(row = 5, column = 1)

root.mainloop()