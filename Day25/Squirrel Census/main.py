import pandas
data=pandas.read_csv("census_squirrel.csv")
fur=data["Primary Fur Color"].dropna().unique().tolist()
count=data["Primary Fur Color"].value_counts().to_list()
squirrel_data={"Fur":fur,"Count":count}
squirrel_count=pandas.DataFrame(squirrel_data)
print(squirrel_count)
squirrel_count.to_csv("squirrel_count.csv")