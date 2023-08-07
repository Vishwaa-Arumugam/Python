import pandas

df = pandas.read_csv("Movies.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df.drop(df[df["id"]==786345].id, inplace=True)
print(df)
df.to_csv("Movies.csv")
