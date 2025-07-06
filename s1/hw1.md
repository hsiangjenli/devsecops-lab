# 作業 1：靜態分析初體驗

## Bandit Report

```shell
bandit s1/hw1.py
```

```javascript
[main]  INFO    profile include tests: None
[main]  INFO    profile exclude tests: None
[main]  INFO    cli include tests: None
[main]  INFO    cli exclude tests: None
[main]  INFO    running on Python 3.10.12
Run started:2025-07-06 10:13:56.275305

Test results:
>> Issue: [B105:hardcoded_password_string] Possible hardcoded password: '123456'
   Severity: Low   Confidence: Medium
   CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
   More Info: https://bandit.readthedocs.io/en/1.8.6/plugins/b105_hardcoded_password_string.html
   Location: ./s1/hw1.py:2:11
1       # 硬編碼
2       password = "123456"
3

--------------------------------------------------
>> Issue: [B307:blacklist] Use of possibly insecure function - consider using safer ast.literal_eval.
   Severity: Medium   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.8.6/blacklists/blacklist_calls.html#b307-eval
   Location: ./s1/hw1.py:6:9
5       user_input = input("Enter a Python expression: ")
6       result = eval(user_input)
7

--------------------------------------------------

Code scanned:
        Total lines of code: 6
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 1
                Medium: 1
                High: 0
        Total issues (by confidence):
                Undefined: 0
                Low: 0
                Medium: 1
                High: 1
Files skipped (0):
```

### 如何看 Report

- **Issue** - Bandit 發現的問題代號
- **Severity** - 問題的嚴重性等級
- **Confidence** - Bandit 對問題的信心等級
- **CWE** - Common Weakness Enumeration，問題的分類編號
- **More Info** - 關於問題的更多資訊連結
- **Location** - 問題出現的位置

### `B105:hardcoded_password_string`

### `B307:blacklist`