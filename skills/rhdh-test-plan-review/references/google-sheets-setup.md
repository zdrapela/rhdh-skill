# Google Sheets API Setup

The skill accesses the RHDH schedule Google Sheet using your existing Google account via `gcloud`.

## Setup (one-time)

**Step 1: Install gcloud** (skip if already installed)

```bash
brew install --cask google-cloud-sdk
```

**Step 2: Authenticate with Google Drive access**

```bash
gcloud auth login --enable-gdrive-access
```

This opens a browser window. Sign in with the Google account that has access to the RHDH schedule sheet.

**Step 3: Verify**

```bash
python scripts/check_gsheets.py
```

Expected output:
```
✓ gcloud auth token available
```

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `gcloud not found` | Install with `brew install --cask google-cloud-sdk` |
| `No active gcloud account` | Run `gcloud auth login --enable-gdrive-access` |
| `403 Forbidden` when fetching sheet | Sign in with an account that has Viewer access to the sheet |
| Token expired | Run `gcloud auth login --enable-gdrive-access` again |
