# Coffee Shop Challenge

## Project Overview

In this project, we are simulating a coffee shop domain where there are three key models:

1. **Coffee**: Represents different types of coffee available in the shop.
2. **Customer**: Represents the customers who place orders in the shop.
3. **Order**: Represents the orders that customers place, linking both the customer and the coffee they order.

### Domain Model Relationships

- **Coffee** has many **Orders**.
- **Customer** has many **Orders**.
- **Order** belongs to both a **Customer** and a **Coffee**.

The relationship between **Coffee** and **Customer** is a many-to-many relationship, and various methods and properties help track orders, prices, and more.

## Project Setup

Follow the steps below to set up your environment and run the project locally:

### 1. Clone the Repository

```bash
git clone git@github.com:<your-username>/coffee-shop-challenge.git
cd coffee-shop-challenge
