import json
from json.decoder import JSONDecodeError




class transactions:
    def __init__(self, title, amount, types, note=""):
        self.title = title
        self.amount = amount
        self.types = types
        self.note = note

    def display_info(self):
        print("transaction: \n expense : {self.title} \n amount:{self.amount} \n types : {self.types} \n note:{self.note} \n")


class bank :
    def __init__(self):
        self.wallet = []

    def add_transaction (self,transaction) :
        self.wallet.append (transaction)

    def del_transaction(self,title):
        for transaction in self.wallet :
            if transaction.title == title :
                self.wallet.remove(transaction)
                return f"{title} has been removed !!"
        return f"{title} is not found !!"

    def display(self):
        if not self.wallet :
            return f"no transaction it's empty mane "
        return f"\n".join([transaction.display_info() for transaction in self.wallet])
    
    def search_wallet(self, query):
        found = [trans for trans in self.wallet if query.lower() in trans.title.lower() or query.lower() in trans.types.lower()]
        if not found:
            return f"no transactions"
        return f"\n".join([transaction.display_info() for transaction in found]) 
    
    def save_file(self,file_name="wallet.json"):
        data = [{'expense': transaction.title , 'amount': transaction.amount, 'types':transaction.types, 'note': transaction.note } for transaction in self.wallet ]
        with open (file_name, "w") as file :
            json.dump(data,file)

    def load_file(self, file_name="wallet.json"):
        try:
            with open(file_name, "r") as file:
             data=json.load(file)
             self.wallet = [transactions(trans['expense'],trans['amount'],trans['types'],trans['note'])for trans in data]
             print("loaded succesfully")
        except FileNotFoundError:
            return "File not found."

def main():
    wallet= bank()
    
    while True:
        print("-------------welcome to boogeyman bankingsystem------------- \n")
        print("1.add transaction")
        print("2.remove all transaction")
        print("3.display a transaction")
        print("4.search transaction")
        print("5.save file")
        print("6.load file")
        print("7.exit")
        choice = str(input("enter your choice good sir !: \n"))
        
        if choice == "1":
            title = str(input("enter the title : \n"))
            amount = str(input ("enter the amount good sir !: \n"))
            types =str(input("what is the types ? \n"))
            note =str(input("a note ? \n"))
            transaction = transactions(title,amount,types,note)
            wallet.add_transaction(transaction)
            print (f"{title} added succesfully")
        elif choice == "2":
            title=input("enter a name: \n")
            print(wallet.del_transaction(title))
        elif choice == "3":
            print(wallet.display())

        elif choice =="4":
            query = input("enter a name to search !:\n")
            print (wallet.search_wallet(query))

        elif choice == "5":
            wallet.save_file()
            print("saved as json!!!")

        elif choice == "6":
            wallet.load_file()
            
        elif choice == "7":
            break

if __name__ in "__main__":
    main()

