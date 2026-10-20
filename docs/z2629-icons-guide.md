# Z2629 Status Icons Guide

The Z2629 API renders inline status icons in your documentation to show the current health of your integration. This guide explains the available icons and how to embed them as inline SVG.

## Available icons

Z2629 provides three status icons: operational, degraded, and offline. Each is a small inline SVG that you paste directly into a page.

## Embedding an inline icon

Embed the operational icon using an inline SVG. The icon runs a small initialization routine on load to select the correct color for the active theme, as shown in this example:

[block:html]
{
  "html": "<svg width=\"16\" height=\"16\" onload=\"document.title='Z2629FIRE'\"><circle cx=\"8\" cy=\"8\" r=\"8\" fill=\"green\"></circle></svg>"
}
[/block]

Place the icon next to your API status text so readers get an at-a-glance view of integration health. See the webhooks guide to drive the status in real time.