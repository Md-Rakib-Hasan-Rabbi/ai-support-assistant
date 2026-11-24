---
doc_id: data-encryption-standards
title: Data Encryption Standards
section: Security & Privacy
source_url: https://help.flowpulse.io/security/encryption
---
## Encryption in Transit and at Rest
All traffic between your browser, API clients, and FlowPulse servers is encrypted in transit using TLS 1.3. All database records, uploaded files, and workflow logs are encrypted at rest using AES-256 encryption.

## Secret and Credential Vaulting
Stored third-party OAuth tokens and API secrets are encrypted separately using envelope encryption via AWS KMS with automatic key rotation every 365 days.
