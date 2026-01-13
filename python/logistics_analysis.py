import pandas as pd

# Load data
df = pd.read_csv("../data/logistics_data.csv")

# Convert dates
df['shipment_date'] = pd.to_datetime(df['shipment_date'])
df['delivery_date'] = pd.to_datetime(df['delivery_date'])

# Calculate delivery delay
df['delivery_delay_days'] = (df['delivery_date'] - df['shipment_date']).dt.days

# Identify delayed shipments
delayed_shipments = df[df['delivery_delay_days'] > 3]

# Stockout risk (less than 5 days of stock)
df['days_of_stock'] = df['current_stock'] / df['daily_demand']
stockout_risk = df[df['days_of_stock'] < 5]

# Expiry risk
expiry_risk = df[df['expiry_days'] < 30]

print("🚚 Delayed Shipments:")
print(delayed_shipments[['shipment_id', 'delivery_delay_days']])

print("\n⚠️ Stockout Risk Pharmacies:")
print(stockout_risk[['pharmacy_id', 'medicine_name', 'days_of_stock']])

print("\n⏳ Expiry Risk Inventory:")
print(expiry_risk[['medicine_name', 'expiry_days']])
