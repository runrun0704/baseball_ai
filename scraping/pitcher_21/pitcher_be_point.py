import pandas as pd

teams = ["swallows", "tigers", "giants", "carp", "dragons", "baystars", "buffaloes", "marines", "eagles", "hawks", "fighters", "lions"]

team_df = []
for i in range(len(teams)):
    df = pd.read_csv(f"{teams[i]}_pitch.csv")
    df1 = df.drop(0, axis = 0)
    team_df.append(df1)

dropped_df = []
for i in range(12):
    null = []
    for j in range(1,len(team_df[i])+1):
        x = team_df[i]
        if x.loc[j, '防御率'] == '-':
            null.append(j)
        else:
            pass
        if j == len(x):
            df2 = x.drop(null, axis = 0)
            dropped_df.append(df2)

to_int_df = []

for i in range(len(teams)):
    x = dropped_df[i]
    x[['防御率','試合','勝利','敗北','セlブ','ホlルド','勝率','打者','投球回','被安打','被本塁打','与四球','与死球','奪三振','失点','自責点','WHIP','DIPS']] = x[['防御率','試合','勝利','敗北','セlブ','ホlルド','勝率','打者','投球回','被安打','被本塁打','与四球','与死球','奪三振','失点','自責点','WHIP','DIPS']].astype(float)
    to_int_df.append(x)

over_49_df = []
for i in range(len(teams)):
    x = to_int_df[i]
    y = x[x['投球回']>9.2]
    over_49_df.append(y)

def defense(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['防御率'].loc[i]
        if y <= 1.50:
            li_.append(10)
        elif y <= 1.75:
            li_.append(9)
        elif y <= 2.0:
            li_.append(8)    
        elif y <= 2.5:
            li_.append(7)    
        elif y <= 3.0:
            li_.append(6)    
        elif y <= 3.5:
            li_.append(5)    
        elif y <= 4.0:
            li_.append(4)    
        elif y <= 4.5:
            li_.append(3)    
        elif y <= 5.0:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def game(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['試合'].loc[i]
        if y >= 60:
            li_.append(10)
        elif y >= 50:
            li_.append(9)
        elif y >= 45:
            li_.append(8)    
        elif y >= 30:
            li_.append(7)    
        elif y >= 25:
            li_.append(6)    
        elif y >= 20:
            li_.append(5)    
        elif y >= 15:
            li_.append(4)    
        elif y >= 10:
            li_.append(3)    
        elif y >= 5:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def win(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['勝利'].loc[i]
        if y >= 18:
            li_.append(10)
        elif y >= 15:
            li_.append(9)
        elif y >= 12:
            li_.append(8)    
        elif y >= 10:
            li_.append(7)    
        elif y >= 8:
            li_.append(6)    
        elif y >= 6:
            li_.append(5)    
        elif y >= 4:
            li_.append(4)    
        elif y >= 2:
            li_.append(3)    
        elif y >= 1:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def lose(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['敗北'].loc[i]
        if y <= 0:
            li_.append(10)
        elif y <= 1:
            li_.append(9)
        elif y <= 2:
            li_.append(8)    
        elif y <= 4:
            li_.append(7)    
        elif y <= 5:
            li_.append(6)    
        elif y <= 6:
            li_.append(5)    
        elif y <= 7:
            li_.append(4)    
        elif y <= 8:
            li_.append(3)    
        elif y <= 9:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def save(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['セlブ'].loc[i]
        if y >= 40:
            li_.append(10)
        elif y >= 35:
            li_.append(9)
        elif y >= 30:
            li_.append(8)    
        elif y >= 25:
            li_.append(7)    
        elif y >= 20:
            li_.append(6)    
        elif y >= 15:
            li_.append(5)    
        elif y >= 10:
            li_.append(4)    
        elif y >= 7:
            li_.append(3)    
        elif y >= 5:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def hold(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['ホlルド'].loc[i]
        if y >= 50:
            li_.append(10)
        elif y >= 40:
            li_.append(9)
        elif y >= 35:
            li_.append(8)    
        elif y >= 30:
            li_.append(7)    
        elif y >= 25:
            li_.append(6)    
        elif y >= 15:
            li_.append(5)    
        elif y >= 10:
            li_.append(4)    
        elif y >= 5:
            li_.append(3)    
        elif y >= 3:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def win_par(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['勝率'].loc[i]
        if y >= 0.700:
            li_.append(10)
        elif y >= 0.650:
            li_.append(9)
        elif y >= 0.600:
            li_.append(8)    
        elif y >= 0.575:
            li_.append(7)    
        elif y >= 0.550:
            li_.append(6)    
        elif y >= 0.525:
            li_.append(5)    
        elif y >= 0.500:
            li_.append(4)    
        elif y >= 0.475:
            li_.append(3)    
        elif y >= 0.450:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def for_hitter(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['打者'].loc[i]
        if y >= 650:
            li_.append(10)
        elif y >= 500:
            li_.append(9)
        elif y >= 400:
            li_.append(8)    
        elif y >= 350:
            li_.append(7)    
        elif y >= 300:
            li_.append(6)    
        elif y >= 250:
            li_.append(5)    
        elif y >= 200:
            li_.append(4)    
        elif y >= 100:
            li_.append(3)    
        elif y >= 50:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def be_hitted(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['被安打'].loc[i]
        if y <= 30:
            li_.append(10)
        elif y <= 90:
            li_.append(9)
        elif y <= 120:
            li_.append(8)    
        elif y <= 140:
            li_.append(7)    
        elif y >= 150:
            li_.append(6)    
        elif y <= 160:
            li_.append(5)    
        elif y <= 180:
            li_.append(4)    
        elif y <= 200:
            li_.append(3)    
        elif y <= 210:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def be_homerun(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['被本塁打'].loc[i]
        if y <= 0:
            li_.append(10)
        elif y <= 1:
            li_.append(9)
        elif y <= 2:
            li_.append(8)    
        elif y <= 3:
            li_.append(7)    
        elif y <= 4:
            li_.append(6)    
        elif y <= 5:
            li_.append(5)    
        elif y <= 6:
            li_.append(4)    
        elif y <= 7:
            li_.append(3)    
        elif y <= 8:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def take_four(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['与四球'].loc[i]
        if y >= 10:
            li_.append(10)
        elif y >= 15:
            li_.append(9)
        elif y >= 20:
            li_.append(8)    
        elif y >= 25:
            li_.append(7)    
        elif y >= 30:
            li_.append(6)    
        elif y >= 35:
            li_.append(5)    
        elif y >= 40:
            li_.append(4)    
        elif y >= 45:
            li_.append(3)    
        elif y >= 50:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def take_dead(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['与死球'].loc[i]
        if y <= 0:
            li_.append(10)
        elif y <= 1:
            li_.append(9)
        elif y <= 2:
            li_.append(8)    
        elif y <= 3:
            li_.append(7)    
        elif y <= 4:
            li_.append(6)    
        elif y <= 5:
            li_.append(5)    
        elif y <= 6:
            li_.append(4)    
        elif y <= 7:
            li_.append(3)    
        elif y <= 8:
            li_.append(2)   
        else:
            li_.append(1)
    return li_  

def struck_out(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['奪三振'].loc[i]
        if y >= 200:
            li_.append(10)
        elif y >= 180:
            li_.append(9)
        elif y >= 160:
            li_.append(8)    
        elif y >= 140:
            li_.append(7)    
        elif y >= 120:
            li_.append(6)    
        elif y >= 100:
            li_.append(5)    
        elif y >= 80:
            li_.append(4)    
        elif y >= 60:
            li_.append(3)    
        elif y >= 40:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def conceded(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['失点'].loc[i]
        if y <= 0:
            li_.append(10)
        elif y <= 15:
            li_.append(9)
        elif y <= 20:
            li_.append(8)    
        elif y <= 30:
            li_.append(7)    
        elif y <= 40:
            li_.append(6)    
        elif y <= 50:
            li_.append(5)    
        elif y <= 55:
            li_.append(4)    
        elif y <= 60:
            li_.append(3)    
        elif y <= 70:
            li_.append(2)   
        else:
            li_.append(1)
    return li_  

def mine_conceded(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['自責点'].loc[i]
        if y <= 0:
            li_.append(10)
        elif y <= 10:
            li_.append(9)
        elif y <= 15:
            li_.append(8)    
        elif y <= 20:
            li_.append(7)    
        elif y <= 25:
            li_.append(6)    
        elif y <= 30:
            li_.append(5)    
        elif y <= 35:
            li_.append(4)    
        elif y <= 40:
            li_.append(3)    
        elif y <= 50:
            li_.append(2)   
        else:
            li_.append(1)
    return li_        

def whip(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['WHIP'].loc[i]
        if y <= 1.0:
            li_.append(10)
        elif y <= 1.09:
            li_.append(9)
        elif y <= 1.19:
            li_.append(8)    
        elif y <= 1.29:
            li_.append(7)    
        elif y <= 1.35:
            li_.append(6)    
        elif y <= 1.39:
            li_.append(5)    
        elif y <= 1.45:
            li_.append(4)    
        elif y <= 1.49:
            li_.append(3)    
        elif y <= 1.55:
            li_.append(2)   
        else:
            li_.append(1)
    return li_  

def name(x):
    point_df = pd.DataFrame(x['選手名'])
    return point_df

def main(df, team_name):
    point_df = name(df)
    
    #以下関数の呼び出し,ポイント化したデータフレームをポイントテーブルに挿入
    defense_ = defense(df)
    point_df['DEFENSE'] = defense_
    
    game_ = game(df)
    point_df['GAME'] = game_
    
    win_ = win(df)
    point_df['WIN'] = win_
    
    lose_ = lose(df)
    point_df['LOSE'] = lose_
    
    save_ = save(df)
    point_df['SAVE'] = save_
    
    hold_ = hold(df)
    point_df['HOLD'] = hold_
    
    win_par_ = win_par(df)
    point_df['WIN_PAR'] = win_par_
    
    be_hitted_ = be_hitted(df)
    point_df['BE_HITTED'] = be_hitted_
    
    be_homerun_ = be_homerun(df)
    point_df['BE_HOMERUN'] = be_homerun_

    take_four_ = take_four(df)
    point_df['TAKE_FOUR'] = take_four_
    
    take_dead_ = take_dead(df)
    point_df['TAKE_DEAD'] = take_dead_
    
    struck_out_ = struck_out(df)
    point_df['STRUCK_OUT'] = struck_out_
    
    conceded_ = conceded(df)
    point_df['CONCEDED'] = conceded_
    
    mine_conceded_ = mine_conceded(df)
    point_df['MINE_CONCEDED'] = mine_conceded_

    whip_ = whip(df)
    point_df['WHIP'] = whip_
    
    point_df.to_csv(f"point_pitch_{team_name}.csv")

for i in range(len(teams)):
    main(over_49_df[i], teams[i])