"""
Uses gridstatus API to pull SPP nodal prices
"""

import gridstatus
import pandas as pd


locations = [
"WR.LEC.5",
"WR.JEC.1",
"KCPLIATANUNIAT1",
"KCPLLACYGNEUNLAC1",
"MPS.ROCKCREEK",
"SECI_CIMARRON",
"SECI.KCPS.SPEARVILLE"]

iso = gridstatus.SPP()

df_main=iso.get_lmp(date="2023-01-01",
    end = "2024-01-01", market="DAY_AHEAD_HOURLY")

df_main=df_main.loc[df_main['Location'].isin(locations)]

df_main.reset_index(drop=True)





df_main.drop(columns=["Interval Start", "Interval End",
    "Market", "Location Type", "PNode", "Energy",
    "Congestion", "Loss"], inplace=True)

df_main.reset_index(drop=True)
