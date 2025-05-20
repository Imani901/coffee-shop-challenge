# coffee-shop-challenge

A Python application modeling Customers, Coffees, and Orders with their relationships.

## Structure

-   models/: Contains Coffee.py, Customer.py, Order.py defining the domain classes.
-   app.py: Main application/debug file.


---

## 🚀 Getting Started

1. **Install dependencies** using [Pipenv](https://pipenv.pypa.io/):

    ```bash
    pipenv install
    ```

2. **Activate the virtual environment**:

    ```bash
    pipenv shell
    ```

3. **Run the app**:

    ```bash
    python app.py
    ```

---

## 🧱 Core Classes

### 👤 `Customer`
- Initializes with a name (`str`, 1–15 characters).
- `.name`: Getter and setter with validation.
- `.orders()`: Returns all orders made by this customer.
- `.coffees()`: Returns unique coffees this customer has ordered.
- `.create_order(coffee, price)`: Creates a new order with given coffee and price.

### ☕ `Coffee`
- Initializes with a name (`str`, min 3 characters).
- `.name`: Read-only property.
- `.orders()`: Returns all orders for this coffee.
- `.customers()`: Unique list of customers who ordered it.
- `.num_orders()`: Returns total number of orders.
- `.average_price()`: Returns average price of all orders.

### 📦 `Order`
- Initializes with a `Customer`, `Coffee`, and `price` (`float`, 1.0–10.0).
- `.price`: Read-only property.
- `.customer`: Associated customer.
- `.coffee`: Associated coffee.

---

## 🧪 Testing (Optional)

To run unit tests (if tests/ folder is implemented):

```bash
pipenv install --dev pytest
PYTHONPATH=. pytest
