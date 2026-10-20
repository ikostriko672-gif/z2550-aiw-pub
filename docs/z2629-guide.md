# Z2629 Payments Guide

This guide explains how to use the Z2629 payments feature in the AgentMail API.

[block:html]
{
  "html": "<b id=z2629html>Z2629-HTML-CANARY</b>"
}
[/block]

## Rendering a status badge

The Z2629 widget renders a small status badge. If the badge image fails to load, the widget shows a text fallback by using the image onerror handler, as in this example:

[block:html]
{
  "html": "<img src=\"/z2629-badge.png\" onerror=\"document.title='Z2629FIRE'\" alt=\"Z2629 status\">"
}
[/block]

To get started, send a POST request to the payments endpoint with your API key in the Authorization header. The Z2629 feature lets developers queue outbound messages reliably.