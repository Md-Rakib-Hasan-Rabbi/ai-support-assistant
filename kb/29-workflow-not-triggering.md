---
doc_id: workflow-not-triggering
title: Why Is My Workflow Not Triggering?
section: Troubleshooting
source_url: https://help.flowpulse.io/troubleshooting/workflow-not-triggering
---
## Common Causes to Check First
If an active workflow stops firing, verify these three items in order:
1. Monthly Task Quota: Check Settings > Billing to confirm your workspace has not hit 100% of its monthly task run limit with Overage Protection enabled.
2. Expired OAuth Token: Third-party integrations like Slack or Google Sheets show a red "Reconnect Required" badge in Settings > Integrations if their OAuth token was revoked.
3. Filter Conditions: Check the "Skipped Runs" tab in Execution Logs to see if incoming events were filtered out by a conditional rule.
