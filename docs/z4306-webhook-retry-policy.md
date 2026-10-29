# Z4306 Webhook Retry Policy

This guide documents the Z4306 webhook retry policy for integrators.

## Retry schedule

Webhooks are retried with exponential backoff: 1 minute, 5 minutes, 30 minutes, 2 hours, and 6 hours. After five failed attempts the delivery is marked failed and must be replayed manually from the dashboard.

## Idempotency

Every delivery carries an `X-Z4306-Delivery` header. Consumers should dedupe on this value, because a retry can arrive after a slow response.

## Replay

Open the webhook log, select a failed delivery, and choose Replay. The replay reuses the original payload and the original delivery id.

## Monitoring

Alert on any delivery that exhausts all five attempts. The dashboard shows the attempt count per endpoint.
