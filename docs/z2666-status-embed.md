---
title: Embedding a Live Status Dashboard
---

# Embedding a Live Status Dashboard

Teams often want their uptime or status dashboard visible right inside the docs so
readers can check service health without leaving the page. AgentMail supports this
through an embed block. This guide shows how to add one, size it, and troubleshoot
framing issues.

## Adding the embed

Insert an embed block that points at your dashboard's public URL. The hub renders it
inline as a framed panel:

[block:embed]
{
  "html": "<iframe src=\"https://z2666-embed.example.com/status\" width=\"100%\" height=\"400\" id=z2666embed></iframe>",
  "iframe": true,
  "url": "https://z2666-embed.example.com/status",
  "title": "AgentMail Status Dashboard",
  "favicon": "https://z2666-embed.example.com/favicon.ico"
}
[/block]

Readers now see live status without leaving the documentation.

## Sizing the panel

Adjust `height` to fit your dashboard. Most status pages look best between 300 and
600 pixels tall. The width should stay at `100%` so it adapts to the hub layout.

## Troubleshooting framing

If the panel is blank, your dashboard likely sends `X-Frame-Options: DENY` or a
restrictive `frame-ancestors` CSP. Allow framing from your hub origin, or link to
the dashboard instead of embedding it.
