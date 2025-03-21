import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Read data
hist1 = pd.read_csv("data/1MsunData/history.data")
hist25 = pd.read_csv("data/25MsunData/history.data")

profile_95 = pd.read_csv("data/1MsunData/profile.95.data")
profile_147 = pd.read_csv("data/1MsunData/profile.147.data")
profile_290 = pd.read_csv("data/1MsunData/profile.290.data")
profile_4903 = pd.read_csv("data/1MsunData/profile.4903.data")
profile_5632 = pd.read_csv("data/1MsunData/profile.5632.data")

profiles = [
    {
        "profile": profile_95,
        "model_number": 95,
        "description": "Ignition of H burning in core (ZAMS)",
    },
    {
        "profile": profile_147,
        "model_number": 147,
        "description": "Present-day Sun",
    },
    {
        "profile": profile_290,
        "model_number": 290,
        "description": "Exhaustion of H in core",
    },
    {
        "profile": profile_4903,
        "model_number": 4903,
        "description": "He core becomes non degenerate",
    },
    {
        "profile": profile_5632,
        "model_number": 5632,
        "description": "Envelope of star ejected",
    },
]

phases = [
    {
        "model_number_start": 100,
        "model_number_end": 170,
        "description": "Main Sequence",
    },
    {
        "model_number_start": 170,
        "model_number_end": 310,
        "description": "Subgiant Branch",
    },
    {
        "model_number_start": 310,
        "model_number_end": 3650,
        "description": "Red Giant Branch",
    },
    {
        "model_number_start": 3650,
        "model_number_end": 5360,
        "description": "Core He burning",
    },
    {
        "model_number_start": 5360,
        "model_number_end": 5570,
        "description": "Asymptotic Giant Branch",
    },
]

# Initialize Dash app
app = dash.Dash(__name__)

fig = px.scatter(
    hist1, x="log_Teff", y="log_L", color="model_number", title="Stellar Evolution"
)
fig.update_layout(xaxis_autorange="reversed")


# for profile_info in profiles[1:]:
#     model_number = profile_info["model_number"]

#     row = hist1[hist1["model_number"] == model_number]
#     x = row["log_Teff"]
#     y = row["log_L"]
#     fig.add_scatter(x=x, y=y, mode="markers", name=model_number)

#     # Add text annotation
#     fig.add_annotation(
#         x=x,
#         y=y,
#         text=f"({model_number}) {profile_info['description']}",
#         showarrow=True,
#     )

# App layout
app.layout = html.Div(
    [
        html.H1("Stellar Evolution Plot"),
        dcc.Graph(
            id="evolution-plot", figure=fig, style={"width": "100%", "height": "800px"}
        ),
    ],
    style={"width": "100%", "maxWidth": "968px", "margin": "auto"},
)


# # Callback to update plot
# @app.callback(Output("evolution-plot", "figure"), Input("profile-selector", "value"))
# def update_plot(selected_profiles):
#     # Create base plot with all history data
#     fig = px.scatter(
#         hist1, x="log_Teff", y="log_L", color="model_number", title="Stellar Evolution"
#     )

#     # Add selected profile points
#     for profile_info in profiles:
#         if str(profile_info["model_number"]) in selected_profiles:
#             model_number = profile_info["model_number"]
#             row = hist1[hist1["model_number"] == model_number]

#             fig.add_scatter(
#                 x=row["log_Teff"],
#                 y=row["log_L"],
#                 mode="markers+text",
#                 marker=dict(symbol="triangle-up", size=15),
#                 name=f"Model {model_number}",
#                 text=f"({model_number}) {profile_info['description']}",
#                 textposition="top right",
#             )

#     # Customize layout
#     fig.update_layout(
#         xaxis_title="log Teff", yaxis_title="log L", xaxis={"autorange": "reversed"}
#     )

#     return fig


if __name__ == "__main__":
    app.run_server(debug=True)
