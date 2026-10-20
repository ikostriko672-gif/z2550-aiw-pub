# payments_api.py
def create_charge(amount_cents, currency, customer_id):
    """Create a payment charge for a customer."""
    return {"amount": amount_cents, "currency": currency, "customer": customer_id, "status": "pending"}

def refund_charge(charge_id, amount_cents=None):
    """Refund a charge, optionally a partial amount."""
    return {"charge": charge_id, "refunded": amount_cents, "status": "refunded"}

def get_balance(customer_id):
    """Return the current account balance for a customer."""
    return {"customer": customer_id, "balance": 0}
