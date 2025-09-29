import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

#get the icc world cup data
iccdf=pd.read_csv('batting_stats_for_icc_mens_t20_world_cup_2024.csv')
print(iccdf.head())
#group by each team
iccaverageperteam=iccdf.groupby('Team').mean(numeric_only=True)
print(iccaverageperteam)
# Select the relevant columns
team_stats = iccaverageperteam[['Runs', 'Mat','SR']]

# Create the bar plot
team_stats.plot(kind='bar', figsize=(12, 6))
plt.title('Average Matches Played and Runs Scored per Team')
plt.xlabel('Team')
plt.ylabel('Average Count')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

top_players_per_team = iccdf.loc[iccdf.groupby('Team')['Runs'].idxmax()]

print("Player with the highest runs for each team:")
print(top_players_per_team[['Team', 'Player', 'Runs','50']])
