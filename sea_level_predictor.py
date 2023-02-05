import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.figure(figsize=(12,6))
    plt.scatter(data=df, 
                x="Year", 
                y="CSIRO Adjusted Sea Level")



    # Create first line of best fit
    m = linregress(x=df["Year"], 
            y=df["CSIRO Adjusted Sea Level"])

    m

    trend = [m.slope * i + m.intercept for i in df["Year"]]

    df["trend"] = trend

    years_extended = [i for i in range(2014, 2051)]
    trend_2050 = [m.slope * i + m.intercept for i in years_extended]
    df_2050 = pd.DataFrame({"Year":years_extended, "trend":trend_2050})

    df_gabung = pd.concat([df, df_2050], ignore_index=True)



    plt.figure(figsize=(12,6))
    plt.scatter(data=df, 
                x="Year", 
                y="CSIRO Adjusted Sea Level")
    plt.plot(df_gabung["Year"], df_gabung["trend"], color="red")   



    # plt.show()


    # Create second line of best fit
    
    df_2000 = df[(df["Year"] >= 2000)]

    m_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    
    df_2000_2050 = df_gabung[df_gabung["Year"] >= 2000].copy(deep=True)

    trend_2000_2050 = [m_2000.slope * i + m_2000.intercept for i in df_2000_2050["Year"]]

    df_2000_2050["trend_2000"] = trend_2000_2050

    plt.plot(df_2000_2050["Year"], df_2000_2050["trend_2000"], color="black")
    
    


    # Add labels and title

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()