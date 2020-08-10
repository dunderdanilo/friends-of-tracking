from FCPython import createPitch
from DunderFC import transform_coordinates
import pandas as pd
import matplotlib.pyplot as plt
import json

# Load Statsbomb event data for the match
match_id = 69301
with open(f'Statsbomb/data/events/{match_id}.json') as data_file:
    data = json.load(data_file)

df = pd.json_normalize(data, sep="_").assign(match_id=match_id)

# Select the passes from Sara
condition = (df['type_name'] == 'Pass') & (
    df['player_name'] == 'Sara Caroline Seger')
saras_passes = df[condition]

# Create the pitch
(fig, ax) = createPitch(120, 80, 'yards', 'gray')

# Plot the passes
for i, p in saras_passes.iterrows():
    x, y = p.location
    x, y = transform_coordinates(x, y)

    end_x, end_y = p.pass_end_location
    end_x, end_y = transform_coordinates(end_x, end_y)

    start_circle = plt.Circle((x, y), 1, alpha=.2, color="blue")
    pass_arrow = plt.Arrow(x, y, end_x - x, end_y - y, width=2, color="blue")
    ax.add_patch(pass_arrow)
    ax.add_patch(start_circle)

fig.set_size_inches(15, 10.5)
fig.savefig('saras-passess.pdf', dpi=100)
plt.show()
