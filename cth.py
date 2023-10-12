

def function1(x, y):
    return (x * x) + (y * y) - 2 * x + 8 * y - 8

def function2(x, y):
    return (((x - 6) * (x - 6)) / 36) + (((y + 4) * (y + 4)) / 16)

def dis(z, x, y):
    if z == 1:
        return function1(x, y)
    else:
        return function2(x, y)

def business_model():
    while True:
        print("Pick your transaction:")
        print("1. Sustainability ratio")
        print("2. Business prediction within 3 months")
        oper2 = input("Enter your choice: ")

        if oper2 == '1':
            print("Enter selling cost together with inventory before at the start of selling period and at the end of selling period")
            kj = float(input())
            inventori_awal = float(input())
            inventori_akhir = float(input())
            kpgi = 365 * (((inventori_awal + inventori_akhir) / 2) / kj)
            print("Every", kpgi, "days, the inventory must be changed.")

            print("Enter accounts payable and credit sales (debt)")
            ls = float(input())
            credit = float(input())
            tbh = (ls / credit) * 365
            print("Business takes", tbh, "days to pay debt.")

            print("Enter accounts receivable and debit sales")
            as_ = float(input())
            debit = float(input())
            tkh = (as_ / debit) * 365
            print("Business takes", tkh, "days to receive debt.")
            break

        elif oper2 == '2':
            print("Enter the following:")
            print("Balance n/m:")
            bbb = float(input())
            print("Capital:")
            cap = float(input())
            print("Cash sales:")
            jt = float(input())
            print("Account receivable:")
            abt = float(input())
            print("non-current asset (sale):")
            jabs = float(input())
            print("Interest on savings:")
            fas = float(input())
            print("Loan:")
            pb = float(input())
            print("Received commissions:")
            kd = float(input())
            jp1 = bbb + cap + jt + abt + jabs + fas + pb + kd

            print("Cash purchase:")
            bt = float(input())
            print("Accounts payable:")
            abb = float(input())
            print("Operational expenses:")
            kp = float(input())
            print("Loan installments:")
            ap = float(input())
            jp2 = bt + abb + kp + ap

            lak1 = jp1 - jp2
            jp3 = lak1 + cap + jt + abt + jabs + fas + pb + kd
            lak2 = jp3 - jp2
            jp5 = lak2 + cap + jt + abt + jabs + fas + pb + kd
            lak3 = jp5 - jp2

            print("Rough estimate")
            print("Receivable")
            print(f"Balance n/m:                     | {bbb}   | {lak1}   | {lak2}   |")
            print(f"Capital:                         | {cap}   | {cap}   | {cap}   |")
            print(f"Cash sales:                      | {jt}   | {jt}   | {jt}   |")
            print(f"Account receivable:              | {abt}   | {abt}   | {abt}   |")
            print(f"non-current asset (sale):        | {jabs}   | {jabs}   | {jabs}   |")
            print(f"Interest on savings:             | {fas}   | {fas}   | {fas}   |")
            print(f"loan:                            | {pb}   | {pb}   | {pb}   |")
            print(f"Received commissions:            | {kd}   | {kd}   | {kd}   |")
            print(f"Total:                           | {jp1}   | {jp3}   | {jp5}   |")
            print("Payable")
            print(f"Cash purchase:                   | {bt}   | {bt}   | {bt}   |")
            print(f"Accounts payable:                | {abb}   | {abb}   | {abb}   |")
            print(f"Operational expenses:            | {kp}   | {kp}   | {kp}   |")
            print(f"Loan installments:               | {ap}   | {ap}   | {ap}   |")
            print(f"Total:                           | {jp2}   | {jp2}   | {jp2}   |")
            print("----------------------------------------------------------")
            print(f"Extra/Deficit:                   | {lak1}   | {lak2}   | {lak3}   |")
            break

        else:
            print("Error! The operator is not correct")

def main():
    while True:
        print("Hello, please enter your desired action:")
        print("0. To quit the program")
        print("1. Statement of financial position")
        print("2. Profit or loss")
        print("3. Capital return point")
        print("4. Profit model")
        print("5. Business model")
        oper = input("Enter your choice: ")

        if oper == '1':
            print("Please enter the following values:")
            abs = float(input("Equipment: "))
            as1 = float(input("Final inventory: "))
            as2 = float(input("Receivable accounts: "))
            as3 = float(input("Bank: "))
            as4 = float(input("Cash: "))
            as5 = float(input("Others (assets): "))
            l1 = float(input("Accounts payable: "))
            l2 = float(input("Others (Liabilities): "))

            wm = abs + as1 + as2 + as3 + as4 + as5 - l1 - l2
            print("Working capital is", wm)

            ep1 = float(input("Initial capital: "))
            ep2 = float(input("Additional capital: "))
            profit_or_loss = float(input("Profit/loss: "))
            ep3 = float(input("Amount you took: "))

            ma = ep1 + ep2 + profit_or_loss - ep3
            print("Final capital is", ma)

            print("\nStatement of financial position of ")
            print("\nIlliquified assets")
            print("Equipment                         ", abs)

            print("\nLiquified assets")
            print("Final inventory                   ", as1)
            print("Receivable accounts               ", as2)
            print("Bank                              ", as3)
            print("Cash                              ", as4)
            print("Others (Assets)                   ", as5)

            print("\nLiabilities")
            print("Accounts payable                  ", l1)
            print("Others (Liabilities)              ", l2)

            print("\nWorking capital                  ", wm)

            print("\nOwner's equity")
            print("Initial capital                   ", ep1)
            print("Additional capital                ", ep2)
            print("Profit/loss                       ", profit_or_loss)
            print("Amount you took                   ", ep3)
            print("Final capital                     ", ma)

        elif oper == '2':
            initial_assets = float(input("Please enter your initial assets: "))
            initial_liabilities = float(input("Please enter your initial liabilities: "))
            initial_capital = initial_assets - initial_liabilities
            print("Your initial capital is", initial_capital)

            final_assets = float(input("Please enter your final assets: "))
            final_liabilities = float(input("Please enter your final liabilities: "))
            final_capital = final_assets - final_liabilities
            print("Your final capital is", final_capital)

            profit_or_loss = final_capital - initial_capital
            print("Your profit/loss is", profit_or_loss)

            choice1 = input("Have you taken away any inventory or add additional capital? (Yes/No): ")
            if choice1.lower() == "yes":
                ambilan = float(input("Please enter the amount you took: "))
                additional_capital = float(input("Please enter the additional capital you added: "))
                profit_or_loss1 = profit_or_loss + ambilan - additional_capital
                print("Your new value for profit/loss is", profit_or_loss1)

            else:
                print("Your profit/loss is", profit_or_loss)

        elif oper == '3':
            kt = float(input("Enter your fixed cost: "))
            kbs = float(input("Enter your variable cost for each product: "))
            hj = float(input("Enter your selling price per unit: "))
            mcs = kt / (hj - kbs)
            print("Your capital return point is", mcs, "units")
            mcs1 = mcs * hj
            print("In RM is RM", mcs1)

        elif oper == '4':
            kt = float(input("Enter your fixed cost: "))
            kbs = float(input("Enter your variable cost: "))
            hj = float(input("Enter your selling price per unit: "))
            us = float(input("Enter your target profit: "))
            mcs = hj - kbs
            print("Your contribution margin per unit is", mcs)
            jp = (kt + us) / mcs
            print("Units need to be sold is", jp)

        elif oper == '5':
            business_model()

        elif oper == '0':
            break

        else:
            print("Error! The operator is not correct")

if __name__ == "__main__":
    main()
