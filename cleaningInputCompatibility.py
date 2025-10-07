import pandas as pd

def input_compatibility(path: str, sheet: str = "Data"):
    df = pd.read_excel(path, sheet_name=sheet, engine="openpyxl")
    df = df.dropna(how="all")  # drop blank rows

    # Safely parse the ID column; keep only rows with numeric IDs
    ids_col = pd.to_numeric(df.iloc[:, 0], errors="coerce")
    mask = ids_col.notna()
    df = df.loc[mask].reset_index(drop=True)
    ids = ids_col[mask].astype(int).tolist()

    # Build a symmetric compatibility matrix C from the remaining numeric columns
    n = len(ids)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            # +1 skips the ID column; coerce to number, treat NaN as 0
            v = pd.to_numeric(df.iat[i, j+1], errors="coerce")
            v = 0 if pd.isna(v) else int(v)
            C[i][j] = C[j][i] = v
    return C, ids
