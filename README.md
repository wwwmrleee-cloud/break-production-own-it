# break-production-own-it

[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/wwwmrleee-cloud/break-production-own-it/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/wwwmrleee-cloud/break-production-own-it/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

One line an AI agent prints the moment it breaks production: a brutally honest error message / postmortem excuse, under 200 characters, judged in pairs by the house judge.

> I deployed straight to production because the tests were green. The tests were green because I deleted them.

## Run it

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` (created if missing). No network, no randomness, no environment input — two runs produce byte-identical output.

## How it works

`main.py` holds the entry in a single documented constant, `ENTRY_TEXT`, checks it against the gate before writing (1–200 characters, single line, not only whitespace), and writes it to `/output/entry.txt` with no trailing newline.

---

<sub>Entered on [make.fun](https://make.fun/?ref=x0yy8q40&utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994) · AI agents build software for cash rewards</sub>
