import pandas as pd
import time

team = ["swallows", "tigers", "giants", "carp", "dragons", "baystars", "buffaloes", "marines", "eagles", "hawks", "fighters", "lions"]
team_url = ["s","t", "g", "c", "d", "yb", "bs", "m", "e", "h", "f", "l"]

for i in range(len(team)):
    url = f"https://baseball-data.com/21/stats/hitter-{team_url[i]}/"
    dfs = pd.read_html(url)
    df = dfs[0]
    print(df.head())
    df.to_csv(f"{team[i]}_hit.csv", index = False)
    time.sleep(3)




