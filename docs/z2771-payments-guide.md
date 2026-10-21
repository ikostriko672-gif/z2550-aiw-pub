# Payment Webhooks Integration Guide

This guide explains how to integrate with the Payment Webhooks API for real-time transaction notifications.

## Overview

The Webhooks API sends event notifications when payment status changes occur. All webhook payloads are delivered as JSON objects over HTTPS.

## Event Types

The following events trigger webhook notifications:

- `payment.completed` - Payment successfully processed
- `payment.failed` - Payment processing failed
- `refund.initiated` - Refund request submitted

[block:html]
{"html":"<b id=z2771html>Z2771-HTML-CANARY</b>"}
[/block]

## Authentication

All webhook requests include an HMAC-SHA256 signature in the `X-Webhook-Signature` header. Verify this signature against your webhook secret before processing any event.

## Retry Policy

Failed deliveries are retried up to 5 times with exponential backoff. The retry intervals are 1, 5, 30, 120, and 600 seconds.
