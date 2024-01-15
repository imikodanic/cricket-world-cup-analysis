import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio


def read_data(file_path):
    return pd.read_csv(file_path)


def display_head(data):
    print(data.head())


def display_bar_chart(data, x, title):
    figure = px.bar(data, x=x, title=title)
    figure.show()


def display_pie_chart(values, title, colors):
    figure = go.Figure(data=[go.Pie(labels=values.index, values=values.values)])
    figure.update_layout(
        title_text=title,
        legend=dict(orientation="h"),
    )
    figure.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                      marker=dict(colors=colors, line=dict(color='black', width=3)))
    figure.show()


def display_grouped_bar_chart(data, x, y, color, title):
    figure = px.bar(data, x=x, y=y, color=color, title=title)
    figure.show()


def display_dual_grouped_bar_chart(x, y1, y2, name1, name2, title):
    figure = go.Figure()
    figure.add_trace(go.Bar(x=x, y=y1, name=name1, marker_color='blue'))
    figure.add_trace(go.Bar(x=x, y=y2, name=name2, marker_color='red'))
    figure.update_layout(barmode='group', xaxis_tickangle=-45, title=title)
    figure.show()


def main():
    pio.templates.default = "plotly_white"
    file_path = "t20-world-cup-22.csv"
    data = read_data(file_path)

    # Display data head
    display_head(data)

    # Number of Matches Won
    display_bar_chart(data, x=data["winner"], title="Number of Matches Won by teams in t20 World Cup 2022")

    # Matches Won By Runs Or Wickets
    won_by_values = data["won by"].value_counts()
    display_pie_chart(won_by_values, 'Number of Matches Won By Runs Or Wickets', ['gold', 'lightgreen'])

    # Toss Decisions
    toss_values = data["toss decision"].value_counts()
    display_pie_chart(toss_values, 'Toss Decisions in t20 World Cup 2022', ['skyblue', 'yellow'])

    # Top Scorers
    display_grouped_bar_chart(data, x=data["top scorer"], y=data["highest score"],
                              color=data["highest score"], title="Top Scorers in t20 World Cup 2022")

    # Player of the Match Awards
    display_bar_chart(data, x=data["player of the match"], title="Player of the Match Awards in t20 World Cup 2022")

    # Best Bowlers
    display_bar_chart(data, x=data["best bowler"], title="Best Bowlers in t20 World Cup 2022")

    # Best Stadiums to Bat First or Chase
    display_dual_grouped_bar_chart(x=data["venue"], y1=data["first innings score"],
                                   y2=data["second innings score"], name1='First Innings Runs',
                                   name2='Second Innings Runs', title="Best Stadiums to Bat First or Chase")

    # Best Stadiums to Bowl First or Defend
    display_dual_grouped_bar_chart(x=data["venue"], y1=data["first innings wickets"],
                                   y2=data["second innings wickets"], name1='First Innings Wickets',
                                   name2='Second Innings Wickets', title="Best Stadiums to Bowl First or Defend")


if __name__ == "__main__":
    main()
