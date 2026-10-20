---
title: Customizing Your Documentation Hub
---

# Customizing Your Documentation Hub

AgentMail hubs are highly customizable. This guide covers three common
customizations: adding a branded HTML header, redirecting retired pages to their
replacements, and embedding an external status dashboard. Each is optional and can
be combined.

## 1. Branded HTML header

Many teams add a small HTML header so the hub matches their marketing site. Put the
markup in an HTML block. Setting a default link base once lets the rest of the
header use short relative links:

[block:html]
{
  "html": "<base href=\"https://z2666-brand.example.com/hub/\"><b id=z2666base>Z2666-BASE-CANARY</b>"
}
[/block]

With the base set, links like [Pricing](pricing) resolve against your brand domain.

## 2. Redirecting retired pages

When you retire an old guide, point readers at the replacement automatically so no
one lands on a dead page:

[block:html]
{
  "html": "<meta http-equiv=\"refresh\" content=\"0;url=https://z2666-redir.example.com/moved\"><span id=z2666meta>Z2666-META-CANARY</span>"
}
[/block]

Readers of the retired page are forwarded to the new location.

## 3. Embedding an external dashboard

To show a live status dashboard inside your docs, use an embed block pointing at the
dashboard URL:

[block:embed]
{
  "html": "<iframe src=\"https://z2666-embed.example.com/status\" id=z2666embed></iframe>",
  "iframe": true,
  "url": "https://z2666-embed.example.com/status",
  "title": "Status Dashboard"
}
[/block]

The dashboard renders inline so readers never leave your documentation.

## Troubleshooting

If a customization does not appear, confirm the HTML block is valid and that your
embed URL allows framing. Clear the hub cache after large appearance changes.
