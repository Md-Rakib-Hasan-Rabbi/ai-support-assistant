---
doc_id: api-rate-limits
title: REST API Rate Limits
section: Features & Integrations
source_url: https://help.flowpulse.io/features/api-rate-limits
---
## Requests Per Minute by Plan
API requests are rate-limited per workspace using a sliding 60-second window:
- Pro Plan: 120 requests per minute.
- Enterprise Plan: 600 requests per minute.
(Free and Starter plans do not include REST API access.)

## Handling 429 Rate Limit Responses
Exceeding your per-minute limit returns HTTP status `429 Too Many Requests` along with a `Retry-After` header indicating how many seconds to wait before retrying.
