import pandas as pd


#  Load datasets

def load_data():

    tariffs = pd.read_csv("data/tariffs.csv")

    irradiance = pd.read_csv("data/solar_irradiance.csv")

    cost_data = pd.read_csv("data/solar_cost.csv")

    return tariffs, irradiance, cost_data


#  1. Electricity bill calculation (slab-based)

def calculate_electricity_bill(units, state, tariffs_df):

    state_tariffs = tariffs_df[tariffs_df['state'] == state]

    total_bill = 0

    previous_max = 0

    for _, row in state_tariffs.iterrows():

        slab_max = row['slab_max']

        rate = row['rate']

        if units > slab_max:

            units_in_slab = slab_max - previous_max
            
        else:    

            units_in_slab = max(0, units - previous_max)

        total_bill += units_in_slab * rate

        previous_max = slab_max

        if units <= slab_max:
            
            break

    return round(total_bill, 2)


#  2. Solar generation calculation

def calculate_solar_generation(system_size_kw, state, irradiance_df):

    sun_hours = irradiance_df[irradiance_df['state'] == state]['sun_hours'].values[0]

    # monthly generation

    generation = system_size_kw * sun_hours * 30

    return round(generation, 2)


#  3. Solar system cost

def calculate_system_cost(system_size_kw, cost_df):

    row = cost_df[cost_df['system_size_kw'] == system_size_kw].iloc[0]

    cost_per_kw = row['cost_per_kw']

    subsidy_percent = row['subsidy_percent']

    total_cost = system_size_kw * cost_per_kw

    subsidy_amount = total_cost * subsidy_percent

    final_cost = total_cost - subsidy_amount

    return round(final_cost, 2)


#  4. Bill after solar

def calculate_new_bill(units, solar_generation, state, tariffs_df):

    net_units = max(units - solar_generation, 0)

    return calculate_electricity_bill(net_units, state, tariffs_df)


#  5. Savings

def calculate_savings(old_bill, new_bill):

    monthly_savings = old_bill - new_bill

    yearly_savings = monthly_savings * 12

    return round(monthly_savings, 2), round(yearly_savings, 2)


#  6. Payback period

def calculate_payback(system_cost, yearly_savings):

    if yearly_savings == 0:

        return None

    return round(system_cost / yearly_savings, 2)
 
def recommend_system_size(monthly_units):

    if monthly_units <= 0:

        return 1

    recommended_size = monthly_units / 120

    # Round to nearest standard size

    if recommended_size <= 1:

        return 1

    elif recommended_size <= 2:

        return 2

    elif recommended_size <= 3:

        return 3

    elif recommended_size <= 5:

        return 5

    else:

        return 10
 