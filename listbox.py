from tkinter import *

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  fg="dodgerblue",
                  bg="#f7ffde",
                  width=12,
                  selectmode=MULTIPLE,
                  font=('Constanta',35))
listbox.pack()

listbox.insert(1,"Garlic bread")
listbox.insert(2,"Pizza")
listbox.insert(3,"Sushi")
listbox.insert(4,"Pasta")
listbox.insert(5,"soup")

listbox.config(height=listbox.size())

entryBox =Entry(window)
entryBox.pack

submitButton =Button(window,text="submit",command=submit)
submitButton.pack()

addButton =Button(window,text="add",command=add)
addButton.pack()

deleteButton =Button(window,text="delete",command=delete)
deleteButton.pack()


window.mainloop()
