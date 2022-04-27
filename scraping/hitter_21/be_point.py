import pandas as pd

team = ["swallows", "tigers", "giants", "carp", "dragons", "baystars", "buffaloes", "marines", "eagles", "hawks", "fighters", "lions"]
list_df = []

for i in range(len(team)):
    df = pd.read_csv(f"{team[i]}_hit.csv")
    df1 = df.drop(0, axis = 0)
    list_df.append(df1)

li_ = []

for i in range(len(list_df)):
    null = []
    for j in range(len(list_df[i])):
        x = list_df[i]
        if x['打率'][j].empty:
            null.append([j])
        if j == len(x):
            df2 = x.drop(null, axis = 0)
            li_.append(df2)

print(li_)
