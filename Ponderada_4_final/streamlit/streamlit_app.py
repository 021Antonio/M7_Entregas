from sqlalchemy import create_engine
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

conn = create_engine("postgresql://postgres:password@localhost:5432/postgres")
SQL_Query = pd.read_sql('SELECT * FROM public.data', conn)

# Set the title for the Streamlit app
st.title("Dashboard gráfico")
st.text('Riscos de ataque cardiaco por sexo')
df = pd.DataFrame(SQL_Query, columns=['gender', 'class'])

# Group the data by 'sex' and 'output' and calculate the count
grouped_data = SQL_Query.groupby(['gender', 'class']).size().unstack(fill_value=0)

# Create the Matplotlib bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Define custom colors
colors = ['#F94886', '#4896F9']

# Set the width of each bar
bar_width = 0.35

# Define x-axis positions for the bars
x = range(len(grouped_data.columns))

# Plot the bars for each 'sex' value (0 and 1)
for i, gender in enumerate(grouped_data.index):
    ax.bar(
        [pos + bar_width * i for pos in x], 
        grouped_data.loc[gender], 
        width=bar_width, 
        color=colors[i], 
        label=f'gender {gender}'
    )

ax.set_xlabel('class')
ax.set_ylabel('Count')
ax.set_title('Riscos de ataque cardiaco por sexo')
ax.set_xticks([pos + bar_width for pos in x])
ax.set_xticklabels(grouped_data.columns)
ax.legend()

# Display the Matplotlib chart in Streamlit
st.pyplot(fig)



