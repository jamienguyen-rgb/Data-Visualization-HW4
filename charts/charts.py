import altair as alt
import pandas as pd

def base_theme():
    return {
        "config": {
            "view": {"stroke": None},
            "axis": {"labelFontSize": 12, "titleFontSize": 14},
            "legend": {"labelFontSize": 12, "titleFontSize": 14},
        }
    }


def dashboard(points_df: pd.DataFrame, wins_df: pd.DataFrame) -> alt.Chart:
    click = alt.selection_point(fields=['team'])

    seasons_dotplot = (
        alt.Chart(points_df).mark_circle().encode(
            x='team:N',
            y='points:Q',
            color='season:N',
            opacity=alt.condition(click, alt.value(1), alt.value(0.15)),
            tooltip=[
                alt.Tooltip('team:N'),
                alt.Tooltip('season:N')],
        ).add_params(
                click
        ).properties(title='Team Points by Season')
    )
    wins_line = (
        alt.Chart(wins_df).transform_filter(
            click
        ).mark_line().encode(
            x='week:O',
            y='cumulative wins:Q',
            color='season:N',
            tooltip=[
                alt.Tooltip('team:N'),
                alt.Tooltip('season:N'),
                alt.Tooltip('cumulative wins:Q')],
        ).properties(
            title='Weekly Wins by Season')
    )
    return alt.vconcat(seasons_dotplot, wins_line).resolve_scale(color="independent")

def point_diff_chart(df: pd.DataFrame) -> alt.Chart:
    point_differences = df.pivot(
        index='team', columns='season', values='points').reset_index().dropna()
    point_differences['point_diff'] = point_differences['2024-2025'] - point_differences['2023-2024']
    sort_order = point_differences.sort_values(by='2024-2025', ascending=False)
    team_order = list(sort_order['team'])
    return (
        alt.Chart(point_differences)
        .mark_bar().encode(
            x=alt.X('point_diff:Q', title='Point Difference'),
            y=alt.Y('team:N', sort=team_order, title = 'Teams by 2024-2025 Points'),
            color=alt.condition(
                alt.datum.point_diff > 0,
                alt.value('green'),
                alt.value('red')),
            tooltip=[
                alt.Tooltip('team:N'),
                alt.Tooltip('2023-2024:Q'),
                alt.Tooltip('2024-2025:Q'),
                alt.Tooltip('point_diff:Q')]
        ).properties(title='Change in Team Points between 2024-2025 and 2023-2024 Season')
    )

def wins_line_promoted(df: pd.DataFrame) -> alt.Chart:
    matches24 = df[df['season'] == '2024-2025'].copy()
    promoted_teams= ['Ipswich', 'Leicester', 'Southampton']
    promoted_df = df.copy() 
    promoted_df['group'] = 'Not Promoted'
    promoted_df.loc[promoted_df['team'].isin(promoted_teams), 'group'] = 'Promoted'
    promoted_df['cumulative wins'] = (promoted_df.groupby(['team'])['win'].cumsum())
    grouped_promoted = (promoted_df.groupby(
        ['group', 'week'], as_index=False).agg(average_cumulative_wins=('cumulative wins', 'mean')))
    return (
        alt.Chart(grouped_promoted).mark_line().encode(
            x='week:O',
            y=alt.Y('average_cumulative_wins:Q', title = 'average cumulative wins'),
            color='group:N',
            tooltip=[
                alt.Tooltip('average_cumulative_wins:Q', title = 'average cumulative wins')]
        ).properties(title='Average Cumulative Weekly Wins for Promoted vs Non-Promoted Teams (2024-2025)')
    )

def points_line(df: pd.DataFrame) -> alt.Chart:
    point_differences = df.pivot(
        index='team', columns='season', values='points').reset_index().dropna()
    return (
        alt.Chart(point_differences
         ).mark_circle(size=100).encode(
            x=alt.X('2023-2024:Q', title='Points in 2023-2024'),
            y=alt.Y('2024-2025:Q', title='Points in 2024-2025'),
            tooltip=[
                alt.Tooltip('team:N', title='Team'),
                alt.Tooltip('2023-2024:Q', title='2023-24 Points'),
                alt.Tooltip('2024-2025:Q', title='2024-25 Points'),            ]
        ).properties(
            title='2023-2024 Points vs 2024-2025 Points',
            width=600,
            height=400
        )
    )
