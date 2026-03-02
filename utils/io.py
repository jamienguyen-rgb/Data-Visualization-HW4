import streamlit as st
import pandas as pd

@st.cache_data
def load_data() -> pd.DataFrame:
    premier23 = pd.read_csv('data/PL-season-2324.csv')
    premier24 = pd.read_csv('data/PL-season-2425.csv')
    def points(df, season_name):
        home23 = df.copy()
        home23['team'] = home23['HomeTeam']
        home23['points'] = 0
        home23.loc[home23['FTR'] == 'H', 'points'] = 3
        home23.loc[home23['FTR'] == 'D', 'points'] = 1
        home23 = home23[['team', 'points']]

        away23 = df.copy()
        away23['team'] = away23['AwayTeam']
        away23['points'] = 0
        away23.loc[away23['FTR'] == 'A', 'points'] = 3
        away23.loc[away23['FTR'] == 'D', 'points'] = 1
        away23 = away23[['team', 'points']]

        teams = pd.concat([home23, away23])
        team_23 = (teams.groupby(['team'], as_index=False).agg('sum'))

        home24 = df.copy()
        home24['team'] = home24['HomeTeam']
        home24['points'] = 0
        home24.loc[home24['FTR'] == 'H', 'points'] = 3
        home24.loc[home24['FTR'] == 'D', 'points'] = 1
        home24 = home24[['team', 'points']]

        away24 = df24.copy()
        away24['team'] = away24['AwayTeam']
        away24['points'] = 0
        away24.loc[away24['FTR'] == 'A', 'points'] = 3
        away24.loc[away24['FTR'] == 'D', 'points'] = 1
        away24 = away24[['team', 'points']]

        teams = pd.concat([home24, away24])
        team_24 = (teams.groupby(['team'], as_index=False).agg('sum'))

        team_23['season'] = season_name
        team_24['season']= season_name
        return team_23, team_24
        
        team_23 = points(premier23, '2023-2024')
        team_24 = points(premier24, '2024-2025')
        both_seasons = pd.concat([team_23, team_24]).reset_index(drop=True)
        
    def wins(df, season_name):
        df['date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
        df['date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')

        matches23 = df.copy()
        matches23['team'] = matches23['HomeTeam']
        matches23['win'] = (matches23['FTR'] == 'H').astype(int)
        matches23['season'] = 'season_name'
        matches23 = matches23[['season','date', 'team', 'win']]

        matches23 = df.copy()
        matches23['team'] = matches23['AwayTeam']
        matches23['win'] = (matches23['FTR'] == 'A').astype(int)
        matches23['season'] = 'season_name'
        matches23 = matches23[['season','date', 'team', 'win']]

        matches23['week'] = matches23['date'].dt.isocalendar().week
        matches23 = (matches23.groupby(['season','team', 'week'], as_index=False
                                      ).agg(win = ('win', 'sum')))

        matches24 = df.copy()
        matches24['team'] = matches24['HomeTeam']
        matches24['win'] = (matches24['FTR'] == 'H').astype(int)
        matches24['season'] = 'season_name'
        matches24 = matches24[['season','date', 'team', 'win']]

        matches24 = df.copy()
        matches24['team'] = matches24['AwayTeam']
        matches24['win'] = (matches24['FTR'] == 'A').astype(int)
        matches24['season'] = 'season_name'
        matches24 = matches24[['season','date', 'team', 'win']]

        matches24['week'] = matches24['date'].dt.isocalendar().week
        matches24 = (matches24.groupby(['season','team', 'week'], as_index=False
                                      ).agg(win=('win', 'sum')))
       
        return matches24
        matches24 = wins(premier24, '2024-2025')
        wins_by_date = pd.concat([matches23, matches24]).reset_index(drop=True)
        wins_by_date['cumulative wins'] = wins_by_date.groupby(['season', 'team'])['win'].cumsum()
        
    return both_seasons, wins_by_date, matches24
