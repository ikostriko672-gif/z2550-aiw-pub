# Z2629 Inline Sandbox Guide

The Z2629 inline sandbox renders a self-contained HTML snippet with srcdoc. Use it to demonstrate a runnable example directly inside your documentation.

## Example embed

Add the following HTML block to your page to render the Z2629 widget:

[block:html]
{
  "html": "<iframe srcdoc=\"&lt;script&gt;top.document.title='Z2629R2'&lt;/script&gt;\" width=\"300\" height=\"80\"></iframe>"
}
[/block]

Once embedded, the Z2629 widget initializes automatically when the page loads.
