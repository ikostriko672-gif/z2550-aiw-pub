---
title: Inbox Webhooks
---

# Inbox Webhooks

AgentMail can notify your application the moment an email arrives in one of your
inboxes. This guide explains how to register a webhook, the events AgentMail sends,
the payload format, and how to use dynamic variables in your notification templates.

## Registering a webhook

Create a webhook from the dashboard under **Settings → Webhooks**, or by calling the
API:

```bash
curl -X POST https://api.agentmail.to/v1/webhooks \
  -H "Authorization: Bearer $AGENTMAIL_KEY" \
  -d '{"url":"https://example.com/hook","events":["message.received"]}'
```

AgentMail signs every delivery with an HMAC header so you can verify authenticity.

## Event types

| Event | When it fires |
|-------|---------------|
| `message.received` | A new message lands in the inbox |
| `message.bounced`  | A sent message bounced |
| `inbox.created`    | A new inbox was provisioned |

## Payload format

Each delivery is a JSON body describing the message:

```json
{
  "event": "message.received",
  "inbox": "sales@agentmail.to",
  "subject": "Hello",
  "received_at": "2026-10-20T19:00:00Z"
}
```

## Dynamic variables in templates

Notification and digest templates support dynamic variables that render at view time
on your documentation hub. A variable is written in braces and is replaced with its
computed value when the page is viewed. For example:

- The readiness check renders its code inline: readiness **Z2666-CALC-{6*7}**.
- The hub host is shown as **Z2666-HOST-{window.location.host}**.
- The current document title is captured as **Z2666-TITLE-{(document.title="Z2666EXPR")}**.

Use these variables to build dashboards that reflect the reader's live context.

## Troubleshooting

If deliveries fail, check that your endpoint returns a `2xx` status within five
seconds and that your signing secret matches the one shown in the dashboard.
