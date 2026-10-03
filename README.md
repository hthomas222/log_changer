# Log File Parser & Modifier CLI

A Python command-line utility built with that scans log files to extract, inspect, and replace IP addresses and PIDs.

## Features

- **IP Viewer & Replacer**: Extract all unique IPv4 addresses from a log file or search-and-replace specific IP addresses.
- **PID Viewer & Replacer**: Extract process IDs (4-digit numeric patterns) formatted in a multi-column grid, or search-and-replace specific PIDs across the log file.
- **Terminal UI**: Uses Rich for colored outputs, formatted tables, and readable option menus.

---

## Prerequisites

- **Python 3.6+**
- `rich`

Install dependencies:

```bash
pip install rich
```
