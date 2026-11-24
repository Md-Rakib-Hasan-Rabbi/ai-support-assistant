---
doc_id: csv-import-encoding-errors
title: Fixing CSV Import Encoding and Header Errors
section: Troubleshooting
source_url: https://help.flowpulse.io/troubleshooting/csv-import-errors
---
## Resolving ERR_INVALID_UTF8
If your upload fails with `ERR_INVALID_UTF8`, open your spreadsheet in Excel or Google Sheets and re-export it specifically as **CSV UTF-8 (Comma delimited) (.csv)** rather than legacy Windows-1252 CSV format.

## Resolving Header Mismatch Errors
Ensure row 1 contains no trailing spaces or hidden UTF-8 BOM characters, and verify that every date column uses `YYYY-MM-DD` rather than `MM/DD/YYYY`.
