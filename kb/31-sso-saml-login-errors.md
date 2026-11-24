---
doc_id: sso-saml-login-errors
title: Troubleshooting SAML SSO Login Errors
section: Troubleshooting
source_url: https://help.flowpulse.io/troubleshooting/saml-sso-errors
---
## Fixing Invalid ACS URL or Entity ID Errors
SAML 2.0 SSO (available on Enterprise) requires exact matching between your Identity Provider (Okta, Azure AD, OneLogin) and FlowPulse. Verify your Assertion Consumer Service (ACS) URL is set to `https://app.flowpulse.io/auth/saml/callback`.

## Expired X.509 Certificates
If SSO logins suddenly fail for all users with `SAML_CERT_EXPIRED`, an Admin must upload the renewed X.509 certificate under Settings > Security > SAML SSO.
