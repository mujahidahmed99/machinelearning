import pandas as pd
import numpy as numpy

team_stats = pd.read_csv('team_stats.csv')
fixtures = pd.read_csv('fixtures.csv')

col_name = ['HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HM1_D', 'HM1_L', 'HM1_M', 'HM1_W', 
'HM2_D', 'HM2_L', 'HM2_M', 'HM2_W', 'HM3_D', 'HM3_L', 'HM3_M', 'HM3_W', 'HM4_D', 'HM4_L', 'HM4_M', 
'HM4_W', 'HM5_D', 'HM5_L', 'HM5_M', 'HM5_W', 'AM1_D', 'AM1_L', 'AM1_M', 'AM1_W', 'AM2_D', 'AM2_L', 
'AM2_M', 'AM2_W', 'AM3_D', 'AM3_L', 'AM3_M', 'AM3_W', 'AM4_D', 'AM4_L', 'AM4_M', 'AM4_W', 'AM5_D', 
'AM5_L', 'AM5_M', 'AM5_W', 'HTFormPts', 'ATFormPts', 'HTGD', 'ATGD', 'DiffPts', 'DiffFormPts', 'DiffxG']
home_shots = []
away_shots = []
home_shots_target = []
away_shots_target = []
home_fouls = []
away_fouls = []
home_corners = []
away_corners = []
HM1_D = []
HM1_L = []
HM1_M = []
HM1_W = []
HM2_D = []
HM2_L = []
HM2_M = []
HM2_W = []
HM3_D = []
HM3_L = []
HM3_M = []
HM3_W = []
HM4_D = []
HM4_L = []
HM4_M = []
HM4_W = []
HM5_D = []
HM5_L = []
HM5_M = []
HM5_W = []
AM1_D = []
AM1_L = []
AM1_M = []
AM1_W = []
AM2_D = []
AM2_L = []
AM2_M = []
AM2_W = []
AM3_D = []
AM3_L = []
AM3_M = []
AM3_W = []
AM4_D = []
AM4_L = []
AM4_M = []
AM4_W = []
AM5_D = []
AM5_L = []
AM5_M = []
AM5_W = []
home_team_form_pts = []
away_team_form_pts = []
home_gd = []
away_gd = []
home_pts = 0
away_pts = 0
home_xg = 0
away_xg = 0
point_diff = []
form_point_diff = []
diff_xg = []
for index in range(len(fixtures)):
    home_pts = 0
    away_pts = 0
    home_xg = 0
    away_xg = 0
    home_form = 0
    away_form = 0
    for j in range(len(team_stats)):
        if fixtures['HomeTeam'][index] == team_stats['team'][j]:
            home_shots.append(team_stats['Shots'][j] / team_stats['played'][j])
            home_shots_target.append(team_stats['Shots_on_Target'][j] / team_stats['played'][j])
            home_fouls.append(team_stats['Fouls'][j] / team_stats['played'][j])
            home_corners.append(team_stats['Corners'][j] / team_stats['played'][j])
            HM1_D.append(team_stats['M1_D'][j])
            HM1_L.append(team_stats['M1_L'][j])
            HM1_M.append(team_stats['M1_M'][j])
            HM1_W.append(team_stats['M1_W'][j])
            HM2_D.append(team_stats['M2_D'][j])
            HM2_L.append(team_stats['M2_L'][j])
            HM2_M.append(team_stats['M2_M'][j])
            HM2_W.append(team_stats['M2_W'][j])
            HM3_D.append(team_stats['M3_D'][j])
            HM3_L.append(team_stats['M3_L'][j])
            HM3_M.append(team_stats['M3_M'][j])
            HM3_W.append(team_stats['M3_W'][j])
            HM4_D.append(team_stats['M4_D'][j])
            HM4_L.append(team_stats['M4_L'][j])
            HM4_M.append(team_stats['M4_M'][j])
            HM4_W.append(team_stats['M4_W'][j])
            HM5_D.append(team_stats['M5_D'][j])
            HM5_L.append(team_stats['M5_L'][j])
            HM5_M.append(team_stats['M5_M'][j])
            HM5_W.append(team_stats['M5_W'][j])
            home_pts = team_stats['pts'][j] / team_stats['played'][j]
            home_team_form_pts.append(team_stats['FormPts'][j] / team_stats['played'][j])
            home_form = team_stats['FormPts'][j] / team_stats['played'][j]
            home_gd.append(team_stats['GD'][j] / team_stats['played'][j] / team_stats['played'][j])
            home_xg = team_stats['xG'][j] / team_stats['played'][j]
        if fixtures['AwayTeam'][index] == team_stats['team'][j]:
            away_shots.append(team_stats['Shots'][j] / team_stats['played'][j])
            away_shots_target.append(team_stats['Shots_on_Target'][j] / team_stats['played'][j])
            away_fouls.append(team_stats['Fouls'][j] / team_stats['played'][j])
            away_corners.append(team_stats['Corners'][j] / team_stats['played'][j])
            AM1_D.append(team_stats['M1_D'][j])
            AM1_L.append(team_stats['M1_L'][j])
            AM1_M.append(team_stats['M1_M'][j])
            AM1_W.append(team_stats['M1_W'][j])
            AM2_D.append(team_stats['M2_D'][j])
            AM2_L.append(team_stats['M2_L'][j])
            AM2_M.append(team_stats['M2_M'][j])
            AM2_W.append(team_stats['M2_W'][j])
            AM3_D.append(team_stats['M3_D'][j])
            AM3_L.append(team_stats['M3_L'][j])
            AM3_M.append(team_stats['M3_M'][j])
            AM3_W.append(team_stats['M3_W'][j])
            AM4_D.append(team_stats['M4_D'][j])
            AM4_L.append(team_stats['M4_L'][j])
            AM4_M.append(team_stats['M4_M'][j])
            AM4_W.append(team_stats['M4_W'][j])
            AM5_D.append(team_stats['M5_D'][j])
            AM5_L.append(team_stats['M5_L'][j])
            AM5_M.append(team_stats['M5_M'][j])
            AM5_W.append(team_stats['M5_W'][j])
            away_pts = team_stats['pts'][j] / team_stats['played'][j]
            away_team_form_pts.append(team_stats['FormPts'][j] / team_stats['played'][j])
            away_form = team_stats['FormPts'][j] / team_stats['played'][j]
            away_gd.append(team_stats['GD'][j] / team_stats['played'][j])
            away_xg = team_stats['xG'][j] / team_stats['played'][j]

    point_diff.append(home_pts - away_pts)
    form_point_diff.append(home_form - away_form)
    diff_xg.append(home_xg - away_xg)

    df = pd.DataFrame([home_shots, away_shots, home_shots_target, away_shots_target, home_fouls, away_fouls,
    home_corners, away_corners, HM1_D, HM1_L, HM1_M, HM1_W, HM2_D, HM2_L, HM2_M, HM2_W, HM3_D, HM3_L, HM3_M,
    HM3_W, HM4_D, HM4_L, HM4_M, HM4_W, HM5_D, HM5_L, HM5_M, HM5_W, AM1_D, AM1_L, AM1_M, AM1_W, AM2_D, AM2_L, AM2_M,
    AM2_W, AM3_D, AM3_L, AM3_M, AM3_W, AM4_D, AM4_L, AM4_M, AM4_W, AM5_D, AM5_L, AM5_M, AM5_W, home_team_form_pts, away_team_form_pts,
    home_gd, away_gd, point_diff, form_point_diff, diff_xg], index=col_name )

    df = df.T
    
df.to_csv('rndm_forest_fixtures.csv', index=False)


