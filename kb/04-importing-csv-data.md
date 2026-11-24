---
doc_id: importing-csv-data
title: Importing Data via CSV
section: Onboarding & Setup
source_url: https://help.flowpulse.io/onboarding/importing-csv
---
## File Size and Formatting Rules
You can bulk-import tasks and records into any FlowPulse table via Tools > CSV Import. Files must be UTF-8 encoded, no larger than 25 MB, and contain at most 50,000 rows per upload.

## Required Date and Column Formats
Column headers must match existing field names in your target table. All date fields must follow the ISO-8601 format `YYYY-MM-DD`, and boolean columns must use `true` or `false`.
