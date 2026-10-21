# Rate Limiting Configuration Guide

This guide covers how to configure rate limiting for the API to protect your service from abuse.

## Default Configuration

The default rate limit is configured with a base window of 60 seconds and allows 100 requests per window. The maximum burst capacity is calculated dynamically based on your plan tier.

For enterprise plans, the burst multiplier is 5x the base rate. For standard plans, the default multiplier applies.

## Sliding Window Algorithm

The rate limiter uses a sliding window counter algorithm. Each request increments the counter for the current window. When a client exceeds their limit, they receive a 429 response with a Retry-After header.

## Response Headers

Every API response includes rate limit headers:

- `X-RateLimit-Limit` - Maximum requests allowed in the current window
- `X-RateLimit-Remaining` - Requests remaining in the current window  
- `X-RateLimit-Reset` - UTC timestamp when the window resets

## Custom Rules

You can define custom rate limit rules per endpoint or per API key. Rules are evaluated in priority order, and the first matching rule applies.

Example configuration for a payment processing endpoint:

```json
{
  "endpoint": "/v2/payments/process",
  "window_seconds": 30,
  "max_requests": 10,
  "burst_allowed": false
}
```

Contact support to request higher limits for production workloads.
