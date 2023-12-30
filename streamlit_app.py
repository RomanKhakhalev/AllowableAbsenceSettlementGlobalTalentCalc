import streamlit as st, pandas as pd
import datetime
from pandas.tseries.offsets import Day

st.set_page_config(
    page_title="Allowable absence constraints calculator (UK Global Talent/Tier 1)",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded")

#st.session_state.now_date_selecion = False
# Sidebar
with st.sidebar:
    st.header('Please, enter the initial parameters')
    trips_file = st.file_uploader('Upload CSV file with outbound trips', type = ['csv'])
    visa_date = st.date_input ('Date of entry clearance (visa issue)', value = datetime.date(2022,1,1))
    enter_date = st.date_input ('Date of first arrival to the UK?', value = datetime.date(2022,1,1))
    st.session_state.now_date_toggle = st.toggle("Predictor mode", value = False)
    now_date = st.date_input ('What date to use as the baseline (today is default value)?', value = datetime.datetime.now().date(), disabled = not st.session_state.now_date_toggle)
    now_date = pd.Timestamp(now_date) 
        

#######################
# Dashboard Main Panel




if visa_date and enter_date and trips_file:
    trips_csv = pd.read_csv(trips_file, parse_dates = [0,1], header = None)
    inner_ds = pd.Series(index = pd.date_range(start = visa_date, end = enter_date, freq = 'D', inclusive = 'left')).fillna(1)
    for row in trips_csv.values:
        inner_ds = pd.concat([inner_ds,pd.Series(index = pd.date_range(start = row[0], end = row[1], freq = 'D', inclusive = 'left')).fillna(1)])
    if inner_ds.index[-1] < now_date:
        inner_ds[now_date] = 0
    st.markdown(f'***Days outside of the UK since visa date in total: {inner_ds.sum().astype(int)}***')
    
    absent_df = pd.DataFrame([[visa_date, enter_date,'Before arrival']])
    absent_df = pd.concat([absent_df, trips_csv], ignore_index = True)
    absent_df.columns = ['Departure', 'Arrival', 'Destination']
    absent_df['Absent midnights'] = absent_df[['Departure','Arrival']].apply(lambda x:inner_ds[x.values[0]:x.values[1]].sum(),axis = 1)
    show_absent_df =  st.toggle('Show the table with trips.', True)
    if show_absent_df:
        st.dataframe(absent_df)

    tabs = st.tabs(['ILR','Passport'])
    with tabs[0]:
        df_ilr = inner_ds.resample("D").asfreq().fillna(0).rolling(360, min_periods = 1).sum()
        on =  st.toggle("Show the 180-days rolling window graph")
        if on:
            st.line_chart(df_ilr)
        
        if df_ilr[df_ilr > 180].any():
            visa_date = enter_date = df_ilr[df_ilr > 180].last_valid_index().date()
            st.markdown(f":red[*As you have exceed initial allowance for absence, the calculation will restart from {visa_date}*] ")
        else:
            st.markdown(f":green[*You have not exceed the allowance on number of days outside UK*")

        ilr_availability_date = visa_date + datetime.timedelta(days = 365 * 3 - 28)
        with st.container(border = True):
            if now_date < pd.Timestamp(ilr_availability_date):
                st.subheader(f"The availability date for the ILR application is: {ilr_availability_date}")
                st.subheader (f"For today, the number of days of allowance remaining is: {180-df_ilr[-1].astype(int)}")
            else:
                st.subheader("Congratulations! You are eligible to apply for ILR.")
            

    with tabs[1]:   
            passport_availability_date = visa_date + datetime.timedelta(days = 365 * 5)
            if temp := ilr_availability_date + datetime.timedelta(days = 365 * 1) > passport_availability_date:
                passport_availability_date = temp
            ninety_days_constraint_startdate = inner_ds.last_valid_index() - datetime.timedelta(days = 90)
            if (inner_ds[ninety_days_constraint_startdate:] > 0).any():
                ninety_days_constraint_enddate = inner_ds[ninety_days_constraint_startdate:].last_valid_index() + datetime.timedelta(days = 90)
                if passport_availability_date < ninety_days_constraint_startdate:
                    passport_availability_date = ninety_days_constraint_startdate 
            with st.container(border = True):
                if now_date < pd.Timestamp(passport_availability_date):
                    st.subheader(f"The availability date for the passport application is: {passport_availability_date}.")
                    st.subheader (f"For today, the number of days of allowance remaining is: {450 - inner_ds[visa_date:].sum().astype(int)}.")
                    st.markdown (f"*:green[You have to return back to the UK before: {passport_availability_date - datetime.timedelta(days = 90)} (excluding ILR constraints).]*")
                else:
                    st.subheader("Congratulations! You are eligible for naturalization application.")
                
#######################
# Help file for the start screen
else:
    with open('UK_settlement_calculator.md') as file:
        st.markdown(file.read())
