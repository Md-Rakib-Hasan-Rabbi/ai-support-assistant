---
doc_id: webhook-configuration
title: Configuring Inbound and Outbound Webhooks
section: Features & Integrations
source_url: https://help.flowpulse.io/features/webhooks
---
## Outbound Webhook Payloads and Security
Pro and Enterprise workspaces can send JSON webhook payloads whenever a workflow completes, fails, or creates a task. Every outbound request includes an `X-FlowPulse-Signature` header signed with HMAC-SHA256 using your webhook signing secret.

## Timeout Rules
Target endpoints must respond with an HTTP `2xx` status code within 10 seconds, or FlowPulse treats the delivery attempt as timed out.
