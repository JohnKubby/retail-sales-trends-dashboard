
import pandas as pd
import numpy as np
import os

np.random.seed(42)

years = list(range(2018, 2024))
regions = ["North America", "Europe", "Asia", "South America", "Africa"]
categories = ["Electronics", "Clothing", "Home & Garden", "Toys", "Groceries"]

os.makedirs("../data", exist_ok=True)

region_sales = []
for year in years:
    for region in regions:
        sales = np.random.randint(50000, 150000)
        region_sales.append([year, region, sales])
region_df = pd.DataFrame(region_sales, columns=["Year", "Region", "Sales"])
region_df.to_csv("../data/regional_sales.csv", index=False)

category_sales = []
for year in years:
    for category in categories:
        sales = np.random.randint(20000, 100000)
        category_sales.append([year, category, sales])
category_df = pd.DataFrame(category_sales, columns=["Year", "Category", "Sales"])
category_df.to_csv("../data/product_sales.csv", index=False)
