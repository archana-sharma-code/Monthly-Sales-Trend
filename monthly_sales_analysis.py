import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the sales data
df = pd.read_csv('sales_data.csv')

# Convert Order Date to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract month and year for grouping
df['Year-Month'] = df['Order Date'].dt.to_period('M')

# Group by month and sum sales
monthly_sales = df.groupby('Year-Month')['Sales'].sum().reset_index()

# Convert period back to datetime for better display
monthly_sales['Year-Month'] = monthly_sales['Year-Month'].dt.to_timestamp()

# Sort chronologically
monthly_sales = monthly_sales.sort_values('Year-Month')

# Format the month column for display
monthly_sales['Month'] = monthly_sales['Year-Month'].dt.strftime('%B %Y')

# Display the monthly table
print("Monthly Sales Summary")
print("=" * 40)
print(monthly_sales[['Month', 'Sales']].to_string(index=False))
print("\n")

# Calculate total sales
total_sales = monthly_sales['Sales'].sum()
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Monthly Sales: ${total_sales/len(monthly_sales):,.2f}")
print(f"Highest Month: {monthly_sales.loc[monthly_sales['Sales'].idxmax(), 'Month']} (${monthly_sales['Sales'].max():,.2f})")
print(f"Lowest Month: {monthly_sales.loc[monthly_sales['Sales'].idxmin(), 'Month']} (${monthly_sales['Sales'].min():,.2f})")

# Create line chart
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['Year-Month'], monthly_sales['Sales'], 
         marker='o', linewidth=2, markersize=8, color='#2E86AB')

# Customize the chart
plt.title('Monthly Sales Trend', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)

# Format y-axis to show currency
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# Add data labels
for i, row in monthly_sales.iterrows():
    plt.annotate(f'${row["Sales"]:,.0f}', 
                 (row['Year-Month'], row['Sales']),
                 textcoords="offset points", 
                 xytext=(0,10), 
                 ha='center',
                 fontsize=9)

plt.tight_layout()
plt.savefig('monthly_sales_trend.png', dpi=300, bbox_inches='tight')
print("\nLine chart saved as 'monthly_sales_trend.png'")
plt.show()

# Save monthly table to CSV
monthly_sales[['Month', 'Sales']].to_csv('monthly_sales_table.csv', index=False)
print("Monthly table saved as 'monthly_sales_table.csv'")