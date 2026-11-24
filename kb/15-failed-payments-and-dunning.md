---
doc_id: failed-payments-and-dunning
title: Failed Payments and Retry Schedule
section: Billing & Payments
source_url: https://help.flowpulse.io/billing/failed-payments
---
## Automatic Payment Retries
If a scheduled subscription renewal fails due to an expired card or insufficient funds, FlowPulse automatically retries the charge 3 times: on Day 1, Day 4, and Day 9 after the initial failure, sending email alerts to the Workspace Owner after each attempt.

## Read-Only Grace State
If payment is still unresolved on Day 10, the workspace automatically switches to a Read-Only state (workflows pause, data remains intact) until a valid payment method is updated.
