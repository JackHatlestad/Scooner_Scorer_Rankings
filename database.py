import pandas as pd
import instaloader 
import re
import csv 

L = instaloader.Instaloader()


profile = instaloader.Profile.from_username(L.context, "schoonerscorer")

with open("schooner_data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Beer", "Score", "Caption"])

for post in profile.get_posts():
        caption = post.caption or ""
        date = post.date_utc.strftime("%Y-%m-%d")
        beer_match = re.search(r'🍺\s*(.*?)\s*(📍|$)', caption)
        beer = beer_match.group(1).strip() if beer_match else None
        pin_match = re.search(r'📍\s*(.*)', caption)
        location = pin_match.group(1).strip() if pin_match else None

        writer.writerow([date, beer, location])

