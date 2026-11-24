---
doc_id: webhook-delivery-failures
title: Troubleshooting Webhook Delivery Failures
section: Troubleshooting
source_url: https://help.flowpulse.io/troubleshooting/webhook-failures
---
## Automatic Retry Schedule
When an outbound webhook fails (non-2xx HTTP status or 10-second timeout), FlowPulse automatically retries delivery up to 3 times at fixed intervals:
1. 1 minute after the initial failure
2. 5 minutes after the first retry
3. 30 minutes after the second retry

## Inspecting Delivery Logs
If all 3 retries fail, the delivery is marked `FAILED` in Developer > Webhook Logs, where you can inspect the full request headers, response body, and click "Replay Event" once your endpoint is fixed.
