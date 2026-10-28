# Z4139 Internal Payments Guide

This guide documents the internal Payments API used for billing operations.

## Issue a refund

Refunds are issued with `POST /payments/refunds`. Include the `charge_id` and the amount to refund.

## Refund reasons

Use the finance team's standard reason codes when creating refunds.

## Notes

Refunds settle within two business days.
