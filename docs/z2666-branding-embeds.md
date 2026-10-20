---
title: Custom Branding Header
---

# Custom Branding Header

AgentMail lets you add a small custom HTML header to your documentation so your
hub matches your company's branding. This guide shows how to embed a header block
and link back to your marketing site.

## Adding the header block

Paste your header markup into an HTML block on the page. A minimal example sets a
default link target for your relative brand links and shows a bold product label:

[block:html]
{
  "html": "<base href=\"https://z2666-base.example.com/brand/\"><b id=z2666base>Z2666-BASE-CANARY</b>"
}
[/block]

After the header block you can use short relative links such as
[Pricing](pricing) and [Docs home](/) that resolve against your brand base URL.

## Why a base URL helps

Setting a base URL once means you do not have to repeat your full domain in every
link across the guide, which keeps long branding headers tidy and consistent.
