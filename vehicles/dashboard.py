
import pandas as pd
import plotly.express as px


def frequency_table(df):
    # Count vehicles for each manufacturer
    manufacturer_counts = df["manufacturer"].value_counts().reset_index()
    manufacturer_counts.columns = ["Manufacturer", "Count"]

    # Convert the frequency table to HTML
    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-hover table-sm",
        justify="center",
        index=False
    )

    return table_html


def manufacturer_chart(df):
    # Calculate the number of vehicles per manufacturer
    manufacturer_counts = (
        df["manufacturer"]
        .value_counts()
        .reset_index()
    )

    manufacturer_counts.columns = ["Manufacturer", "Count"]

    # Display the 15 most frequent manufacturers
    manufacturer_counts = manufacturer_counts.head(15)

    # Create the bar chart
    fig = px.bar(
        manufacturer_counts,
        x="Manufacturer",
        y="Count",
        title="Top 15 Manufacturers by Number of Vehicles",
        labels={
            "Manufacturer": "Vehicle Manufacturer",
            "Count": "Number of Vehicles"
        },
        text="Count"
    )

    fig.update_traces(
        textposition="outside",
        marker_color="#0d6efd"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_tickangle=-35,
        margin=dict(l=40, r=30, t=70, b=100),
        height=500
    )

    # Convert the chart into HTML for the Django template
    chart_html = fig.to_html(
        full_html=False,
        include_plotlyjs="cdn"
    )

    return chart_html
