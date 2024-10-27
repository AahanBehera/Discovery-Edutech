import streamlit as st

EMISSION_FACTORS = {
    "India":{
        "Transportation": 0.14, #kgco2/km
        "Electricity": 0.82, #kgco2/kwh
        "Diet": 1.25, #kgco2/meal, 2.5 kgco2/kg
        "Waste": 0.1, #kgco2/kg
        }
    }

st.set_page_config(layout="wide", page_title = "Personal Carbon Calculator")

st.title("Personal Carbon Calculator App")

countries = ["India", "Pakistan", "Nepal", "Bhutan", "Bangladesh", "Sri Lanka", "The Maldives"]

#user inputs
st.subheader("🌎Your Country")
country = st.selectbox("Select", options = countries)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗Daily Commute Distance(in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡Monthly Electricity Consumption(in kwh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🗑Waste generated per week(in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍔Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

#normalize inputs
if distance > 0:
    distance = distance*365
if electricity > 0:
    electricity = electricity*12
if meals > 0:
    meals = meals*365
if waste > 0:
    waste = waste*52

#calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"]*distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"]*electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"]*meals
waste_emissions = EMISSION_FACTORS[country]["Waste"]*waste

transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

#rounding and conversion
total_emissions = round(
    transportation_emissions+electricity_emissions+diet_emissions+waste_emissions, 2
)

if st.button("Calculate CO2 Emissions"):
    #result
    st.header("Results")
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Carbon Emissions by Categories")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🗑 Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🍔 Waste: {waste_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.info(f"🌎 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning("Per capita carbon dioxide (CO₂) emissions in India have soared in recent decades, climbing from roughly 0.4 metric tons in 1970 to a high of 2.07 metric tons in 2023. This was an increase of 6.7 percent in comparison to 2022 levels. Total CO₂ emissions in India also reached a record high in 2023.")
    col5,col6 = st.columns(2)
    with col5:
        st.image("/Users/manasbehera/Downloads/image.png", caption="Carbon Footprint")
    with col6:
        st.image("/Users/manasbehera/Downloads/Planet.jpg", caption="Earth,The Blue Planet")



    

    
    

                       
