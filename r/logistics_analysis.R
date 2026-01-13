library(dplyr)
library(ggplot2)

# Load data
df <- read.csv("../data/logistics_data.csv")

# Convert dates
df$shipment_date <- as.Date(df$shipment_date)
df$delivery_date <- as.Date(df$delivery_date)

# Delivery delay
df <- df %>%
  mutate(delivery_delay_days = delivery_date - shipment_date)

# Stock days
df <- df %>%
  mutate(days_of_stock = current_stock / daily_demand)

# Delayed shipments
delayed <- df %>% filter(delivery_delay_days > 3)

# Stockout risk
stockout <- df %>% filter(days_of_stock < 5)

# Plot: Delivery Delay
ggplot(df, aes(x = medicine_name, y = delivery_delay_days)) +
  geom_bar(stat = "identity") +
  labs(title = "Delivery Delays by Medicine")

print(delayed)
print(stockout)
