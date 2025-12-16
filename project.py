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
        date_str = current.date.strftime("%Y-%m-%d %H:%M:%S")
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

def history():
    head = None
    while True:
        print("Transaction Menu")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Show transaction history")
        print("4. Exit")
        choice = int(input("Choose an option (1-4): "))

        if choice == 1:
            amount = float(input("Enter amount to Deposit: "))
            head = insertAtEnd(head, amount, "Deposit")
            print("\nDeposit successful!")

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
            print("Exiting...")

        else:
            print("Invalid option. Please choose 1-4.")

history()