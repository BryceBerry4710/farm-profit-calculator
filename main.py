'''This is afarm profit calculator. (Later feature will ask for how many crops being farmed and how many of each.) Current version will ask for total corn and soybeans,
        '''
import sys
import requests
import time

def get_float(question):
        while True:
                try:
                        value = float(input(question))
                except ValueError:
                        print("That is not a valid number. Please try again.\n")
                else:
                        return value


def get_corn_prices():
        try:
                commodity = "corn"
                api_key = "ok_b3e433a540909825c95ba67b2b974681"
                response = requests.get("https://commodity-price-api.omkar.cloud/commodity-price",
                params={"name": commodity},
                headers={"API-Key": api_key}
                )
                data_corn = (response.json())
                price_corn = data_corn['price_usd']
                return price_corn

        except:
                print("Could not retrieve live corn price. Using default price.")
                return 5.25


def get_bean_prices():
        try:
                commodity = "soybean"
                api_key = "ok_b3e433a540909825c95ba67b2b974681"
                response = requests.get(
                "https://commodity-price-api.omkar.cloud/commodity-price",
                params={"name": commodity},
                headers={"API-Key": api_key}
                )
                data_beans = (response.json())
                price_beans = data_beans['price_usd']
                return price_beans
        except:
                print("Could not retrieve live bean price. Using default price.")
                return 11.50

def main():

        while True:
                pick = input("Hello! Welcome to the farm calculator. What would you like to configure today? " \
                             "OPTIONS: \nREV = Revenue Calculator," \
                             "\nCOSTS =Total Costs," \
                             " \nALL = Total revenue, minus total costs., " \
                             "\nQ = quit." \
                             "\nBE = find what you need prices to average based on costs.  ")
                if pick.upper() == ("REV"):
                        additives()
                elif pick.upper() ==("COSTS"):
                        negatives()
                elif pick.upper() ==("ALL"):
                        all()
                elif pick.upper() ==("CORN"):
                        get_corn_prices()
                elif pick.upper() ==("BEAN"):
                        get_bean_prices()
                elif pick.upper() ==("BE"):
                        break_even()
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
        time.sleep(0.5)
        print("Calculating...")
        time.sleep(1)
        #Finding comodity prices.
        price_corn = get_corn_prices()
        price_beans = get_bean_prices()
        print(f"Looks like corn is currently selling for ${price_corn},\n Looks like soybeans are current selling for ${price_beans}  ")
        time.sleep(1)
       

        #Final Print Statement.
        total_corn_plus = (bushels_corn * total_corn) * (price_corn)
        total_beans_plus = (bushels_beans * total_soybeans) * (price_beans)
        final_plus = total_beans_plus + total_corn_plus
        print("-----TOTAL:-----")
        time.sleep(2)
        print(f"In total, based on {price_corn} corn and {price_beans} beans, you're looking at:\n${total_corn_plus} roughly from corn,\n \
        and ${total_beans_plus} roughly from beans.")
        print(f"This totals out to be: {total_beans_plus + total_corn_plus} ")
        time.sleep(5)

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
        time.sleep(5)

        return total_costs

def break_even():
        costs = negatives()
        total_bushels = get_float("What is your expected total bushels?")
        
        break_even_price = round(costs / total_bushels, 2)

        print(f"You need at least ${break_even_price} to break even.")
        time.sleep(5)



def all():
        revenue = additives()
        costs = negatives()
        final_all = revenue - costs
        print(f"Your total after your costs should come out to be around: ${final_all}")
        time.sleep(5)


if __name__ == '__main__':
        main()