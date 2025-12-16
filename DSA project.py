import datetime


class Node:
    def __init__(self,amount,transaction_type, date):
        self.amount=amount
        self.transaction_type=transaction_type
        self.date=datetime.datetime.now()
        self.next=None





def traverseList(head):

    current=head
    if current is None:
        print("No transaction yet")
    while current is not None:
        date_str = current.timestamp.strftime("%Y-%m-%d %H:%M:%S")

        print(f"Date: {date_str}")
        print(f"Type: {current.type}")
        print(f"Amount: ${current.amount}")
        current=current.next
    print()


def insertAtEnd(head,amount,transaction_type):
    newNode=Node(amount,transaction_type)


    if head is None:
        return newNode

    last=head

    while last.next is not None:
        last=last.next

    last.next=newNode

    return head


def history():
    head=None

    while True:
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Show transaction history")
        print("4. Exit")

        choice = int(input("Choose an option (1-4): "))

        if choice == 1:
            amount = float(input("Enter amount to Deposit: "))
            head = insertAtEnd(head, amount, "Deposit")
            traverseList(head)


        elif choice ==3:
            traverseList(head)



history()

