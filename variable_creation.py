import pandas as pd
import numpy as np

from csv_import import yearly_data
from cat_map import *

rs_2018, rs_2019, rs_2021 = yearly_data()

def returing_cust():
    """
    Function to check if the AccountId was present the previous year.
    """
    rs_2018['AccountId'] = rs_2018['AccountId'].astype(str)
    rs_2019['AccountId'] = rs_2019['AccountId'].astype(str)
    rs_2021['AccountId'] = rs_2021['AccountId'].astype(str)
    bought_in2018 = rs_2018['AccountId'].to_list()
    bought_in2019 = rs_2019['AccountId'].to_list()

    rs_2019 = rs_2019['AccountId'].isin(bought_in2018)
    rs_2021 = rs_2021['AccountId'].isin(bought_in2019)
    return rs_2019, rs_2021

rs_2019,rs_2021 = returing_cust()

def map_categoricals(df):
    """Function to map categorial variables to the dataframe"""
    df['STH_Act'] = df['account_type'].map(SEASON_map)
    df['BUSINESS_STH_Act'] = df['account_type'].map(SEABUS_map)
    df['GROUP_Act'] = df['account_type'].map(GROUP_map)
    df['BUSINESS_act'] = df['account_type'].map(BUSINESS_map)
    df['Individual_Act'] = df['account_type'].map(IND_map)
    df['SPONSOR_Act'] = df['account_type'].map(SPONSOR_map)
    df['EMPLOYEE_Act'] = df['account_type'].map(EMPLOYEE_map)

    df['April'] = df['game_month'].map(April_map)
    df['May'] = df['game_month'].map(May_map)
    df['June'] = df['game_month'].map(June_map)
    df['July'] = df['game_month'].map(July_map)
    df['August'] = df['game_month'].map(August_map)
    df['September'] = df['game_month'].map(September_map)

    df['Thursday'] = df['game_day'].map(Thurs_map)
    df['Sunday'] = df['game_day'].map(Sun_map)
    df['Tuesday'] = df['game_day'].map(Tues_map)
    df['Wednesday'] = df['game_day'].map(Weds_map)
    df['Saturday'] = df['game_day'].map(Sat_map)
    df['Friday'] = df['game_day'].map(Fri_map)
    df['Monday'] = df['game_day'].map(Mon_map)

    df['low_scale_seat'] = df['price_scale_seat'].map(low_scale_seat_map)
    df['med_scale_seat'] = df['price_scale_seat'].map(med_scale_seat_map)
    df['high_scale_seat'] = df['price_scale_seat'].map(high_scale_seat_map)
    df = df.drop(columns = ['AccountId', 'TicketId', 'EventCd', 'Tickets', 'from_USA', 'RS_HomeTeam'])

    df['game_hour'] = df['game_hour'].astype(int)

    return df
