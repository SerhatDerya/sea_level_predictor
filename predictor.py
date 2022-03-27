import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# read data from file
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    # define x and y axis of the plot
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    res = linregress(x, y)
    
    #creating the plot
    plt.scatter(x, y)
    plt.plot(range(x[0],2051), res.intercept + res.slope*range(x[0],2051), "r")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.savefig("sea_level_plot.png")