import pandas as pd

teams = ["swallows", "tigers", "giants", "carp", "dragons", "baystars", "buffaloes", "marines", "eagles", "hawks", "fighters", "lions"]

team_df = []
for i in range(len(teams)):
    df = pd.read_csv(f"{teams[i]}_hit.csv")
    df1 = df.drop(0, axis = 0)
    team_df.append(df1)

dropped_df = []
for i in range(12):
    null = []
    for j in range(1,len(team_df[i])+1):
        x = team_df[i]
        if x.loc[j, '打率'] == '-':
            null.append(j)
        else:
            pass
        if j == len(x):
            df2 = x.drop(null, axis = 0)
            dropped_df.append(df2)

to_int_df = []

for i in range(len(teams)):
    x = dropped_df[i]
    x[['打率', '試合','打席数','打数','安打','本塁打','打点','盗塁','四球','死球','三振','犠打','併殺打','出塁率','長打率','OPS','RC27','XR27']] = x[['打率', '試合','打席数','打数','安打','本塁打','打点','盗塁','四球','死球','三振','犠打','併殺打','出塁率','長打率','OPS','RC27','XR27']].astype(float)
    to_int_df.append(x)

over_49_df = []
for i in range(len(teams)):
    x = to_int_df[i]
    y = x[x['打席数']>49.0]
    over_49_df.append(y)

def ave(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['打率'].loc[i]
        if y >= 0.350:
            li_.append(10)
        elif y >= 0.325:
            li_.append(9)
        elif y >= 0.310:
            li_.append(8)    
        elif y >= 0.300:
            li_.append(7)    
        elif y >= 0.290:
            li_.append(6)    
        elif y >= 0.280:
            li_.append(5)    
        elif y >= 0.270:
            li_.append(4)    
        elif y >= 0.260:
            li_.append(3)    
        elif y >= 0.250:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def game(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['試合'].loc[i]
        if y >= 143:
            li_.append(10)
        elif y >= 135:
            li_.append(9)
        elif y >= 120:
            li_.append(8)    
        elif y >= 110:
            li_.append(7)    
        elif y >= 100:
            li_.append(6)    
        elif y >= 80:
            li_.append(5)    
        elif y >= 60:
            li_.append(4)    
        elif y >= 40:
            li_.append(3)    
        elif y >= 20:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def stand(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['打席数'].loc[i]
        if y >= 600:
            li_.append(10)
        elif y >= 500:
            li_.append(9)
        elif y >= 400:
            li_.append(8)    
        elif y >= 300:
            li_.append(7)    
        elif y >= 250:
            li_.append(6)    
        elif y >= 200:
            li_.append(5)    
        elif y >= 150:
            li_.append(4)    
        elif y >= 100:
            li_.append(3)    
        elif y >= 50:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def hit_stand(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['打数'].loc[i]
        if y >= 500:
            li_.append(10)
        elif y >= 400:
            li_.append(9)
        elif y >= 350:
            li_.append(8)    
        elif y >= 300:
            li_.append(7)    
        elif y >= 250:
            li_.append(6)    
        elif y >= 200:
            li_.append(5)    
        elif y >= 150:
            li_.append(4)    
        elif y >= 100:
            li_.append(3)    
        elif y >= 50:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def hit(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['安打'].loc[i]
        if y >= 180:
            li_.append(10)
        elif y >= 170:
            li_.append(9)
        elif y >= 150:
            li_.append(8)    
        elif y >= 130:
            li_.append(7)    
        elif y >= 110:
            li_.append(6)    
        elif y >= 100:
            li_.append(5)    
        elif y >= 90:
            li_.append(4)    
        elif y >= 70:
            li_.append(3)    
        elif y >= 50:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def homerun(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['本塁打'].loc[i]
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

def hit_point(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['打点'].loc[i]
        if y >= 100:
            li_.append(10)
        elif y >= 90:
            li_.append(9)
        elif y >= 80:
            li_.append(8)    
        elif y >= 70:
            li_.append(7)    
        elif y >= 60:
            li_.append(6)    
        elif y >= 50:
            li_.append(5)    
        elif y >= 40:
            li_.append(4)    
        elif y >= 30:
            li_.append(3)    
        elif y >= 20:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def steel(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['盗塁'].loc[i]
        if y >= 50:
            li_.append(10)
        elif y >= 40:
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

def four_ball(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['四球'].loc[i]
        if y >= 100:
            li_.append(10)
        elif y >= 90:
            li_.append(9)
        elif y >= 80:
            li_.append(8)    
        elif y >= 70:
            li_.append(7)    
        elif y >= 60:
            li_.append(6)    
        elif y >= 50:
            li_.append(5)    
        elif y >= 40:
            li_.append(4)    
        elif y >= 30:
            li_.append(3)    
        elif y >= 20:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def dead_ball(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['死球'].loc[i]
        if y >= 15:
            li_.append(10)
        elif y >= 10:
            li_.append(9)
        elif y >= 8:
            li_.append(8)    
        elif y >= 7:
            li_.append(7)    
        elif y >= 6:
            li_.append(6)    
        elif y >= 5:
            li_.append(5)    
        elif y >= 4:
            li_.append(4)    
        elif y >= 3:
            li_.append(3)    
        elif y >= 2:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def struck_out(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['三振'].loc[i]
        if y <= 15:
            li_.append(10)
        elif y <= 30:
            li_.append(9)
        elif y <= 45:
            li_.append(8)    
        elif y <= 60:
            li_.append(7)    
        elif y <= 80:
            li_.append(6)    
        elif y <= 90:
            li_.append(5)    
        elif y <= 100:
            li_.append(4)    
        elif y <= 120:
            li_.append(3)    
        elif y <= 150:
            li_.append(2)   
        else:
            li_.append(1)
    return li_

def bant(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['犠打'].loc[i]
        if y >= 30:
            li_.append(10)
        elif y >= 25:
            li_.append(9)
        elif y >= 20:
            li_.append(8)    
        elif y >= 15:
            li_.append(7)    
        elif y >= 10:
            li_.append(6)    
        elif y >= 8:
            li_.append(5)    
        elif y >= 6:
            li_.append(4)    
        elif y >= 4:
            li_.append(3)    
        elif y >= 2:
            li_.append(2)   
        else:
            li_.append(1)
    return li_  

def dubble_play(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['併殺打'].loc[i]
        if y <= 3:
            li_.append(10)
        elif y <= 5:
            li_.append(9)
        elif y <= 7:
            li_.append(8)    
        elif y <= 10:
            li_.append(7)    
        elif y <= 12:
            li_.append(6)    
        elif y <= 15:
            li_.append(5)    
        elif y <= 17:
            li_.append(4)    
        elif y <= 20:
            li_.append(3)    
        elif y <= 25:
            li_.append(2)   
        else:
            li_.append(1)
    return li_ 

def survived(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['出塁率'].loc[i]
        if y >= 0.400:
            li_.append(10)
        elif y >= 0.375:
            li_.append(9)
        elif y >= 0.350:
            li_.append(8)    
        elif y >= 0.325:
            li_.append(7)    
        elif y >= 0.300:
            li_.append(6)    
        elif y >= 0.275:
            li_.append(5)    
        elif y >= 0.250:
            li_.append(4)    
        elif y >= 0.225:
            li_.append(3)    
        elif y >= 0.200:
            li_.append(2)   
        else:
            li_.append(1)
    return li_  

def long_hit(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['長打率'].loc[i]
        if y >= 0.600:
            li_.append(10)
        elif y >= 0.550:
            li_.append(9)
        elif y >= 0.500:
            li_.append(8)    
        elif y >= 0.450:
            li_.append(7)    
        elif y >= 0.400:
            li_.append(6)    
        elif y >= 0.350:
            li_.append(5)    
        elif y >= 0.300:
            li_.append(4)    
        elif y >= 0.250:
            li_.append(3)    
        elif y >= 0.200:
            li_.append(2)   
        else:
            li_.append(1)
    return li_        

def ops(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['OPS'].loc[i]
        if y >= 0.950:
            li_.append(10)
        elif y >= 0.900:
            li_.append(9)
        elif y >= 0.850:
            li_.append(8)    
        elif y >= 0.800:
            li_.append(7)    
        elif y >= 0.750:
            li_.append(6)    
        elif y >= 0.700:
            li_.append(5)    
        elif y >= 0.650:
            li_.append(4)    
        elif y >= 0.600:
            li_.append(3)    
        elif y >= 0.550:
            li_.append(2)   
        else:
            li_.append(1)
    return li_  

def rc27(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['RC27'].loc[i]
        if y >= 10:
            li_.append(10)
        elif y >= 9:
            li_.append(9)
        elif y >= 8:
            li_.append(8)    
        elif y >= 7:
            li_.append(7)    
        elif y >= 6:
            li_.append(6)    
        elif y >= 5:
            li_.append(5)    
        elif y >= 4:
            li_.append(4)    
        elif y >= 3:
            li_.append(3)    
        elif y >= 2:
            li_.append(2)   
        else:
            li_.append(1)
    return li_        

def xr27(x):
    li_ = []
    for i in range(1, len(x)+1):
        y = x['XR27'].loc[i]
        if y >= 10:
            li_.append(10)
        elif y >= 9:
            li_.append(9)
        elif y >= 8:
            li_.append(8)    
        elif y >= 7:
            li_.append(7)    
        elif y >= 6:
            li_.append(6)    
        elif y >= 5:
            li_.append(5)    
        elif y >= 4:
            li_.append(4)    
        elif y >= 3:
            li_.append(3)    
        elif y >= 2:
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
    ave_ = ave(df)
    point_df['AVE'] = ave_
    
    game_ = game(df)
    point_df['GAME'] = game_
    
    stand_ = stand(df)
    point_df['STAND'] = stand_
    
    hit_stand_ = hit_stand(df)
    point_df['HIT_STAND'] = hit_stand_
    
    hit_ = hit(df)
    point_df['HIT'] = hit_
    
    homerun_ = homerun(df)
    point_df['HOMERUN'] = homerun_
    
    hit_point_ = hit_point(df)
    point_df['HIT_POINT'] = hit_point_
    
    steel_ = steel(df)
    point_df['STEEL'] = steel_
    
    four_ball_ = four_ball(df)
    point_df['FOUR_BALL'] = four_ball_

    dead_ball_ = dead_ball(df)
    point_df['DEAD_BALL'] = dead_ball_
    
    struck_out_ = struck_out(df)
    point_df['STRUCK_OUT'] = struck_out_
    
    bant_ = bant(df)
    point_df['BANT'] = bant_
    
    dubble_play_ = dubble_play(df)
    point_df['DUBBLE_PLAY'] = dubble_play_
    
    survived_ = survived(df)
    point_df['SURVIVED'] = survived_
    
    long_hit_ = long_hit(df)
    point_df['LONG_HIT'] = long_hit_
    
    ops_ = ops(df)
    point_df['OPS'] = ops_
    
    rc27_ = rc27(df)
    point_df['RC27'] = rc27_
    
    xr27_ = xr27(df)
    point_df['XR27'] = xr27_
    
    point_df.to_csv(f"point_hit_{team_name}.csv")

for i in range(len(teams)):
    main(over_49_df[i], teams[i])