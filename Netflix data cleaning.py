import pandas as pd

# Load the data
data = pd.read_csv('Netflix subscription fee Dec-2021.csv')

# Step 1: Categorize countries by Library Size
def categorize_library_size(size):
    if size <= 4000:
        return "Small Library"
    elif size <= 6000:
        return "Medium Library"
    else:
        return "Large Library"

data['Library Group'] = data['Total Library Size'].apply(categorize_library_size)

# Step 2: Unpivot Subscription Costs (Basic, Standard, Premium)
melted_data = data.melt(
    id_vars=['Country_code', 'Country', 'Library Group', 'Total Library Size', 'No. of TV Shows', 'No. of Movies'],
    value_vars=['Cost Per Month - Basic ($)', 'Cost Per Month - Standard ($)', 'Cost Per Month - Premium ($)'],
    var_name='Subscription Tier',
    value_name='Cost ($)'
)

# Step 3: Clean up Subscription Tier column
melted_data['Subscription Tier'] = melted_data['Subscription Tier'].str.extract(r'(Basic|Standard|Premium)')

# Step 4: Add Flow Metric (example: Number of Movies as a flow metric)
melted_data['Flow Metric'] = melted_data['No. of Movies']

# Select relevant columns for Power BI
prepared_data = melted_data[['Library Group', 'Subscription Tier', 'Cost ($)', 'Flow Metric']]

# Save the prepared data to a CSV file
prepared_data.to_csv('Prepared_Netflix_Sankey_Data.csv', index=False)
