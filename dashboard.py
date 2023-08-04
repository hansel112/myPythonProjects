import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Load dummy data
df = pd.DataFrame({
    "Patient Age": [25, 30, 35, 40, 45, 50],
    "Admission Date": ["2022-01-01", "2022-01-02", "2022-01-03",
                       "2022-01-04", "2022-01-05", "2022-01-06"],
    "Discharge Date": ["2022-01-05", "2022-01-06", "2022-01-07",
                       "2022-01-08", "2022-01-09", "2022-01-10"],
    "Admission Type": ["Emergency", "Elective", "Emergency", "Elective",
                       "Emergency", "Elective"],
    "Patient Outcome": ["Discharged", "Discharged", "Deceased",
                        "Discharged", "Deceased", "Discharged"]
})

app.layout = html.Div([
    # Patient Age Distribution
    html.H3("Patient Age Distribution"),
    dcc.Graph(
        figure=px.histogram(df, "Patient Age").update_layout(title_text="Patient Age Distribution"),
        id="age-distribution"
    ),

    # Patient Outcome
    html.H3("Patient Outcome"),
    dcc.Graph(
        figure=px.pie(df, values="Patient Age", names="Patient Outcome").update_layout(title_text="Patient Outcome"),
        id="patient-outcome"
    ),

    # Admission Type
    html.H3("Admission Type"),
    dcc.Graph(
        figure=px.pie(df, values="Patient Age", names="Admission Type").update_layout(title_text="Admission Type"),
        id="admission-type"
    ),
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8000)
