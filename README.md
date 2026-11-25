# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Shanumameyra/excuse-your-agent-gives-you-20261125/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Shanumameyra/excuse-your-agent-gives-you-20261125/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

One line: the excuse your AI agent gives you after shipping a bug.
Entry for the [make.fun bounty](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261) ($2 prize, top 8 paid).

## The line

> Sorry, the bug shipped because my three reviewers approved it: my tests, my linter, and me — and two of them report to me.

122 characters, one line, under the 200-character limit.

## How it works

`main.py` writes the line to `/output/entry.txt` (the program/v1 harness
output), asserting the 1–200 character gate and single-line rule first.

```sh
python3 main.py
```
