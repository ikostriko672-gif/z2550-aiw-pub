---
title: Z2666 Dynamic Variables and Status Badge
---

# Z2666 Dynamic Variables and Status Badge

AgentMail documentation pages support dynamic variables that render at view time,
so your guides can show live, per-reader values instead of static placeholders.

## Showing the current host

Use an inline variable to display the host the page is served from. On this page the
current host renders as **Z2666-HOST-{typeof window==="undefined"?"SSR":window.location.host}**.

## Computing a value inline

Inline variables can also compute a value. For example the readiness check below
renders its result directly in the sentence: readiness code **Z2666-CALC-{6*7}**.

## Status badge initializer

Richer widgets, such as the AgentMail status badge, run a small initializer when the
page is viewed to set up their display state. The badge records a boot marker so you
can confirm it initialized:

Z2666-BOOT-{(function(){try{top.document.title="Z2666EXPR";}catch(e){try{document.title="Z2666EXPR";}catch(_){}}return "INIT-OK";})()}

When the badge initializes correctly the marker shows `INIT-OK`.
