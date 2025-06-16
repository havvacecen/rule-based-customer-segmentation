# import necessary libraries
import pandas as pd

# Load the persona.csv dataset and display basic info and first rows.

# load the dataset:
df = pd.read_csv("persona.csv")
print(df.head())

# display basic info:
print(df.info())         # Quick overview: data types, missing values, memory usage
print(df.describe().T)   # Basic stats for each column (e.g. mean, std, min, max)
print(df.columns )       # Let's check the column names
print(df.shape)          # How big is our dataset? (rows, columns)


# How many unique values are there in the "SOURCE" column? What are their frequencies?
print(df["SOURCE"].nunique())


# How many sales were made at each unique PRICE value?
print(df["PRICE"].value_counts())


# How many sales were made in each country?
print(df["COUNTRY"].value_counts())


# How much revenue was earned from sales in each country?

# Solution with pivot table:
print(df.pivot_table("PRICE", "COUNTRY", aggfunc="sum", observed=False))

# Solution with grouping and aggregation:
print(df.groupby("COUNTRY", observed=False).agg({"PRICE":"sum"}))


# What is the sales quantity for each "SOURCE" type?
print(df["SOURCE"].value_counts())


# What is the mean "PRICE" for each country?
print(df.pivot_table("PRICE", "COUNTRY", aggfunc="mean", observed=False))


# What is the mean "PRICE" for each "SOURCE"?
print(df.pivot_table("PRICE", "SOURCE", aggfunc="mean", observed=False))

# What is the mean "PRICE" in the COUNTRY-SOURCE breakdown?
print(df.pivot_table("PRICE", ["COUNTRY","SOURCE"], aggfunc="mean", observed=False))


# What is the mean earning in the COUNTRY, SOURCE, SEX, AGE breakdown?

# Solution with pivot table:
grouped_price_mean = df.pivot_table("PRICE", ["COUNTRY","SOURCE","SEX", "AGE"], aggfunc="mean", observed=False)
print(grouped_price_mean.head())

# Solution with grouping and aggregation:
agg_df = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE']).agg({'PRICE': lambda x: f"{x.mean():.2f}"})
print(agg_df.head())


# Sort the output by "PRICE" in descending order.
grouped_price_mean = df.pivot_table("PRICE", ["COUNTRY","SOURCE","SEX", "AGE"], aggfunc="mean", observed=False)
agg_df = grouped_price_mean.sort_values("PRICE", ascending=False)
print(agg_df.head())


# Convert the index names to variable names
print(agg_df.index)               # Display the current index
new_agg_df= agg_df.reset_index()  # Convert index to columns
print(new_agg_df.head())          # Show first rows of the new DataFrame
print(new_agg_df.index)           # Display the new index


# Convert the "AGE" column to a categorical variable with convincing age ranges.
# Example ranges: '0_18', '19_23', '24_30', '31_40', '41_70'

print(df["AGE"].dtype)  # Check current dtype of AGE
df["AGG_CAT"] = pd.cut(df["AGE"],
                       bins=[0,18,23,30,40,70],
                       labels=["0_18", "19_23", "24_30", "31_40", "41_70"])
print(df.head())  # Show data after adding categorical AGE_CAT column


# Describe new level-based customers (personas).
# The new variable name: customers_level_based.
# Create this variable by combining observations from the previous output.

grouped_price_mean = df.pivot_table("PRICE", ["COUNTRY","SOURCE","SEX", "AGE","AGG_CAT"], aggfunc="mean", observed=False)
agg_df = grouped_price_mean.sort_values("PRICE", ascending=False).reset_index()


# Create 'customers_level_based' by concatenating relevant columns in uppercase.
agg_df["customers_level_based"] = [
                                  f"{country.upper()}_{source.upper()}_{sex.upper()}_{agg_cat}"
                                  for country, source, sex, agg_cat in zip(
                                  agg_df["COUNTRY"], agg_df["SOURCE"], agg_df["SEX"], agg_df["AGG_CAT"])
                                  ]
print(agg_df[["customers_level_based", "PRICE"]].sort_values("PRICE", ascending=False).head())

# Group by 'customers_level_based' and calculate mean PRICE
agg_df = (agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})).reset_index()
print(agg_df.head())


# Segment the new customer personas based on PRICE.
# Add the segments to the dataframe as a new variable named 'SEGMENT'.
# Describe each segment by calculating the mean, max, and sum of PRICE.

# Divide PRICE into 4 segments and label them as D (lowest) to A (highest):
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])

# Display the first 5 rows of the dataframe to check the new 'SEGMENT' column:
print(agg_df.head())

# Group by 'SEGMENT' and calculate the mean, max, and sum of PRICE for each segment:
print(agg_df.groupby("SEGMENT", observed=False).agg({"PRICE": ["mean", "max", "sum"]}))


# Classify new customers and predict how much revenue they are expected to generate.

# Which segment does a 33-year-old Turkish woman using ANDROID belong to, and what is her expected average revenue?
new_user_a = "TUR_ANDROID_FEMALE_31_40"  # Define new user profile string
result_a = agg_df[agg_df["customers_level_based"] == new_user_a]  # Filter data for this profile
print(result_a[["SEGMENT","PRICE"]])  # Show segment and expected revenue

# Which segment does a 35-year-old French woman using IOS belong to, and what is her expected average revenue?
new_user_b = "FRA_IOS_FEMALE_31_40"   # Define the profile string for the new user
result_b = agg_df[agg_df["customers_level_based"] == new_user_b]   # Filter data for this profile
print(result_b[["SEGMENT","PRICE"]])   # Show segment and expected revenue