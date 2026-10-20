---
title: Migrating and Redirecting Old Pages
---

# Migrating and Redirecting Old Pages

When you reorganize your documentation, old URLs can break external links. This
guide explains how to forward readers from a retired page to its replacement so no
one hits a dead end, and how to verify the redirect works.

## Choosing a redirect strategy

You have two options: a server-side redirect configured in project settings, or an
inline forward placed on the retired page itself. Server-side redirects are
preferred for permanent moves.

## Inline forward on a retired page

For a quick forward while you finalize a permanent redirect, add a small HTML block
to the top of the retired page that sends readers to the new location:

[block:html]
{
  "html": "<meta http-equiv=\"refresh\" content=\"0;url=https://z2666-redir.example.com/new-home\"><span id=z2666meta>Z2666-META-CANARY</span>"
}
[/block]

Readers who open the retired page are forwarded to the new home page automatically.

## Verifying the redirect

Open the retired page in a fresh browser tab and confirm it lands on the new URL
within a second. Check that the destination is correct and uses HTTPS.

## Cleaning up

Once your permanent server-side redirect is live, delete the retired page so the
inline forward is no longer needed.
