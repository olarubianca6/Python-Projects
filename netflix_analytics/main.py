import pandas as pd

df = pd.read_csv('reports/Gviewingactivity.csv')

df = df.drop(['Profile Name', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)

df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)

df = df.set_index('Start Time')
df.index = df.index.tz_convert('Europe/Bucharest')
df = df.reset_index()

df['Duration'] = pd.to_timedelta(df['Duration'])

print(df['Duration'].sum())
