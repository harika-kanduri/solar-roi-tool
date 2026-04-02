import streamlit as st
from utils.calculations import *

# Load data
tariffs, irradiance, cost_data = load_data()
st.set_page_config(page_title="Solar ROI Calculator", layout="wide")

#  Title
st.title(" Solar ROI Calculator")
st.markdown("###  For Indian Households")
st.markdown("Estimate electricity bill, system size and long term savings based on your usage.")

# Info Section
st.markdown("## How it works")
st.write("""
1. Enter your monthly electricity usage
2. We estimate your bill based on state tariff 
3. Calculate required solar system size  
4. Show long-term savings 
""")

# Assumptions
st.markdown("### Assumptions")
st.write("""
- Tariff based on average Indian rates  
- 1 kW solar sytem generates ~120 units/month  
""")

#  Sidebar Inputs
with st.sidebar:
    st.header(" Input Parameters")
    state = st.sidebar.selectbox("Select State", tariffs['state'].unique())
    units = st.sidebar.number_input("Monthly Consumption (kWh)", min_value=0, value=400)

# Auto recommendation
recommended_size = recommend_system_size(units)
st.sidebar.info(f" Recommended System Size: {recommended_size} kW")

# User can still override
system_size = st.sidebar.selectbox(
   "Select Solar System Size (kW)",
   cost_data['system_size_kw'],
   index=list(cost_data['system_size_kw']).index(recommended_size)
)

#  Calculate button
if st.sidebar.button("Calculate"):
   # Calculations
   old_bill = calculate_electricity_bill(units, state, tariffs)
   solar_gen = calculate_solar_generation(system_size, state, irradiance)
   new_bill = calculate_new_bill(units, solar_gen, state, tariffs)
   monthly_savings, yearly_savings = calculate_savings(old_bill, new_bill)
   system_cost = calculate_system_cost(system_size, cost_data)
   payback = calculate_payback(system_cost, yearly_savings)
   if monthly_savings > 0:
        st.success(f" You can save approximately ₹{monthly_savings}/month by installing solar!")
   else:
        st.warning(" Solar may not be beneficial for your current usage.")

   #  Display Results
   st.markdown("###  Key Metrics")
   col1, col2, col3 = st.columns(3)
   with col1:
       col1.metric(" Before Solar", f"₹{old_bill}")
   with col2:
       col2.metric(" After Solar", f"₹{new_bill}")
   with col3:
       col3.metric(" Monthly Savings", f"₹{monthly_savings}")
   col4, col5, col6 = st.columns(3)
   col4.metric(" Yearly Savings", f"₹{yearly_savings}")
   col5.metric(" System Cost", f"₹{system_cost}")
   col6.metric(" Payback", f"{payback} yrs" if payback else "N/A")

   #  Simple Chart
   tab1, tab2 = st.tabs([" Analysis", " Projections"])
   with tab1:
      st.markdown("###  Cost Comparison")
      st.bar_chart({
       "Before Solar": old_bill,
       "After Solar": new_bill
   })
   with tab2:
      st.markdown("### Savings Over Time")
      years = list(range(1, 21))
      savings_projection = [yearly_savings * y for y in years]
      df = pd.DataFrame({
          "Year": years,
          "Savings": savings_projection
      })
      st.line_chart(df.set_index("Year"))
      st.caption("Projected cumulative savings over 20 years.")

   # CO2 Savings
   CO2_saved = solar_gen * 0.82 # kg CO2 per kWh approx
   st.markdown("### Environmental Impact")
   st.success(f"CO2 Saved:  **{CO2_saved:.1f} (kg/month)**") 
 
# Footer
st.markdown("___")
st.markdown(
    "<center>Built by <b>Harika Kanduri</b> | Python | Data Analytics | Solar Domain</center>",
   unsafe_allow_html=True)