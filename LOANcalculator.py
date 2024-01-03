# Loan Calculator

def calculate_loan(principal, interest_rate, years):
    # Convert interest rate from percentage to decimal
    interest_rate_decimal = interest_rate / 100.0
    
    # Calculate the total amount to be repaid
    total_amount = principal * (1 + interest_rate_decimal * years)
    
    # Calculate the monthly payment
    monthly_payment = total_amount / (years * 12)
    
    return total_amount, monthly_payment

def get_user_input():
    principal = float(input("Enter the loan amount: $"))
    interest_rate = float(input("Enter the annual interest rate (%): "))
    years = int(input("Enter the loan duration (in years): "))
    
    return principal, interest_rate, years

def main():
    print("Welcome to the Loan Calculator!")
    
    # Get user inputs
    principal, interest_rate, years = get_user_input()
    
    # Calculate loan details
    total_amount, monthly_payment = calculate_loan(principal, interest_rate, years)
    
    # Display results
    print("\nLoan Details:")
    print("Loan Amount: $%.2f" % principal)
    print("Annual Interest Rate: %.2f%%" % interest_rate)
    print("Loan Duration: %d years" % years)
    print("\nTotal Amount to be Repaid: $%.2f" % total_amount)
    print("Monthly Payment: $%.2f" % monthly_payment)

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import ttk

def calculate_loan():
    principal = float(entry_principal.get())
    interest_rate = float(entry_interest_rate.get())
    years = int(entry_years.get())
    
    # Convert interest rate from percentage to decimal
    interest_rate_decimal = interest_rate / 100.0
    
    # Calculate the total amount to be repaid
    total_amount = principal * (1 + interest_rate_decimal * years)
    
    # Calculate the monthly payment
    monthly_payment = total_amount / (years * 12)
    
    result_label.config(text=f"Total Amount: ${total_amount:.2f}\nMonthly Payment: ${monthly_payment:.2f}")

# Create main window
root = tk.Tk()
root.title("Loan Calculator App")

# Style configuration
style = ttk.Style()
style.configure("TButton", padding=(10, 5), font=('Helvetica', 12, 'bold'))
style.configure("TLabel", font=('Helvetica', 12))

# Create and place widgets
label_principal = ttk.Label(root, text="Loan Amount ($):")
label_principal.grid(row=0, column=0, padx=10, pady=10)

entry_principal = ttk.Entry(root)
entry_principal.grid(row=0, column=1, padx=10, pady=10)

label_interest_rate = ttk.Label(root, text="Annual Interest Rate (%):")
label_interest_rate.grid(row=1, column=0, padx=10, pady=10)

entry_interest_rate = ttk.Entry(root)
entry_interest_rate.grid(row=1, column=1, padx=10, pady=10)

label_years = ttk.Label(root, text="Loan Duration (years):")
label_years.grid(row=2, column=0, padx=10, pady=10)

entry_years = ttk.Entry(root)
entry_years.grid(row=2, column=1, padx=10, pady=10)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_loan, style="TButton")
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = ttk.Label(root, text="", style="TLabel")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
