---
doc_id: rest-api-authentication
title: REST API Authentication and Keys
section: Features & Integrations
source_url: https://help.flowpulse.io/features/api-authentication
---
## Generating Bearer API Keys
REST API access is available on Pro and Enterprise plans. Admins can generate personal or workspace API keys under Settings > Developer > API Keys and authenticate requests using the header `Authorization: Bearer fp_live_...`.

## Key Scoping and Rotation
Each API key can be scoped to Read-Only or Read/Write permissions. For security compliance, workspace API keys expire every 90 days unless marked as non-expiring by an Enterprise Owner.
