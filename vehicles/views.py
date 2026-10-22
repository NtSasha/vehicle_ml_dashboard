
import pandas as pd
from pathlib import Path
from django.shortcuts import render
from .dashboard import frequency_table, manufacturer_chart


def dashboard_view(request):
    csv_path = (
        Path(__file__).resolve().parent.parent
        / "dummy_data"
        / "vehicles_ml_dataset.csv"
    )

    df = pd.read_csv(csv_path)

    context = {
        "total_vehicles": len(df),
        "total_manufacturers": df["manufacturer"].nunique(),
        "frequency_table": frequency_table(df),
        "chart_html": manufacturer_chart(df),
    }

    return render(request, "vehicles/index.html", context)
