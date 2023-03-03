# Sea-Level-Predictor
certification python project from <a href="https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor" target="_blank" rel="noopener noreferrer">freecodecamp</a>


1. using Python to predict the sea level change through year 2050.
      <details>
      <summary><b>Prediction graphic</b></summary>
        <img src="https://github.com/mas-tono/Sea-Level-Predictor/blob/main/sea_level_plot.png">
      </details>
           
2. import libraries
      <details>
        <summary>import library</summary>
        <pre>
        import pandas as pd
        import matplotlib.pyplot as plt
        from scipy.stats import linregress
        </pre>
      </details>

3. matplotlib to create scatter plot for year and sea level from data available

      <details>
        <summary>scatter plot</summary>
        <pre>def draw_plot():
          # Read data from file
          df = pd.read_csv("epa-sea-level.csv")</br>
          # Create scatter plot
          plt.figure(figsize=(12,6))
          plt.scatter(data=df, 
                      x="Year", 
                      y="CSIRO Adjusted Sea Level")
        </pre>
      </details>

4. scipy.stats (linregress) to make a prediction (red line) of sea level to year 2050 based on available data
      <details>
        <summary>linregress</summary>
        <pre>
            m = linregress(x=df["Year"], 
            y=df["CSIRO Adjusted Sea Level"])
            trend = [m.slope * i + m.intercept for i in df["Year"]]
            df["trend"] = trend
            years_extended = [i for i in range(2014, 2051)]
            trend_2050 = [m.slope * i + m.intercept for i in years_extended]
            df_2050 = pd.DataFrame({"Year":years_extended, "trend":trend_2050})
            df_gabung = pd.concat([df, df_2050], ignore_index=True)
        </pre>
      </details>

      <details>
        <summary>scatter plot</summary>
        <pre>
            lt.figure(figsize=(12,6))
            plt.scatter(data=df, 
                        x="Year", 
                        y="CSIRO Adjusted Sea Level")
            plt.plot(df_gabung["Year"], df_gabung["trend"], color="red")
        </pre>
      </details>

5. scipy.stats (linregress) to make a prediction (black line) of sea level to year 2050 based on selected available data (year 2000 up)
      <details>
        <summary>linregress</summary>
        <pre>
            df_2000 = df[(df["Year"] >= 2000)]
            m_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
            df_2000_2050 = df_gabung[df_gabung["Year"] >= 2000].copy(deep=True)
            trend_2000_2050 = [m_2000.slope * i + m_2000.intercept for i in df_2000_2050["Year"]]
            df_2000_2050["trend_2000"] = trend_2000_2050            
        </pre>
      </details>

      <details>
        <summary>scatter plot</summary>
        <pre>
            plt.plot(df_2000_2050["Year"], df_2000_2050["trend_2000"], color="black")
        </pre>
      </details>

6. add labels and title
      <details>
        <summary>labels & titles</summary>
        <pre>
            plt.xlabel("Year")
            plt.ylabel("Sea Level (inches)")
            plt.title("Rise in Sea Level")            
            plt.savefig('sea_level_plot.png')
            return plt.gca()
        </pre>
      </details>

7. call via main.py
