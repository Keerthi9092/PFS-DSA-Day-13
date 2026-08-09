# #implementation of stack by files
# #undo and redo operations
# undo_stack=[]
# redo_stack=[]
# filename="text.txt"
# with open(filename,'w') as f:
#     pass
# while True:
#     print("\n1.Write")
#     print("2.Undo")
#     print("3.Redo")
#     print("4.Display")
#     print("5.Exit")
#     choice=int(input("Enter choice: "))
#     if choice==1:
#         text=input("Enter any text: ")
#         undo_stack.append(text)
#         redo_stack.clear()
#         with open(filename,'a') as f:
#             f.write(text+"\n")
#         print("Text passed to file successfully!!!!")
#     elif choice==2:
#         if len(undo_stack)==0:
#             print("nothing to Undo...")
#         else:
#             last=undo_stack.pop()
#             redo_stack.append(last)
#             with open(filename,'w')as f:
#                 for line in undo_stack:
#                     f.write(line+"\n")
#             print("Stored undo successfully...")
#     elif choice==3:
#         if len(redo_stack)==0:
#             print("nothing to redo...")
#         else:
#             text=redo_stack.pop()
#             undo_stack.append(text)
#             with open(filename,'a')as f:
#                 f.write(text+'\n')
#             print("Redo successfully completed...")
#     elif choice==4:
#         print("\nData in the file")
#         with open(filename,'r')as f:
#             data=f.read()
#             if data=='':
#                 print("File is Empty...")
#             else:
#                 print(data)
#     elif choice==5:
#         print("Operation Ended...")
#         break
#     else:
#         print("Invalid choice...")
        
        
# #check balanced or not
# stack=[]
# exp=input("Enter expressions: ")
# balanced=True
# for ch in exp:
#     if ch in '([{':
#         stack.append(ch)
#     elif ch in ')]}':
#         if len(stack)==0:
#             balanced=False
#             break
#         top=stack.pop()
#         if (ch==')' and top!='(') or (ch==']' and top!='[') or (ch=='}' and top!='{'):
#             balanced=False
#             break
# if balanced:
#     print(exp,"is balanced")
# else:
#     print(exp,"is not balanced")


# ==========================================
# Day 13 - Stack Implementation Using Files
# Date: 07-07-2026
# ==========================================

FILE_NAME = "stack.txt"


# -----------------------------
# Push Operation
# -----------------------------
def push(value):
    with open(FILE_NAME, "a") as file:
        file.write(str(value) + "\n")

    print(value, "pushed into stack")


# -----------------------------
# Pop Operation
# -----------------------------
def pop():
    try:
        with open(FILE_NAME, "r") as file:
            stack = file.readlines()

        if len(stack) == 0:
            print("Stack Underflow")
            return

        removed = stack.pop().strip()

        with open(FILE_NAME, "w") as file:
            file.writelines(stack)

        print("Popped element:", removed)

    except FileNotFoundError:
        print("Stack is empty")


# -----------------------------
# Peek Operation
# -----------------------------
def peek():
    try:
        with open(FILE_NAME, "r") as file:
            stack = file.readlines()

        if len(stack) == 0:
            print("Stack is empty")
            return

        print("Top element:", stack[-1].strip())

    except FileNotFoundError:
        print("Stack is empty")


# -----------------------------
# Display Stack
# -----------------------------
def display():
    try:
        with open(FILE_NAME, "r") as file:
            stack = file.readlines()

        if len(stack) == 0:
            print("Stack is empty")
            return

        print("\nStack elements:")

        for value in reversed(stack):
            print(value.strip())

    except FileNotFoundError:
        print("Stack is empty")


# -----------------------------
# Menu
# -----------------------------
while True:

    print("\n========== STACK ==========")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = input("Enter value: ")
        push(value)

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid choice")