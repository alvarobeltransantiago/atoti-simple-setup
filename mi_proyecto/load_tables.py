from pathlib import Path

import atoti as tt
import pandas as pd

RESOURCES_DIRECTORY = Path(__file__).parent / "__resources__"


def read_sensitivities() -> pd.DataFrame:
    sensitivities = pd.read_csv(
        RESOURCES_DIRECTORY / "sensitivities.csv",
        parse_dates=["AsOfDate"],
    )
    sensitivities["AsOfDate"] = sensitivities["AsOfDate"].dt.date
    return sensitivities


def build_calendar(sensitivities: pd.DataFrame) -> pd.DataFrame:
    calendar = pd.DataFrame(
        {"AsOfDate": pd.to_datetime(sensitivities["AsOfDate"].unique())}
    )
    calendar["Year"] = calendar["AsOfDate"].dt.year.astype(str)
    calendar["Quarter"] = "Q" + calendar["AsOfDate"].dt.quarter.astype(str)
    calendar["Month"] = calendar["AsOfDate"].dt.month.astype(str).str.zfill(2)
    calendar["Day"] = calendar["AsOfDate"].dt.day.astype(str).str.zfill(2)
    calendar["AsOfDate"] = calendar["AsOfDate"].dt.date
    return calendar


def load_tables(session: tt.Session) -> None:
    session.tables["Sensitivities"].load(tt.CsvLoad(RESOURCES_DIRECTORY / "sensitivities.csv"))
    session.tables["TradeInfo"].load(tt.CsvLoad(RESOURCES_DIRECTORY / "trade_info.csv"))
    session.tables["RiskFactors"].load(tt.CsvLoad(RESOURCES_DIRECTORY / "risk_factors.csv"))

    sensitivities = read_sensitivities()
    calendar = build_calendar(sensitivities)
    session.tables["Calendar"].load(calendar)
