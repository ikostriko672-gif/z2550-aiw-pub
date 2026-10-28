# Payments API — Refund Reference

The Payments API lets you refund a completed charge, partially or in full. Use this reference to issue refunds and track their settlement.

## Create a refund

Send a `POST` request to `/payments/refunds`:

```json
{
  "charge_id": "ch_123",
  "amount": 500,
  "reason": "customer_request"
}
```

A refund is created in `pending` state and settles within 1-2 business days.

## Refund statuses

- `pending` — accepted, awaiting settlement
- `succeeded` — funds returned to the customer
- `failed` — refund rejected by the card network

## Idempotency

Pass an `Idempotency-Key` header to safely retry a refund without creating duplicate refunds.
