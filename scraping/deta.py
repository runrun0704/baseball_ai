import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
import chromedriver_binary
import time

browser = webdriver.Chrome()

team = ["ヤクルト", "阪神", "巨人", "広島", "中日", "DeNA", "オリックス", "ロッテ", "楽天", "ソフトバンク", "日本ハム", "西武"]
team_url = ["s","t", "g", "c", "d", "yb", "bs", "m", "e", "h", "f", "l"]

for i in range(len(team)):
    elem_btn = browser.findElement(by.linkText(team[i]))
    elem_btn.click()
    url = f"https://baseball-data.com/stats/hitter-{team_url[i]}/tpa-1.html"
    dfs = pd.read_html(url)
    df = dfs[0]
    print(df.head())
    df.to_csv(f"{team[i]}_hit.csv", index = False)
    sleep(3)




