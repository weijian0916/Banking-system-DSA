import datetime

class Node:
    def __init__(self, amount, transaction_type, date=None):
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = datetime.datetime.now()
        self.next = None

def traverseList(head):
    current = head
    if current is None:
        print("No transaction yet")
        return

    while current is not None:
        date_str = current.date.strftime("%Y-%m-%d")
        print(f"Date: {date_str}")
        print(f"Type: {current.transaction_type}")
        print(f"Amount: ${current.amount}")
        print()
        current = current.next

def insertAtEnd(head, amount, transaction_type):
    newNode = Node(amount, transaction_type)
    if head is None:
        return newNode
    last = head
    while last.next is not None:
        last = last.next
    last.next = newNode
    return head

def calculateBalance(head):
    balance = 0
    current = head
    while current is not None:
        if current.transaction_type == "Deposit":
            balance += current.amount
        else:
            balance -= current.amount
        current = current.next
    return balance

#refer from https://www.geeksforgeeks.org/dsa/search-an-element-in-a-linked-list-iterative-and-recursive/
def searchByDate(head, search_date):
    current = head
    found = False
    if current is None:
        print("No transactions to search")
        return
    print(f"Searching for transactions on {search_date}")
    while current is not None:
        transaction_date = current.date.strftime("%Y-%m-%d")
        if transaction_date == search_date:
            found = True
            print(f"Date: {transaction_date}")
            print(f"Type: {current.transaction_type}")
            print(f"Amount: ${current.amount}")
            print()
        current = current.next
    if not found:
        print("No transactions found on that date.")

def history():
    head = None
    while True:
        print()
        print("Transaction Menu")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Show transaction history")
        print("4. Search transactions by date")
        print("5. Show current balance")
        print("6. Exit")
        choice = int(input("Choose an option (1-6): "))

        if choice == 1:
            amount = float(input("Enter amount to Deposit: "))
            head = insertAtEnd(head, amount, "Deposit")
            print("Deposit successful!")

        elif choice == 2:
            amount = float(input("Enter amount to Withdraw: "))
            balance = calculateBalance(head)
            if balance >= amount:
                head = insertAtEnd(head, amount, "Withdrawal")
                print("Withdrawal successful!")
            else:
                print("Not enough money!")

        elif choice == 3:
            print("Transaction History")
            traverseList(head)

        elif choice == 4:
            date_input = input("Enter date to search (YYYY-MM-DD): ")
            searchByDate(head, date_input)

        elif choice == 5:
            balance = calculateBalance(head)
            print(f"Current Balance: ${balance:.2f}")

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1-6.")

history()