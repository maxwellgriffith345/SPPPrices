"""
Uses gridstatus API to pull SPP nodal prices
"""

import gridstatus
import pandas as pd
import os


""" Set Paths For Exporting Data """
#how much path checking to do?
#Get path to current dir /src
current_dir = os.getcwd()

#get path to main project path
main_dir = os.path.dirname(current_dir)

#create path to data folder
data_path = os.path.join(current_dir, "data")


""" Pull Data From Grid Status """

locations = [
"WR.LEC.5",
"WR.JEC.1",
"KCPLIATANUNIAT1",
"KCPLLACYGNEUNLAC1",
"MPS.ROCKCREEK",
"SECI_CIMARRON",
"SECI.KCPS.SPEARVILLE"]

iso = gridstatus.SPP()

# Wrap in a try except? sometimes years aren't available
# don't wan tht escript to crash

df_main = iso.get_lmp_day_ahead_hourly(date="2024-01-01", end = "2024-01-02",
    location_type =  "Hub")


df_main=df_main.loc[df_main['Location'].isin(locations)]

df_main.reset_index(drop=True)





df_main.drop(columns=["Interval Start", "Interval End",
    "Market", "Location Type", "PNode", "Energy",
    "Congestion", "Loss"], inplace=True)

df_main.reset_index(drop=True)
