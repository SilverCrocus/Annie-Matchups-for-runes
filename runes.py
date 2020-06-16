import pandas as pd


sheet_id = "1weLfPPWwnw08I_2cF69nJs9eaQPMdqErzQU-teQicVA"

data = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
col_lst = []
for col in data.columns:
    # print(col)
    col_lst.append(col)
# print(col_lst)

data = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv", usecols=col_lst[:-2])

champ_lst = []
for champ in data["Matchup"]:
    champ_lst.append(champ)

opp = input("Match up?: ")
index = champ_lst.index(f"{opp}")
print(data.iloc[index])
prompt = input("Close or new matchup: ")
if prompt == "q":
    quit()