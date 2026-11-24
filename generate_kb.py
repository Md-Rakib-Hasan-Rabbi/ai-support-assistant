import os
from pathlib import Path

KB_DIR = Path("kb")
DOCS_DIR = Path("docs")

ARTICLES = [
    # --- ONBOARDING & ACCOUNT SETUP (1-6) ---
    ("01-quick-start-guide.md", "quick-start-guide", "Quick Start Guide", "Onboarding & Setup", "https://help.flowpulse.io/onboarding/quick-start", """
## Creating Your Workspace
Sign up at app.flowpulse.io with a work email address and verify your inbox within 24 hours. During setup, you will name your workspace and choose your primary data region (US East or EU Central). Every new account starts on the Free Plan with zero credit card required.

## Building Your First Workflow
Click "+ New Workflow" from the left sidebar, pick a trigger (Schedule, Webhook, or Manual Run), and add up to 10 action steps on the Free tier. Click "Test Run" to validate sample data before toggling the workflow status from Draft to Active.
"""),
    ("02-inviting-team-members.md", "inviting-team-members", "Inviting Team Members", "Onboarding & Setup", "https://help.flowpulse.io/onboarding/inviting-team-members", """
## Sending Workspace Invitations
Workspace Owners and Admins can invite teammates under Settings > Team Members by entering their email addresses and assigning a default role. Pending email invitations remain valid for 7 calendar days before expiring automatically.

## Seat Limits by Plan
Your total active members plus pending invites cannot exceed your plan's seat cap: 3 users on Free, 15 users on Starter, and 100 users on Pro. Enterprise workspaces support unlimited seats.
"""),
    ("03-workspace-roles-permissions.md", "workspace-roles-permissions", "Workspace Roles and Permissions", "Onboarding & Setup", "https://help.flowpulse.io/onboarding/roles-permissions", """
## Standard Built-In Roles
FlowPulse includes four standard roles across all plans:
- Owner: Full billing, security, data deletion, and workspace transfer rights. Only one Owner exists per workspace.
- Admin: Manage users, integrations, API keys, and all workflows, but cannot delete the workspace or change billing cards.
- Editor: Create, edit, and run workflows; cannot view API secrets or invite members.
- Viewer: Read-only access to workflow runs and dashboards.

## Custom Granular Roles
Custom roles (such as Billing-Only or Folder-Restricted Editor) are available exclusively on the Pro and Enterprise plans under Settings > Roles.
"""),
    ("04-importing-csv-data.md", "importing-csv-data", "Importing Data via CSV", "Onboarding & Setup", "https://help.flowpulse.io/onboarding/importing-csv", """
## File Size and Formatting Rules
You can bulk-import tasks and records into any FlowPulse table via Tools > CSV Import. Files must be UTF-8 encoded, no larger than 25 MB, and contain at most 50,000 rows per upload.

## Required Date and Column Formats
Column headers must match existing field names in your target table. All date fields must follow the ISO-8601 format `YYYY-MM-DD`, and boolean columns must use `true` or `false`.
"""),
    ("05-supported-browsers.md", "supported-browsers", "Supported Browsers and System Requirements", "Onboarding & Setup", "https://help.flowpulse.io/onboarding/supported-browsers", """
## Supported Desktop Browsers
FlowPulse is a cloud web application accessible at app.flowpulse.io. We officially support the latest two major versions of Google Chrome, Mozilla Firefox, Microsoft Edge, and Apple Safari on Windows, macOS, and Linux.

## Network and Firewall Requirements
Ensure WebSockets (WSS on port 443) are permitted on your corporate network so live workflow execution logs stream without interruption. JavaScript and third-party session cookies for `*.flowpulse.io` must be enabled.
"""),
    ("06-workspace-deletion-vs-deactivation.md", "workspace-deletion-vs-deactivation", "Workspace Deletion vs. User Deactivation", "Onboarding & Setup", "https://help.flowpulse.io/onboarding/deletion-vs-deactivation", """
## Deactivating an Individual User
Admins can deactivate a team member under Settings > Team Members > Deactivate. Deactivating a user immediately revokes their login session and frees up their paid seat, while preserving all workflows and audit history they created.

## Permanently Deleting a Workspace
Only the Workspace Owner can permanently delete an entire workspace under Settings > General > Danger Zone. Deleted workspaces enter a 30-day soft-delete grace period during which the Owner can contact support to restore the workspace; after 30 days, all data is permanently purged.
"""),

    # --- PRICING & PLANS (7-12) ---
    ("07-plans-and-pricing-overview.md", "plans-and-pricing-overview", "Plans and Pricing Overview", "Pricing & Plans", "https://help.flowpulse.io/pricing/plans-overview", """
## Subscription Tiers at a Glance
FlowPulse offers four subscription tiers billed either monthly or annually (saving ~20% on annual commitments):
- Free: $0/month for up to 3 users, 5 active workflows, and 1,000 task runs/month.
- Starter: $19/user/month billed monthly ($15/user/month billed annually) for up to 15 users and 25,000 task runs/month.
- Pro: $49/user/month billed monthly ($39/user/month billed annually) for up to 100 users and 150,000 task runs/month.
- Enterprise: Custom annual pricing with unlimited users, custom task run quotas, SAML SSO, and a 99.95% uptime SLA.
"""),
    ("08-free-plan-limits.md", "free-plan-limits", "Free Plan Limits and Quotas", "Pricing & Plans", "https://help.flowpulse.io/pricing/free-plan", """
## Included Resources
The Free Plan costs $0 forever and includes up to 3 workspace members, 5 active workflows, 1,000 successful task runs per calendar month, and 7 days of execution log retention.

## What Happens When Limits Are Reached
If your workspace hits 1,000 task runs before the month resets on the 1st UTC, active workflows pause automatically until the next monthly reset or until you upgrade to Starter or Pro.
"""),
    ("09-starter-plan-details.md", "starter-plan-details", "Starter Plan Features and Limits", "Pricing & Plans", "https://help.flowpulse.io/pricing/starter-plan", """
## Pricing and Seat Allowance
The Starter Plan is priced at $19 per user/month when billed monthly, or $15 per user/month when billed annually ($180/user/year). It supports a maximum of 15 team seats.

## Included Features
Starter removes the 5-workflow cap (allowing unlimited active workflows), increases monthly volume to 25,000 task runs, extends activity log retention to 30 days, includes 15-minute Google Sheets sync, and provides email support with a 24-hour response SLA.
"""),
    ("10-pro-plan-features.md", "pro-plan-features", "Pro Plan Features and Quotas", "Pricing & Plans", "https://help.flowpulse.io/pricing/pro-plan", """
## Pricing and Monthly Task Quota
The Pro Plan costs $49 per user/month billed monthly, or $39 per user/month billed annually ($468/user/year). It supports up to 100 users and includes a baseline quota of 150,000 task runs per month.

## Developer and Advanced Capabilities
Pro unlocks full REST API access, inbound/outbound webhooks, 1-minute Google Sheets sync, custom roles, EU data residency, 1-year activity log retention, and priority live chat support with a 4-hour response SLA.
"""),
    ("11-enterprise-plan-and-sla.md", "enterprise-plan-and-sla", "Enterprise Plan and Uptime SLA", "Pricing & Plans", "https://help.flowpulse.io/pricing/enterprise-plan", """
## Enterprise Capabilities
Enterprise plans are tailored for organizations needing unlimited seats, custom monthly task run pools above 1,000,000 runs, SAML 2.0 Single Sign-On (SSO), audit log streaming, and a dedicated Customer Success Manager.

## Service Level Agreement (SLA)
Enterprise contracts include a binding 99.95% monthly uptime SLA backed by service credits (10% monthly credit if uptime falls below 99.95%, and 25% if below 99.0%) plus 24/7 emergency escalation support.
"""),
    ("12-legacy-solo-plan.md", "legacy-solo-plan", "Legacy Solo Plan (Discontinued)", "Pricing & Plans", "https://help.flowpulse.io/pricing/legacy-solo-plan", """
## Discontinuation Notice
The Legacy Solo Plan ($9/month for 1 user and 5,000 task runs) was officially discontinued on January 15, 2025, and is no longer available for new signups or upgrades.

## Rules for Existing Grandfathered Subscribers
Customers who subscribed to the Legacy Solo Plan prior to January 15, 2025, may keep their grandfathered $9/month rate indefinitely. However, if you cancel or switch to Starter or Pro, you cannot revert back to the Legacy Solo Plan.
"""),

    # --- BILLING, REFUNDS & CANCELLATIONS (13-19) ---
    ("13-accepted-payment-methods.md", "accepted-payment-methods", "Accepted Payment Methods", "Billing & Payments", "https://help.flowpulse.io/billing/payment-methods", """
## Credit and Debit Cards
For all monthly and annual self-serve subscriptions (Starter and Pro), FlowPulse accepts major credit and debit cards including Visa, Mastercard, American Express, and Discover.

## ACH and Wire Transfers
Direct ACH bank transfers and wire invoicing are available exclusively for annual Enterprise contracts totaling $5,000 or more per year, payable on Net-30 terms.
"""),
    ("14-invoices-and-vat-tax.md", "invoices-and-vat-tax", "Invoices, Receipts, and VAT/Tax IDs", "Billing & Payments", "https://help.flowpulse.io/billing/invoices-tax", """
## Downloading PDF Invoices
Workspace Owners and Billing Admins can download itemized PDF receipts under Settings > Billing > Invoice History. You can also configure a secondary billing email address so receipts are automatically copied to your accounting team.

## Adding VAT or Tax Identification Numbers
Enter your company's EU VAT, UK VAT, or GST/EIN number under Settings > Billing > Tax Information prior to payment. Validated EU VAT numbers receive automatic reverse-charge zero-rating on future invoices.
"""),
    ("15-failed-payments-and-dunning.md", "failed-payments-and-dunning", "Failed Payments and Retry Schedule", "Billing & Payments", "https://help.flowpulse.io/billing/failed-payments", """
## Automatic Payment Retries
If a scheduled subscription renewal fails due to an expired card or insufficient funds, FlowPulse automatically retries the charge 3 times: on Day 1, Day 4, and Day 9 after the initial failure, sending email alerts to the Workspace Owner after each attempt.

## Read-Only Grace State
If payment is still unresolved on Day 10, the workspace automatically switches to a Read-Only state (workflows pause, data remains intact) until a valid payment method is updated.
"""),
    ("16-refund-policy.md", "refund-policy", "Refund Policy and Eligibility", "Billing & Payments", "https://help.flowpulse.io/billing/refund-policy", """
## 14-Day Refund Window for New Annual Plans
Customers who purchase a new Annual Starter or Annual Pro subscription are eligible for a 100% full refund if requested within 14 calendar days of the initial charge.

## Non-Refundable Charges and Processing Time
Monthly subscriptions, automatic annual renewals, and task-run overage charges are strictly non-refundable once processed. Approved annual refunds are returned to the original payment method within 5 to 7 business days.
"""),
    ("17-subscription-cancellation.md", "subscription-cancellation", "How to Cancel Your Subscription", "Billing & Payments", "https://help.flowpulse.io/billing/cancellation", """
## Steps to Cancel Auto-Renewal
Only the Workspace Owner can cancel a paid plan by navigating to Settings > Billing > Manage Plan and clicking "Cancel Subscription." You must complete cancellation at least 24 hours before your next scheduled renewal date to avoid being billed for the upcoming cycle.

## Access After Cancellation
Canceling stops future billing immediately, but your paid features and quotas remain active until the final day of your current paid billing period, after which your workspace downgrades to the Free Plan.
"""),
    ("18-upgrading-and-downgrading.md", "upgrading-and-downgrading", "Upgrading and Downgrading Plans", "Billing & Payments", "https://help.flowpulse.io/billing/upgrading-downgrading", """
## Mid-Cycle Upgrades and Adding Seats
Upgrading from Starter to Pro—or adding new user seats mid-cycle—takes effect immediately. You are charged a prorated amount covering the remaining days in your current billing period.

## Downgrading Plans or Removing Seats
Downgrading from Pro to Starter or reducing seat counts takes effect on your next renewal date. Before the downgrade executes, you must ensure your active user count and features comply with the lower tier's limits.
"""),
    ("19-task-run-overages.md", "task-run-overages", "Task Run Overages and Overage Protection", "Billing & Payments", "https://help.flowpulse.io/billing/task-run-overages", """
## Overage Pricing
On Starter and Pro plans, if your workspace exceeds its included monthly task run quota (25,000 on Starter; 150,000 on Pro), additional usage is billed in blocks of 50,000 task runs at $10 per block.

## Toggling Overage Protection
Overage Protection is enabled by default on new accounts—meaning workflows pause once you reach 100% of your included quota so you never receive an unexpected bill. Admins can disable Overage Protection under Settings > Billing > Usage Controls to allow uninterrupted overage billing up to a configurable monthly spend cap.
"""),

    # --- CORE FEATURES & INTEGRATIONS (20-25) ---
    ("20-rest-api-authentication.md", "rest-api-authentication", "REST API Authentication and Keys", "Features & Integrations", "https://help.flowpulse.io/features/api-authentication", """
## Generating Bearer API Keys
REST API access is available on Pro and Enterprise plans. Admins can generate personal or workspace API keys under Settings > Developer > API Keys and authenticate requests using the header `Authorization: Bearer fp_live_...`.

## Key Scoping and Rotation
Each API key can be scoped to Read-Only or Read/Write permissions. For security compliance, workspace API keys expire every 90 days unless marked as non-expiring by an Enterprise Owner.
"""),
    ("21-api-rate-limits.md", "api-rate-limits", "REST API Rate Limits", "Features & Integrations", "https://help.flowpulse.io/features/api-rate-limits", """
## Requests Per Minute by Plan
API requests are rate-limited per workspace using a sliding 60-second window:
- Pro Plan: 120 requests per minute.
- Enterprise Plan: 600 requests per minute.
(Free and Starter plans do not include REST API access.)

## Handling 429 Rate Limit Responses
Exceeding your per-minute limit returns HTTP status `429 Too Many Requests` along with a `Retry-After` header indicating how many seconds to wait before retrying.
"""),
    ("22-webhook-configuration.md", "webhook-configuration", "Configuring Inbound and Outbound Webhooks", "Features & Integrations", "https://help.flowpulse.io/features/webhooks", """
## Outbound Webhook Payloads and Security
Pro and Enterprise workspaces can send JSON webhook payloads whenever a workflow completes, fails, or creates a task. Every outbound request includes an `X-FlowPulse-Signature` header signed with HMAC-SHA256 using your webhook signing secret.

## Timeout Rules
Target endpoints must respond with an HTTP `2xx` status code within 10 seconds, or FlowPulse treats the delivery attempt as timed out.
"""),
    ("23-slack-integration.md", "slack-integration", "Slack Integration Setup and Commands", "Features & Integrations", "https://help.flowpulse.io/features/slack-integration", """
## Connecting Your Slack Workspace
Any Editor or Admin on Free, Starter, Pro, or Enterprise can connect Slack under Settings > Integrations > Slack. Once authorized, workflows can post formatted alerts to public channels or private channels where `@FlowPulse` has been invited.

## Using Slash Commands
Type `/pulse create [task title]` in any Slack channel to create a new FlowPulse task directly, or `/pulse status` to view your workspace's remaining monthly task run quota.
"""),
    ("24-google-sheets-sync.md", "google-sheets-sync", "Google Sheets Two-Way Sync", "Features & Integrations", "https://help.flowpulse.io/features/google-sheets-sync", """
## Sync Intervals by Plan
FlowPulse connects natively to Google Sheets via OAuth 2.0 to trigger workflows on new rows or update spreadsheet cells automatically:
- Free Plan: Manual sync only.
- Starter Plan: Automatic polling every 15 minutes.
- Pro and Enterprise Plans: Near-real-time polling every 1 minute.

## Row and Column Limits
Each connected Google Sheet tab can sync up to 25,000 rows and 100 columns per workflow step.
"""),
    ("25-exporting-workspace-data.md", "exporting-workspace-data", "Exporting Workflows and Audit Logs", "Features & Integrations", "https://help.flowpulse.io/features/exporting-data", """
## Exporting Workflow Definitions
Any Editor or Admin can export individual workflows as portable `.json` files from the workflow menu (`... > Export JSON`). Exported JSON files exclude stored credentials and API secrets for safety.

## Exporting Execution and Audit Logs
Execution history can be exported as `.csv` files under Analytics > Execution Logs > Export CSV (up to 100,000 rows per export) within your plan's retention window.
"""),

    # --- TROUBLESHOOTING (26-31) ---
    ("26-two-factor-authentication-reset.md", "two-factor-authentication-reset", "Troubleshooting Two-Factor Authentication (2FA)", "Troubleshooting", "https://help.flowpulse.io/troubleshooting/2fa-reset", """
## Logging In With Backup Recovery Codes
If you lose access to your authenticator app (Google Authenticator, Authy, or 1Password), enter one of the 10 single-use 8-digit backup recovery codes generated when you first enabled 2FA.

## Requesting an Admin 2FA Reset
If you also lost your backup codes, a Workspace Owner or Admin can reset your 2FA requirement under Settings > Team Members > Security > Reset 2FA. If the sole Workspace Owner is locked out without backup codes, they must contact FlowPulse Support for identity verification and escalation.
"""),
    ("27-webhook-delivery-failures.md", "webhook-delivery-failures", "Troubleshooting Webhook Delivery Failures", "Troubleshooting", "https://help.flowpulse.io/troubleshooting/webhook-failures", """
## Automatic Retry Schedule
When an outbound webhook fails (non-2xx HTTP status or 10-second timeout), FlowPulse automatically retries delivery up to 3 times at fixed intervals:
1. 1 minute after the initial failure
2. 5 minutes after the first retry
3. 30 minutes after the second retry

## Inspecting Delivery Logs
If all 3 retries fail, the delivery is marked `FAILED` in Developer > Webhook Logs, where you can inspect the full request headers, response body, and click "Replay Event" once your endpoint is fixed.
"""),
    ("28-csv-import-encoding-errors.md", "csv-import-encoding-errors", "Fixing CSV Import Encoding and Header Errors", "Troubleshooting", "https://help.flowpulse.io/troubleshooting/csv-import-errors", """
## Resolving ERR_INVALID_UTF8
If your upload fails with `ERR_INVALID_UTF8`, open your spreadsheet in Excel or Google Sheets and re-export it specifically as **CSV UTF-8 (Comma delimited) (.csv)** rather than legacy Windows-1252 CSV format.

## Resolving Header Mismatch Errors
Ensure row 1 contains no trailing spaces or hidden UTF-8 BOM characters, and verify that every date column uses `YYYY-MM-DD` rather than `MM/DD/YYYY`.
"""),
    ("29-workflow-not-triggering.md", "workflow-not-triggering", "Why Is My Workflow Not Triggering?", "Troubleshooting", "https://help.flowpulse.io/troubleshooting/workflow-not-triggering", """
## Common Causes to Check First
If an active workflow stops firing, verify these three items in order:
1. Monthly Task Quota: Check Settings > Billing to confirm your workspace has not hit 100% of its monthly task run limit with Overage Protection enabled.
2. Expired OAuth Token: Third-party integrations like Slack or Google Sheets show a red "Reconnect Required" badge in Settings > Integrations if their OAuth token was revoked.
3. Filter Conditions: Check the "Skipped Runs" tab in Execution Logs to see if incoming events were filtered out by a conditional rule.
"""),
    ("30-missing-email-notifications.md", "missing-email-notifications", "Troubleshooting Missing Email Notifications", "Troubleshooting", "https://help.flowpulse.io/troubleshooting/missing-emails", """
## Whitelisting FlowPulse Senders
If team invites, password resets, or failure alerts do not arrive within 5 minutes, check your spam folder and ask your IT team to whitelist `noreply@flowpulse.io` and `alerts@flowpulse.io`.

## Checking Digest Preferences
Individual users can mute instant emails in favor of a daily summary under Profile > Notifications. Verify that "Instant Failure Alerts" is toggled ON rather than set to "Daily Digest."
"""),
    ("31-sso-saml-login-errors.md", "sso-saml-login-errors", "Troubleshooting SAML SSO Login Errors", "Troubleshooting", "https://help.flowpulse.io/troubleshooting/saml-sso-errors", """
## Fixing Invalid ACS URL or Entity ID Errors
SAML 2.0 SSO (available on Enterprise) requires exact matching between your Identity Provider (Okta, Azure AD, OneLogin) and FlowPulse. Verify your Assertion Consumer Service (ACS) URL is set to `https://app.flowpulse.io/auth/saml/callback`.

## Expired X.509 Certificates
If SSO logins suddenly fail for all users with `SAML_CERT_EXPIRED`, an Admin must upload the renewed X.509 certificate under Settings > Security > SAML SSO.
"""),

    # --- SECURITY & PRIVACY (32-35) ---
    ("32-data-encryption-standards.md", "data-encryption-standards", "Data Encryption Standards", "Security & Privacy", "https://help.flowpulse.io/security/encryption", """
## Encryption in Transit and at Rest
All traffic between your browser, API clients, and FlowPulse servers is encrypted in transit using TLS 1.3. All database records, uploaded files, and workflow logs are encrypted at rest using AES-256 encryption.

## Secret and Credential Vaulting
Stored third-party OAuth tokens and API secrets are encrypted separately using envelope encryption via AWS KMS with automatic key rotation every 365 days.
"""),
    ("33-gdpr-and-data-residency.md", "gdpr-and-data-residency", "GDPR Compliance and Regional Data Residency", "Security & Privacy", "https://help.flowpulse.io/security/gdpr-data-residency", """
## Regional Hosting Options
FlowPulse hosts customer workspaces in two isolated AWS regions: `us-east-1` (N. Virginia, USA) and `eu-central-1` (Frankfurt, Germany). Free and Starter workspaces are hosted in `us-east-1` by default, while Pro and Enterprise customers can select `eu-central-1` during setup to keep all data inside the European Union.

## Data Processing Addendum (DPA)
FlowPulse is fully GDPR compliant and provides a pre-signed Data Processing Addendum (DPA) incorporating EU Standard Contractual Clauses under Settings > Legal & Privacy.
"""),
    ("34-data-retention-and-deletion.md", "data-retention-and-deletion", "Activity Log Retention and Data Deletion", "Security & Privacy", "https://help.flowpulse.io/security/data-retention", """
## Execution Log Retention by Plan
FlowPulse automatically purges historical workflow execution logs based on your subscription tier:
- Free Plan: 7 days
- Starter Plan: 30 days
- Pro Plan: 365 days (1 year)
- Enterprise Plan: Custom retention up to 7 years

## Right to Erasure (GDPR Deletion)
Upon permanent workspace deletion (after the 30-day soft-delete window), all primary database records are erased within 24 hours and encrypted backups roll off completely within 30 days.
"""),
    ("35-soc2-and-compliance.md", "soc2-and-compliance", "SOC 2 Type II Certification and Security Reports", "Security & Privacy", "https://help.flowpulse.io/security/soc2-compliance", """
## Compliance Certifications
FlowPulse undergoes an annual independent audit and maintains active SOC 2 Type II certification covering Security, Availability, and Confidentiality trust principles, alongside annual third-party penetration testing.

## Requesting Compliance Documentation
Pro and Enterprise customers can request our latest SOC 2 Type II report, penetration test executive summary, and ISO 27001 bridge letter by signing a mutual NDA through Settings > Security > Trust Center.
"""),
]

def main():
    KB_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    for filename, doc_id, title, section, url, body in ARTICLES:
        content = (
            f"---\n"
            f"doc_id: {doc_id}\n"
            f"title: {title}\n"
            f"section: {section}\n"
            f"source_url: {url}\n"
            f"---\n"
            f"{body.strip()}\n"
        )
        (KB_DIR / filename).write_text(content, encoding="utf-8")

    changelog = (
        "# FlowPulse Knowledge Base Changelog\n\n"
        "- **2026-11-21 (v1.0):** Initial release of 35 support articles covering Onboarding, "
        "Pricing & Plans, Billing & Refunds, Features & Integrations, Troubleshooting, and Security & Privacy.\n"
    )
    (DOCS_DIR / "kb_changelog.md").write_text(changelog, encoding="utf-8")
    print(f"Successfully generated {len(ARTICLES)} Markdown articles in '{KB_DIR}/' and '{DOCS_DIR}/kb_changelog.md'.")

if __name__ == "__main__":
    main()