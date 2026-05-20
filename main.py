'''This is afarm profit calculator. (Later feature will ask for how many crops being farmed and how many of each.) Current version will ask for total corn and soybeans,
        '''
import sys

def get_float(question):
        while True:
                try:
                        value = float(input(question))
                except ValueError:
                        print("That is not a valid number. Please try again.\n")
                else:
                        return value


def main():

        while True:
                pick = input("Hello! Welcome to the farm calculator. What would you like to configure today?\nOPTIONS: \nPOSITIVES, \nNEGATIVES, \nALL, \nQ to quit.\n")
                if pick.upper() == ("POSITIVES"):
                        additives()
                elif pick.upper() ==("NEGATIVES"):
                        negatives()
                elif pick.upper() ==("ALL"):
                        all()
                elif pick.upper() == ("Q"):
                        sys.exit()
                else: 
                        print("I couldn't quite catch what your input. Please select from the options listed.\n")
        

def additives():
        # Figuring Crops
        
        total_corn = get_float("How many total acres of corn did you plant?")

        
        total_soybeans = get_float("How many total acres of soybeans did you plant? ")

        print(f"Total acres farmed: {float(total_corn) + float(total_soybeans)}")

        #Finding Population.
        pop_total_corn = get_float("What was your average population per field in corn?")
        pop_total_beans = get_float("What was your average population per field in beans?")
        print(f"The stand rate is about 95%, so you can expect about {pop_total_corn * 0.95} corn stalks, and {pop_total_beans * 0.95} beans.")
        #Finding total average bushels expected.
        bushels_corn = get_float("How many bushels do you think you will average across your acres of corn? ")
        bushels_beans = get_float("How many bushels do you think you will average across your acres of beans?")
              
        #Finding comodity prices.
        price_corn = get_float("What price do you expect to sell your corn at on average?")
        price_beans = get_float("What price do you expect to sell your beans at on average?")
        #Final Print Statement.
        total_corn_plus = (bushels_corn * total_corn) * price_corn
        total_beans_plus = (bushels_beans * total_soybeans) * price_beans
        final_plus = total_beans_plus + total_corn_plus
        print("-----TOTAL:-----")
        print(f"In total, based on {price_corn} corn and {price_beans} beans, you're looking at:\n${total_corn_plus} roughly from corn,\n \
        and ${total_beans_plus} roughly from beans.")
        print(f"This totals out to be: {total_beans_plus + total_corn_plus} ")

        return final_plus

def negatives():

        '''COSTS'''
        #seed per acre
        seed_cost = get_float("What was your total seed cost?")
        fert_cost = get_float("What was your fertilizer costs in total?")
        rent_cost = get_float("What are your total rent costs?")

        print("-----COSTS-----")
        total_costs = seed_cost + fert_cost + rent_cost
        print(f"Your total costs come out to be {seed_cost + fert_cost + rent_cost}")

        return total_costs

def all():
        revenue = additives()
        costs = negatives()
        final_all = revenue - costs
        print(f"Your total after your costs should come out to be around: ${final_all}")



if __name__ == '__main__':
        main()