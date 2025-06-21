import pandas as pd

df = pd.read_json("C:\\Users\\Bogda\\OneDrive\\Documents\\KSE\\kse_pb\\kse_pb\\assigment_5\\Kyiv_next7days.json")

#DataFrame
hourly = []
for day in df['days']:
    day_date = day['datetime']
    for hour in day['hours']:
        hourly.append({
            'date': day_date,
            'time': hour['datetime'],
            'temp': hour['temp'],
            'windspeed': hour['windspeed']
        })

df = pd.DataFrame(hourly)
print(df)

#Next 3 days
df['date'] = pd.to_datetime(df['date'])
df_next3day = df[df['date'] < pd.Timestamp('2025-06-24')]
max_3days = df_next3day["temp"].max()
min_3days = df_next3day["temp"].min()
mean_3days = df_next3day["temp"].mean()

print(f"Max: {max_3days}, Min: {min_3days}, Mean: {mean_3days:.2f}")

#Wind
wind_mean  = df["windspeed"].mean()
wind_above = df[df["windspeed"] > wind_mean]
amount = len(wind_above)
print(f"{amount} hours")
