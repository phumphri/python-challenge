
<h1>Heroes Of Pymoli Data Analysis</h1>
<ul>
    <li>Most Popular:  <b>Betrayal, Whisper of Grieving Widows</b></li>
    <li>Age Group Spending the Most:  <b>20-24</b></li>
    <li>Gender that Purchase the Most:  <b>Male</b></li>
</ul>


```python
import pandas as pd
import numpy as np
```


```python
# Load the json file to a dataframe.
# This dataframe will be used as the database.
f = "purchase_data.json"
df = pd.read_json(f, orient='records')
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Players with multiple purchases.

# Get players (including duplicates).
series_SN = df.loc[:,'SN'] 

# Create a dictionary of unique players with there number of purchases
dict_SN = dict(series_SN.groupby(series_SN).count())

# Create a dictionary containing the column name for the count.
columns_SN = {'Count'}

# Create a dataframe of unique players and their number of purchases.
df_SN = pd.DataFrame(dict_SN, columns_SN)

# Swap axis for presentation and filtering
df_SN = df_SN.T

# Select those that have more tha one purchase.
df_SN = df_SN.loc[df_SN.Count > 1]

# Select the index SN's of the players with multiple purchases.
index_SN = df_SN.index

# Put the index into a list to used as a filer.
list_SN = list(index_SN.values)

# Display the puchases for players that have more than one purchase.
df.loc[df.SN.isin(list_SN)].sort_values(by=['SN', 'Item ID']).head(10)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>308</th>
      <td>37</td>
      <td>Male</td>
      <td>79</td>
      <td>Alpha, Oath of Zeal</td>
      <td>2.88</td>
      <td>Aduephos78</td>
    </tr>
    <tr>
      <th>431</th>
      <td>37</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Aduephos78</td>
    </tr>
    <tr>
      <th>377</th>
      <td>37</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Aduephos78</td>
    </tr>
    <tr>
      <th>721</th>
      <td>26</td>
      <td>Male</td>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>2.35</td>
      <td>Aeduera68</td>
    </tr>
    <tr>
      <th>224</th>
      <td>26</td>
      <td>Male</td>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>Aeduera68</td>
    </tr>
    <tr>
      <th>647</th>
      <td>26</td>
      <td>Male</td>
      <td>156</td>
      <td>Soul-Forged Steel Shortsword</td>
      <td>1.16</td>
      <td>Aeduera68</td>
    </tr>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>529</th>
      <td>38</td>
      <td>Male</td>
      <td>172</td>
      <td>Blade of the Grave</td>
      <td>1.69</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>637</th>
      <td>20</td>
      <td>Male</td>
      <td>18</td>
      <td>Torchlight, Bond of Storms</td>
      <td>1.77</td>
      <td>Aeliriam77</td>
    </tr>
    <tr>
      <th>359</th>
      <td>20</td>
      <td>Male</td>
      <td>32</td>
      <td>Orenmir</td>
      <td>4.95</td>
      <td>Aeliriam77</td>
    </tr>
  </tbody>
</table>
</div>



<h2>Player Count</h2>


```python
# Player Count

# Get a series of unique players and then count the number of players.
unique_player_count = df.loc[:,'SN'].unique().size

# For grins and giggles, count the total number of players in the data.
all_player_count = df.loc[:,'SN'].size

# Build a dictionary of players and their count to be used in a dataframe.
data_player_count = {"Unique":unique_player_count, "All":all_player_count}

# Build a list of headers to be used in the dataframe.
columns_player_count = ['Total Players']

# Create the dataframe of players and their count.
df_player_count = pd.DataFrame(data_player_count, columns_player_count)

# Flip the axis for display.
df_player_count = df_player_count.T

# Display the players and counts for unique players and all players.
df_player_count.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>All</th>
      <td>780</td>
    </tr>
    <tr>
      <th>Unique</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



<h2>Purchasing Analysis (Total)</h2>


```python
# Purchasing Analysis (Total)

# Callculate total revenue.
total_revenue = df['Price'].sum()

# Calculate number of purchases.
number_of_purchases = df['Price'].count()

# Calculate the average price of a purchase.
average_price = total_revenue / number_of_purchases

# Calculate the number of unique items.
number_of_unique_items = df['Item ID'].unique().size

# Create a dataframe with just the number of unique items.
total_dict = {}
total_dict["Number of Unique Items"] = number_of_unique_items
total_cols = [" "]
df_total = pd.DataFrame(total_dict, total_cols)

# Add average price, number of purchases, and total revenue to the dataframe.
df_total['Average Price'] = average_price
df_total["Number of Purchases"] = number_of_purchases
df_total["Total Revenue"] = total_revenue

# Format the currency fields of average price and total revenue,.
df_total['Average Price'] = df_total['Average Price'].map('${:,.2f}'.format)
df_total["Total Revenue"] = df_total["Total Revenue"].map('${:,.2f}'.format)

# Display the dataframe with the calculated and formated amounts.
df_total
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th></th>
      <td>183</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>



<h2>Gender Demographics</h2>


```python
# Gender Demographics

# Get all unique players and their gender.
df_gender = df[['Gender', 'SN']].drop_duplicates()

# Calculate the number of players for the percentage calculation.
total_population = df_gender['SN'].count()

# Group the players by gender and count the number in each group.
df_gender = df_gender.groupby('Gender').count()

# Rename the column with count of players to total players.
df_gender = df_gender.rename(columns={"SN": "Total Count"})

# Calculate the percentage of players in each group.
df_gender['Percentage of Players'] = round((df_gender['Total Count'] / total_population) * 100, 2)

# Rearrange the columns to meet display requirements.,
df_gender = df_gender.reindex(columns=['Percentage of Players', 'Total Count'])

# Rearrange the rows do display the number of players is descending order.
df_gender = df_gender.sort_values(by='Total Count', ascending=False)

# Display the player count by gender.
df_gender
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



<h2>Purchasing Analysis (Gender)</h2>


```python
# Purchasing Analysis (Gender)

# Get the gender and price for each purchase.
df_purgen = df[['Gender', 'Price']]

# Let the computer do the work:  Aggregate by gender.
df_purgen = df_purgen.groupby('Gender').agg({'Price': ['count', 'mean', 'sum', 'median']})

# Aggregation creates a multiple-level index with price on top.  Delete it.,
df_purgen.columns = df_purgen.columns.droplevel(0)

# Sort results by total purchase value.
df_purgen = df_purgen.sort_values(by="sum", ascending=False)

# Create a dictionary of new column headings to meet requirements.
column_names = {}
column_names['count'] = 'Purchase Count'
column_names['mean'] = 'Average Purchase Price'
column_names['sum'] = "Total Purchase Value"
column_names['median'] = "Normalized Totals"

# Rename the column headings in the dataframe.
df_purgen = df_purgen.rename(columns=column_names)

# Format currency fields
df_purgen['Average Purchase Price'] = df_purgen['Average Purchase Price'].map('${:,.2f}'.format)
df_purgen['Total Purchase Value'] = df_purgen['Total Purchase Value'].map('${:,.2f}'.format)
df_purgen['Normalized Totals'] = df_purgen['Normalized Totals'].map('${:,.2f}'.format)

# Display the dataframe with the analysis
df_purgen
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$2.62</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$3.73</td>
    </tr>
  </tbody>
</table>
</div>



<h2>Age Demographics</h2>


```python
# Age Demographics

# Create a datafram of users and their ages.
df_age = pd.DataFrame(df[['Age','SN']].to_dict())

# Remove the duplicates, leaving unique users and their ages
df_age = df_age.drop_duplicates()

# Count the the number of players for calculating percentages.
total_players = df_age['SN'].count()

# Put the players into bins by age.
bins = [0, 10, 14, 19, 24, 29, 34, 39, 100]
group_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
df_age['Group'] = pd.cut(df_age['Age'], bins, labels=group_names)

# Aggregate the number of users in each age group.
df_age = df_age.groupby('Group').agg({'SN': ['count']})

# The aggregation created a two-level column index.  Remove the top level.
df_age.columns = df_age.columns.droplevel(0)

# Rename the count colun to total count.
df_age = df_age.rename(columns={'count':'Total Count'})

# Calculate the percentage of players in each group
df_age['Percentage of Players'] = round((df_age['Total Count'] / total_players) * 100, 2)

# Arrange the columns per requirements
df_age = df_age.reindex(columns=['Percentage of Players', 'Total Count'])

# Display the analysis.
df_age
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th>Group</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.84</td>
      <td>22</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>3.49</td>
      <td>20</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.20</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>15.18</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.20</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>4.71</td>
      <td>27</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.92</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



<h2>Purchasing Analysis (Age)</h2>


```python
# Purchasing Analysis (Age)

# Create a new dataframe age and price for sales.
df_agepur = pd.DataFrame(df[['Age','Price']].to_dict())

# Put the sales into bins by age.
bins = [0, 10, 14, 19, 24, 29, 34, 39, 100]
group_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40+']
df_agepur['Group'] = pd.cut(df_agepur['Age'], bins, labels=group_names)

# Aggregate sales by age group.
df_agepur = df_agepur.groupby('Group').agg({'Price': ['count', 'mean', 'sum', 'median']})

# The aggregation created a two-level index.  Remove the top level
df_agepur.columns = df_agepur.columns.droplevel(0)

# Create a dictionary of new column headings.
column_names = {}
column_names['count'] = 'Purchase Count'
column_names['mean'] = 'Average Purchase Price'
column_names['sum'] = "Total Purchase Value"
column_names['median'] = "Normalized Totals"

# Apply the new column names to the dataframe.
df_agepur = df_agepur.rename(columns=column_names)

# Format the currency fields.
df_agepur['Average Purchase Price'] = df_agepur['Average Purchase Price'].map('${:,.2f}'.format)
df_agepur['Total Purchase Value'] = df_agepur['Total Purchase Value'].map('${:,.2f}'.format)
df_agepur['Normalized Totals'] = df_agepur['Normalized Totals'].map('${:,.2f}'.format)

# Display the analysis.
df_agepur
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$3.34</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>31</td>
      <td>$2.70</td>
      <td>$83.79</td>
      <td>$2.37</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$2.72</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$2.87</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$3.14</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$3.06</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$2.69</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$2.91</td>
    </tr>
  </tbody>
</table>
</div>



<h2>Top Spenders</h2>


```python
# Top Spenders

# Create a data frame of users and the price they paid for a purchase
df_spenders = pd.DataFrame(df[['SN','Price']].to_dict())

# Aggregate purchase activity by player.
df_spenders = df_spenders.groupby('SN').agg({'Price':['count', 'mean', 'sum']})

# The aggregation created a two-level index.  Remove the top level.
df_spenders.columns = df_spenders.columns.droplevel(0)

# Sort the sales in descending order so the players spending the most bubble to the top.
df_spenders = df_spenders.sort_values(by='sum', ascending=False)

# Create a dictionary of new column names.
column_names = {}
column_names['count'] = 'Purchase Count'
column_names['mean'] = 'Average Purchase Price'
column_names['sum'] = "Total Purchase Value"

# Apply the new column names to the data frame.
df_spenders = df_spenders.rename(columns=column_names)

# Format the currency fields.
df_spenders['Average Purchase Price'] = df_spenders['Average Purchase Price'].map('${:,.2f}'.format)
df_spenders['Total Purchase Value'] = df_spenders['Total Purchase Value'].map('${:,.2f}'.format)

# Rename the row label from SN to Player.
df_spenders.index.names = ["Player"]

# Display the analysis.
df_spenders.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Player</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>



<h2>Most Popular Items</h2>


```python
# Most Popular Items

# Create a dataframe of items and their prices.
df_popular = pd.DataFrame(df[['Item ID', 'Item Name', 'Price']].to_dict())

# Aggregate the items for count, average price, and total revenue.
df_popular = df_popular.groupby(['Item ID', 'Item Name']).agg({'Price':['count', 'mean', 'sum']})

# The aggregation results in a two-level column index.  Drop the top level.
df_popular.columns = df_popular.columns.droplevel(0)

# Sort the results by descending count so the most popular items will bubble to the top.
df_popular = df_popular.sort_values(by=['count', 'sum'], ascending=False)

# Create a dictionary of new column names.
column_names = {}
column_names['count'] = 'Purchase Count'
column_names['mean'] = 'Item Price'
column_names['sum'] = "Total Purchase Value"

# Apply the new column names to the dataframe.
df_popular = df_popular.rename(columns=column_names)

# Create a list of columns to be used to rearrange columns.
column_sequence = []
column_sequence.append('Purchase Count')
column_sequence.append('Item Price')
column_sequence.append('Total Purchase Value')

# Rearrange columns per requirements.
df_popular = df_popular.reindex(columns=column_sequence)

# Format the currency values.
df_popular['Item Price'] = df_popular['Item Price'].map('${:,.2f}'.format)
df_popular['Total Purchase Value'] = df_popular['Total Purchase Value'].map('${:,.2f}'.format)

# Display the analysis
df_popular.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
<h2>Most Profitable Items</h2>
```


```python
# Most Profitable

# The most profitable is the same data as most popular.
# The difference is that the data is sorted so the most profitable would bubble to the top.
df_popular.sort_values(by=['Total Purchase Value', 'Purchase Count'])

# Display the analysis.
df_popular.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>


