import atoti as tt

#Función para crear el cubo.
def create_cubes(session: tt.Session) -> None:

    #Creamos el cubo
    cube = session.create_cube(
        session.tables["Sensitivities"],
        name="SensitivityCube",
        mode="manual",
    )

    #Definimos las hiearchies y las measures. 
    h = cube.hierarchies
    l = cube.levels
    m = cube.measures

    h["Time"] = {
        "Year": session.tables["Calendar"]["Year"],
        "Quarter": session.tables["Calendar"]["Quarter"],
        "Month": session.tables["Calendar"]["Month"],
        "Day": session.tables["Calendar"]["Day"],
    }

    h["RiskHierarchy"] = {
        "RiskClass": session.tables["RiskFactors"]["RiskClass"],
        "Bucket": session.tables["RiskFactors"]["Bucket"],
        "Currency": session.tables["RiskFactors"]["Currency"],
    }

    m["Delta.SUM"] = tt.agg.sum(session.tables["Sensitivities"]["Delta"])
    m["Vega.SUM"] = tt.agg.sum(session.tables["Sensitivities"]["Vega"])
    m["Vega.MEAN"] = tt.agg.mean(session.tables["Sensitivities"]["Vega"])
    m["Vega.MAX"] = tt.agg.max(session.tables["Sensitivities"]["Vega"])

    m["Delta_pct_RiskClass"] = m["Delta.SUM"] / tt.parent_value(
        m["Delta.SUM"],
        degrees={h["RiskHierarchy"]: 1},
    )