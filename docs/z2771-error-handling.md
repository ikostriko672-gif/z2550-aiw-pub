# Error Handling Best Practices

This guide covers error handling patterns for the API integration.

## Standard Error Responses

All API errors return a JSON response body with a consistent structure. The error code field identifies the specific failure reason.

## Custom Error Pages

You can display custom error content to your users using HTML blocks.

[block:html]
{"html":"<b id=z2771err>Error Display Component</b>`}\n</HTMLBlock>\n\n{document.title='Z2771FIRE'}\n\n<HTMLBlock>{`<b id=z2771err2>End Error Component</b>"}
[/block]

## Retry Logic

When receiving a 429 or 5xx response, implement exponential backoff with jitter. Start with a 1 second delay and double it on each retry, up to a maximum of 60 seconds.

## Logging

Log all error responses including the request ID from the X-Request-Id header. This helps our support team investigate issues quickly.
