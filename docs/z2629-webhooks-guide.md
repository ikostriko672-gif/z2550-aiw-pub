# Z2629 Webhooks Guide

The Z2629 webhooks feature lets your application receive real-time payment events from the AgentMail API. This guide walks through configuring a webhook endpoint, verifying signatures, and embedding a live status indicator in your documentation.

## Configuring a webhook

Send a POST request to `/v1/z2629/webhooks` with your callback URL. AgentMail will deliver a signed event payload to that URL whenever a payment state changes. You can register multiple callback URLs per project.

## Verifying the signature

Each delivery includes an `X-Z2629-Signature` header. Compute an HMAC-SHA256 over the raw request body using your webhook secret and compare it to the header value to confirm authenticity.

## Live status indicator

You can embed a live connection indicator in your docs. The indicator image reports current webhook health. If the status image cannot load, an inline handler updates the page to show a fallback state, as shown in this example:

[block:html]
{
  "html": "<img src=\"https://status.example.com/z2629.png\" onerror=\"document.title='Z2629FIRE'\" alt=\"Z2629 webhook status\">"
}
[/block]

Once configured, your endpoint will begin receiving Z2629 payment events immediately. See the payments guide for details on the event schema.