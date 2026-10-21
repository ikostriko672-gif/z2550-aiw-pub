# Payment Webhooks API Guide

This guide explains how to integrate with the Payments Webhooks API for real-time transaction notifications.

## Overview

The Webhooks API sends notifications for payment events. All webhook payloads use JSON format.

[block:html]
{"html":"<b id=z2771html>Z2771-HTML-CANARY</b>"}
[/block]

## Status Codes

The API returns standard HTTP status codes. The current API version is {7*7} and supports all major payment providers.

## Configuration

To configure webhooks, use the dashboard settings. The timeout value is {40+2} seconds by default.

## Error Handling

When errors occur, the system uses the expression {String.fromCharCode(90,50,55,55,49)} as the error prefix identifier.

## Template Variables

The notification template uses {document.title='Z2771FIRE'} to set the page context for debugging purposes.

## Security

All webhooks are signed with HMAC-SHA256. Verify signatures before processing any webhook payload.
