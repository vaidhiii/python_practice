def add_note():
    with open("notes.txt","a") as f:
        note=input("Enter your note: ")
        f.write(note)
        f.write("\n")

def view_notes():
    with open("notes.txt","r") as f:
        data=f.read()
        print(data)

def menu():
    a,b,c=1,2,3
    print("1. Add Note.\n2. View Notes.\n3. Exit.")

print("--------Notes App--------")
while True:
    try:
        menu()
        choice=int(input("Enter Your Choice:"))
        if choice==1:
            add_note()
            print("Your note added successfully.")
        elif choice==2:
            view_notes()
        elif choice==3:
            print("Goodbye!")
            break
    except FileNotFoundError:
        print("No notes found.")
    except ValueError:
        print("Enter valid choice.")