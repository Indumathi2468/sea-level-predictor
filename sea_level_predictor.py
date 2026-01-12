import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os

def draw_plot():
  
    file_path = os.path.join(os.path.dirname(__file__), "epa-sea-level.csv")
    df = pd.read_csv(file_path)

   
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

   
    res_all = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = pd.Series(range(1880, 2051))
    plt.plot(years_all, res_all.slope * years_all + res_all.intercept)


    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = pd.Series(range(2000, 2051))
    plt.plot(years_recent, res_recent.slope * years_recent + res_recent.intercept)

    
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

  
    plt.savefig("sea_level_plot.png")

    return plt.gca()
