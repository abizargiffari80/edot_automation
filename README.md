# Automation Test (PyTest + Selenium)

End-to-end web UI tests using **Python**, **PyTest**, **Selenium**, and **webdriver-manager**.  
HTML reports are generated automatically with **pytest-html**.

---

## 📦 Setup

```bash
python -m venv .venv
```

### Activate virtual environment
- **Windows PowerShell**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Windows CMD**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```
- **macOS / Linux**
  ```bash
  source .venv/bin/activate
  ```

### Install dependencies
```bash
pip install -r requirements.txt
```

(Optional) copy `.env.example` → `.env` and set your variables:
```
BASE_URL, TEST_USERNAME, TEST_PASSWORD, BROWSER, HEADLESS
```

---

## ▶️ Running Tests

### Run all tests (default headless)
```bash
pytest
```

### Run with visible browser (headed)
```bash
pytest --headed
```

### Force headless
```bash
pytest --headless
```

### Keep browser open after test (for debugging)
```bash
pytest --headed --keep-open -k test_login_success -s
```

---

## 🎯 Select Specific Tests

### Run one file
```bash
pytest web_automation/tests/test_login.py --headed
```

### Run one test function
```bash
pytest -k test_login_success --headed
```

### Run by marker
Markers are defined in `pytest.ini`:
- Run only smoke tests
  ```bash
  pytest -m smoke
  ```
- Run only negative tests
  ```bash
  pytest -m negative
  ```

---

## 📑 Test Report

After any run, open the generated report at:

```
artifacts/report.html
```

This is a **self-contained HTML file** you can view or share directly.

---

## ⚡ Environment Variables (optional)

You can override config via env vars:

- **macOS/Linux/Git Bash**
  ```bash
  HEADLESS=0 pytest
  ```

- **Windows PowerShell**
  ```powershell
  $env:HEADLESS="0"
  pytest
  ```

- **Windows CMD**
  ```cmd
  set HEADLESS=0
  pytest
  ```

---

✅ That’s all! Now you can run the Selenium tests easily and always get a clean `report.html`.
