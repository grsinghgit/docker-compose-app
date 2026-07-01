# 🔐 Docker Security Audit Report

# Report Summary

**Project:** compose-app (Python Flask + MySQL)  
**Scan Tool:** Trivy v0.72.0  
**Date:** 02 July 2026  
**Image:** compose-app-web:latest  

---

## 📊 Executive Summary

This security audit scanned the Docker image `compose-app-web:latest` for known vulnerabilities.

**Key Findings:**

- **Total Vulnerabilities Found:** 39
  - **CRITICAL:** 5 (Require immediate action)
  - **HIGH:** 34 (Should be addressed urgently)

**Top Critical Issues:**

1. **OpenSSL (CVE-2026-31789)** — Heap buffer overflow on 32-bit systems.  
   ➜ **Fix:** Update OpenSSL to version `3.5.5-1~deb13u2` or higher.

2. **Perl (CVE-2026-42496)** — Path traversal allows arbitrary file access.  
   ➜ **Fix:** Update Perl or remove if not required.

**Python Package Issues (Easier to Fix):**

1. **wheel (CVE-2026-24049)** — Privilege escalation via malicious wheel file.  
   ➜ **Fix:** Update `wheel` to `>= 0.46.2`

2. **jaraco.context (CVE-2026-23949)** — Path traversal via malicious tar archives.  
   ➜ **Fix:** Update `jaraco.context` to `>= 6.1.0`

---

## 🛠️ Recommended Actions

1. **Update Base Image** — Use `python:3.12-slim` instead of `python:3.9-slim` to get newer OpenSSL and system packages.
2. **Update Python Dependencies** — Run `pip install --upgrade wheel jaraco.context`
3. **Add Non-Root User** — In Dockerfile, add `RUN adduser appuser && USER appuser`
4. **Multi-stage Build** — Reduce image size and remove unnecessary build tools.

---

## 📋 Detailed Scan Report



┌──────────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┬─────────┐
│                                      Target                                      │    Type    │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ compose-app-web:latest (debian 13.1)                                             │   debian   │       36        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/blinker-1.9.0.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/click-8.1.8.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/flask-3.1.3.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/importlib_metadata-8.7.1.dist-info/METADA- │ python-pkg │        0        │    -    │
│ TA                                                                               │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/itsdangerous-2.2.0.dist-info/METADATA      │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/jinja2-3.1.6.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/markupsafe-3.0.3.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/mysql_connector_python-9.4.0.dist-info/ME- │ python-pkg │        0        │    -    │
│ TADATA                                                                           │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/pip-23.0.1.dist-info/METADATA              │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools-79.0.1.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/autocommand-2.2.2.dist- │ python-pkg │        0        │    -    │
│ -info/METADATA                                                                   │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/backports.tarfile-1.2.- │ python-pkg │        0        │    -    │
│ 0.dist-info/METADATA                                                             │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/importlib_metadata-8.0- │ python-pkg │        0        │    -    │
│ .0.dist-info/METADATA                                                            │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/inflect-7.3.1.dist-inf- │ python-pkg │        0        │    -    │
│ o/METADATA                                                                       │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/jaraco.collections-5.1- │ python-pkg │        0        │    -    │
│ .0.dist-info/METADATA                                                            │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/jaraco.context-5.3.0.d- │ python-pkg │        1        │    -    │
│ ist-info/METADATA                                                                │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/jaraco.functools-4.0.1- │ python-pkg │        0        │    -    │
│ .dist-info/METADATA                                                              │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/jaraco.text-3.12.1.dis- │ python-pkg │        0        │    -    │
│ t-info/METADATA                                                                  │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/more_itertools-10.3.0.- │ python-pkg │        0        │    -    │
│ dist-info/METADATA                                                               │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/packaging-24.2.dist-in- │ python-pkg │        0        │    -    │
│ fo/METADATA                                                                      │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/platformdirs-4.2.2.dis- │ python-pkg │        0        │    -    │
│ t-info/METADATA                                                                  │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/tomli-2.0.1.dist-info/- │ python-pkg │        0        │    -    │
│ METADATA                                                                         │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/typeguard-4.3.0.dist-i- │ python-pkg │        0        │    -    │
│ nfo/METADATA                                                                     │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/typing_extensions-4.12- │ python-pkg │        0        │    -    │
│ .2.dist-info/METADATA                                                            │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/wheel-0.45.1.dist-info- │ python-pkg │        1        │    -    │
│ /METADATA                                                                        │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/setuptools/_vendor/zipp-3.19.2.dist-info/- │ python-pkg │        0        │    -    │
│ METADATA                                                                         │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/werkzeug-3.1.8.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/wheel-0.45.1.dist-info/METADATA            │ python-pkg │        1        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.9/site-packages/zipp-3.23.1.dist-info/METADATA             │ python-pkg │        0        │    -    │
└──────────────────────────────────────────────────────────────────────────────────┴────────────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


compose-app-web:latest (debian 13.1)
====================================
Total: 36 (HIGH: 31, CRITICAL: 5)

┌─────────────────────────┬────────────────┬──────────┬──────────────┬───────────────────┬───────────────────┬──────────────────────────────────────────────────────────────┐
│         Library         │ Vulnerability  │ Severity │    Status    │ Installed Version │   Fixed Version   │                            Title                             │
├─────────────────────────┼────────────────┼──────────┼──────────────┼───────────────────┼───────────────────┼──────────────────────────────────────────────────────────────┤
│ libacl1                 │ CVE-2026-54369 │ HIGH     │ affected     │ 2.3.2-2+b1        │                   │ acl: Symlink traversal privilege escalation via libacl       │
│                         │                │          │              │                   │                   │ functions                                                    │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-54369                   │
├─────────────────────────┼────────────────┤          │              ├───────────────────┼───────────────────┼──────────────────────────────────────────────────────────────┤
│ libattr1                │ CVE-2026-54371 │          │              │ 1:2.5.2-3         │                   │ attr: Symlink Traversal Privilege Escalation via getfattr    │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-54371                   │
├─────────────────────────┼────────────────┤          ├──────────────┼───────────────────┼───────────────────┼──────────────────────────────────────────────────────────────┤
│ libcap2                 │ CVE-2026-4878  │          │ fixed        │ 1:2.75-10+b1      │ 1:2.75-10+deb13u1 │ libcap: libcap: Privilege escalation via TOCTOU race         │
│                         │                │          │              │                   │                   │ condition in cap_set_file()                                  │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-4878                    │
├─────────────────────────┼────────────────┤          ├──────────────┼───────────────────┼───────────────────┼──────────────────────────────────────────────────────────────┤
│ libncursesw6            │ CVE-2025-69720 │          │ affected     │ 6.5+20250216-2    │                   │ ncurses: ncurses: Buffer overflow vulnerability may lead to  │
│                         │                │          │              │                   │                   │ arbitrary code execution.                                    │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2025-69720                   │
├─────────────────────────┼────────────────┼──────────┼──────────────┼───────────────────┼───────────────────┼──────────────────────────────────────────────────────────────┤
│ libssl3t64              │ CVE-2026-31789 │ CRITICAL │ fixed        │ 3.5.1-1+deb13u1   │ 3.5.5-1~deb13u2   │ openssl: OpenSSL: Heap buffer overflow on 32-bit systems     │
│                         │                │          │              │                   │                   │ from large X.509 certificate...                              │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-31789                   │
│                         ├────────────────┼──────────┤              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2025-15467 │ HIGH     │              │                   │ 3.5.4-1~deb13u2   │ openssl: OpenSSL: Remote code execution or Denial of Service │
│                         │                │          │              │                   │                   │ via oversized Initialization...                              │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2025-15467                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2025-69421 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service via malformed PKCS#12    │
│                         │                │          │              │                   │                   │ file processing                                              │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2025-69421                   │
│                         ├────────────────┤          │              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28387 │          │              │                   │ 3.5.5-1~deb13u2   │ openssl: OpenSSL: Arbitrary code execution due to            │
│                         │                │          │              │                   │                   │ use-after-free in DANE TLSA authentication...                │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28387                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28388 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
│                         │                │          │              │                   │                   │ dereference in delta...                                      │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28388                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28389 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service vulnerability in CMS     │
│                         │                │          │              │                   │                   │ processing                                                   │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28389                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28390 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
│                         │                │          │              │                   │                   │ dereference in CMS...                                        │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28390                   │
│                         ├────────────────┤          │              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-45447 │          │              │                   │ 3.5.6-1~deb13u2   │ openssl: Heap Use-After-Free in OpenSSL PKCS7_verify()       │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-45447                   │
├─────────────────────────┼────────────────┤          ├──────────────┼───────────────────┼───────────────────┼──────────────────────────────────────────────────────────────┤
│ libtinfo6               │ CVE-2025-69720 │          │ affected     │ 6.5+20250216-2    │                   │ ncurses: ncurses: Buffer overflow vulnerability may lead to  │
│                         │                │          │              │                   │                   │ arbitrary code execution.                                    │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2025-69720                   │
├─────────────────────────┤                │          │              │                   ├───────────────────┤                                                              │
│ ncurses-base            │                │          │              │                   │                   │                                                              │
│                         │                │          │              │                   │                   │                                                              │
│                         │                │          │              │                   │                   │                                                              │
├─────────────────────────┤                │          │              │                   ├───────────────────┤                                                              │
│ ncurses-bin             │                │          │              │                   │                   │                                                              │
│                         │                │          │              │                   │                   │                                                              │
│                         │                │          │              │                   │                   │                                                              │
├─────────────────────────┼────────────────┼──────────┼──────────────┼───────────────────┼───────────────────┼──────────────────────────────────────────────────────────────┤
│ openssl                 │ CVE-2026-31789 │ CRITICAL │ fixed        │ 3.5.1-1+deb13u1   │ 3.5.5-1~deb13u2   │ openssl: OpenSSL: Heap buffer overflow on 32-bit systems     │
│                         │                │          │              │                   │                   │ from large X.509 certificate...                              │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-31789                   │
│                         ├────────────────┼──────────┤              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2025-15467 │ HIGH     │              │                   │ 3.5.4-1~deb13u2   │ openssl: OpenSSL: Remote code execution or Denial of Service │
│                         │                │          │              │                   │                   │ via oversized Initialization...                              │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2025-15467                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2025-69421 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service via malformed PKCS#12    │
│                         │                │          │              │                   │                   │ file processing                                              │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2025-69421                   │
│                         ├────────────────┤          │              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28387 │          │              │                   │ 3.5.5-1~deb13u2   │ openssl: OpenSSL: Arbitrary code execution due to            │
│                         │                │          │              │                   │                   │ use-after-free in DANE TLSA authentication...                │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28387                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28388 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
│                         │                │          │              │                   │                   │ dereference in delta...                                      │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28388                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28389 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service vulnerability in CMS     │
│                         │                │          │              │                   │                   │ processing                                                   │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28389                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28390 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
│                         │                │          │              │                   │                   │ dereference in CMS...                                        │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28390                   │
│                         ├────────────────┤          │              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-45447 │          │              │                   │ 3.5.6-1~deb13u2   │ openssl: Heap Use-After-Free in OpenSSL PKCS7_verify()       │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-45447                   │
├─────────────────────────┼────────────────┼──────────┤              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│ openssl-provider-legacy │ CVE-2026-31789 │ CRITICAL │              │                   │ 3.5.5-1~deb13u2   │ openssl: OpenSSL: Heap buffer overflow on 32-bit systems     │
│                         │                │          │              │                   │                   │ from large X.509 certificate...                              │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-31789                   │
│                         ├────────────────┼──────────┤              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2025-15467 │ HIGH     │              │                   │ 3.5.4-1~deb13u2   │ openssl: OpenSSL: Remote code execution or Denial of Service │
│                         │                │          │              │                   │                   │ via oversized Initialization...                              │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2025-15467                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2025-69421 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service via malformed PKCS#12    │
│                         │                │          │              │                   │                   │ file processing                                              │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2025-69421                   │
│                         ├────────────────┤          │              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28387 │          │              │                   │ 3.5.5-1~deb13u2   │ openssl: OpenSSL: Arbitrary code execution due to            │
│                         │                │          │              │                   │                   │ use-after-free in DANE TLSA authentication...                │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28387                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28388 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
│                         │                │          │              │                   │                   │ dereference in delta...                                      │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28388                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28389 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service vulnerability in CMS     │
│                         │                │          │              │                   │                   │ processing                                                   │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28389                   │
│                         ├────────────────┤          │              │                   │                   ├──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-28390 │          │              │                   │                   │ openssl: OpenSSL: Denial of Service due to NULL pointer      │
│                         │                │          │              │                   │                   │ dereference in CMS...                                        │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-28390                   │
│                         ├────────────────┤          │              │                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-45447 │          │              │                   │ 3.5.6-1~deb13u2   │ openssl: Heap Use-After-Free in OpenSSL PKCS7_verify()       │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-45447                   │
├─────────────────────────┼────────────────┼──────────┼──────────────┼───────────────────┼───────────────────┼──────────────────────────────────────────────────────────────┤
│ perl-base               │ CVE-2026-42496 │ CRITICAL │ fix_deferred │ 5.40.1-6          │                   │ perl-archive-tar: perl-archive-tar: Path traversal via       │
│                         │                │          │              │                   │                   │ crafted symlinks allows arbitrary file access                │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-42496                   │
│                         ├────────────────┤          ├──────────────┤                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-8376  │          │ affected     │                   │                   │ Perl versions through 5.43.10 have a heap buffer overflow    │
│                         │                │          │              │                   │                   │ when compili ......                                          │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-8376                    │
│                         ├────────────────┼──────────┼──────────────┤                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-42497 │ HIGH     │ fix_deferred │                   │                   │ perl-Archive-Tar: perl-Archive-Tar: Arbitrary file           │
│                         │                │          │              │                   │                   │ modification via crafted hardlinks during archive extraction │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-42497                   │
│                         ├────────────────┤          ├──────────────┤                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-48962 │          │ affected     │                   │                   │ perl-IO-Compress: perl-IO-Compress: Arbitrary code execution │
│                         │                │          │              │                   │                   │ via attacker-controlled output glob                          │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-48962                   │
│                         ├────────────────┤          ├──────────────┤                   ├───────────────────┼──────────────────────────────────────────────────────────────┤
│                         │ CVE-2026-9538  │          │ fix_deferred │                   │                   │ Archive::Tar versions before 3.10 for Perl allow memory      │
│                         │                │          │              │                   │                   │ exhaustion via ...                                           │
│                         │                │          │              │                   │                   │ https://avd.aquasec.com/nvd/cve-2026-9538                    │
└─────────────────────────┴────────────────┴──────────┴──────────────┴───────────────────┴───────────────────┴──────────────────────────────────────────────────────────────┘

Python (python-pkg)
===================
Total: 3 (HIGH: 3, CRITICAL: 0)

┌───────────────────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│          Library          │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                            Title                             │
├───────────────────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ jaraco.context (METADATA) │ CVE-2026-23949 │ HIGH     │ fixed  │ 5.3.0             │ 6.1.0         │ jaraco.context: jaraco.context: Path traversal via malicious │
│                           │                │          │        │                   │               │ tar archives                                                 │
│                           │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-23949                   │
├───────────────────────────┼────────────────┤          │        ├───────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ wheel (METADATA)          │ CVE-2026-24049 │          │        │ 0.45.1            │ 0.46.2        │ wheel: wheel: Privilege Escalation or Arbitrary Code         │
│                           │                │          │        │                   │               │ Execution via malicious wheel file...                        │
│                           │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2026-24049                   │
│                           │                │          │        │                   │               │                                                              │
│                           │                │          │        │                   │               │                                                              │
│                           │                │          │        │                   │               │                                                              │
│                           │                │          │        │                   │               │                                                              │
└───────────────────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
