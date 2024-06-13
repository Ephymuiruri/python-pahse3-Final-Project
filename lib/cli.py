from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from User_management import (
    exit_program,
    create_user,
    get_all_users,
    find_user_by_id,
)
from Money_management import (
    make_payment,
    find_payment,
    find_payments_user,
    get_all_payments,

    make_deposit,
    find_deposit_by_id,
    find_deposit_user,
    get_all_deposits,
)
from loan_management import (
    make_loan,
    get_all_loans,
    find_loan_by_id,
    find_user_loans,
)
from Bank_management import(
    delete_user,
    delete_payment,
    deleteDeposit,
    delete_loan,
    create_manager,
    delete_manager,
    get_all_managers,
    find_manager_by_id,
)

console = Console()

def main():
    while True:
        menu()
        choice = input("> ")
        handle_choice(choice)

def menu():
    console.clear()
    
    # Title
    title = Text("Wachira Financial Institution", style="bold cyan")
    console.print(title, justify="center")
    
    # User Functions Section
    user_section = Panel(
        Text("USER FUNCTIONS\n"
             "1. Create a new customer Account\n"
             "2. Find a customer using their id\n"
             "3. Get a list of all customers names", style="green"),
        title="User Functions",
        border_style="green"
    )
    
    # Deposit Functions Section
    deposit_section = Panel(
        Text("DEPOSIT FUNCTIONS\n"
             "4. Deposit money into a customer's account\n"
             "5. Get deposits by a specific customer\n"
             "6. Find a deposit using the deposit_id\n"
             "7. Get a list of all deposits", style="yellow"),
        title="Deposit Functions",
        border_style="yellow"
    )
    
    # Payment Functions Section
    payment_section = Panel(
        Text("PAYMENT FUNCTIONS\n"
             "8. Make a payment to a customer account\n"
             "9. Find payments made by a specific customer\n"
             "10. Find payments by payment id\n"
             "11. Get a list of all payments", style="magenta"),
        title="Payment Functions",
        border_style="magenta"
    )
    
    # Loan Management Section
    loan_section = Panel(
        Text("LOAN MANAGEMENT FUNCTIONS\n"
             "12. Apply and receive a loan\n"
             "13. Find loans given to a specific user\n"
             "14. Find a loan using the loan id\n"
             "15. Get a list of all loans", style="blue"),
        title="Loan Management Functions",
        border_style="blue"
    )
    
    # Management Section
    management_section = Panel(
        Text("MANAGEMENT FUNCTIONS\n"
             "16. Delete a User Account\n"
             "17. Delete a deposit\n"
             "18. Delete a payment\n"
             "19. Delete a loan\n"
             "20. Create a manager\n"
             "21. Delete a manager\n"
             "22. Get a list of all managers\n"
             "23. Find a manager using the manager id", style="red"),
        title="Management Functions",
        border_style="red"
    )
    
    console.print(user_section)
    console.print(deposit_section)
    console.print(payment_section)
    console.print(loan_section)
    console.print(management_section)
    
    # Exit Option
    console.print(Text("0. Exit the program", style="bold red"), justify="center")

def handle_choice(choice):
    if choice == "0":
        exit_program()
    elif choice == "1":
        create_user()
    elif choice == "2":
        find_user_by_id()
    elif choice == "3":
        get_all_users()
    elif choice == "4":
        make_deposit()
    elif choice == "5":
        find_deposit_user()
    elif choice == "6":
        find_deposit_by_id()
    elif choice == "7":
        get_all_deposits()
    elif choice == "8":
        make_payment()
    elif choice == "9":
        find_payments_user()
    elif choice == "10":
        find_payment()
    elif choice == "11":
        get_all_payments()
    elif choice == "12":
        make_loan()
    elif choice == "13":
        find_user_loans()
    elif choice == "14":
        find_loan_by_id()
    elif choice == "15":
        get_all_loans()
    elif choice == "16":
        delete_user()
    elif choice == "17":
        deleteDeposit()
    elif choice == "18":
        delete_payment()
    elif choice == "19":
        delete_loan()
    elif choice == "20":
        create_manager()
    elif choice == "21":
        delete_manager()
    elif choice == "22":
        get_all_managers()
    elif choice == "23":
        find_manager_by_id()
    else:
        console.print("[bold red]Invalid choice[/bold red]")

if __name__ == "__main__":
    main()
