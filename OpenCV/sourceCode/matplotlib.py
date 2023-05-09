import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame of temperature data
data = {'Year': [2010, 2011, 2012, 2013, 2014],
        'Temperature': [72, 75, 78, 80, 82]}

df = pd.DataFrame(data)

# Create a line graph of temperature over time
plt.plot(df['Year'], df['Temperature'])

# Add labels to the x-axis and y-axis
plt.xlabel('Year')
plt.ylabel('Temperature')

# Add a title to the graph
plt.title('Temperature Over Time')

# Display the graph
plt.show()
