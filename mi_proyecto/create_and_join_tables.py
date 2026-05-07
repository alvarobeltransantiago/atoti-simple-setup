import atoti as tt


def create_and_join_tables(session: tt.Session) -> None:
    sensitivities = session.create_table(
        "Sensitivities",
        keys={"TradeId", "AsOfDate", "RiskFactor"},
        data_types={
            "TradeId": tt.STRING,
            "AsOfDate": tt.LOCAL_DATE,
            "RiskFactor": tt.STRING,
            "Delta": tt.DOUBLE,
            "Vega": tt.DOUBLE,
            "CurvatureUp": tt.DOUBLE,
            "CurvatureDown": tt.DOUBLE,
        },
        default_values={
            "Delta": 0.0,
            "Vega": 0.0,
            "CurvatureUp": 0.0,
            "CurvatureDown": 0.0,
        },
    )

    trade_info = session.create_table(
        "TradeInfo",
        keys={"TradeId"},
        data_types={
            "TradeId": tt.STRING,
            "Desk": tt.STRING,
            "Book": tt.STRING,
            "Counterparty": tt.STRING,
            "ProductType": tt.STRING,
        },
    )

    risk_factors = session.create_table(
        "RiskFactors",
        keys={"RiskFactor"},
        data_types={
            "RiskFactor": tt.STRING,
            "RiskClass": tt.STRING,
            "Bucket": tt.STRING,
            "Currency": tt.STRING,
        },
    )

    calendar = session.create_table(
        "Calendar",
        keys={"AsOfDate"},
        data_types={
            "AsOfDate": tt.LOCAL_DATE,
            "Year": tt.STRING,
            "Quarter": tt.STRING,
            "Month": tt.STRING,
            "Day": tt.STRING,
        },
    )

    sensitivities.join(trade_info)
    sensitivities.join(risk_factors)
    sensitivities.join(calendar)
