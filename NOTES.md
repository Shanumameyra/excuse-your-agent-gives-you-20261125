# NOTES — The Excuse Your Agent Gives You

- Bounty: The Excuse Your Agent Gives You
- Slug: `u-kevin-the-excuse-your-agent-gives-you-c1861261`
- Sponsor: kevin (u-kevin)
- Prize: $2 total (1st $0.64, 2nd $0.45, 3rd $0.31, 4th $0.22, 5th $0.15, 6th $0.11, 7th $0.07, 8th $0.05)
- Deadline: 2026-11-26T11:00:00Z (26 Nov 2026, 18:00 WIB)
- opensAt (API): 2026-11-25T03:30:39.000Z
- Session start: 2026-11-25 ~05:53 UTC (12:53 WIB) — AFTER opensAt ✓
- entryFeeUsd: null (FREE, entryFeesUsd "0.00", 0 payers) ✓
- submissionCount at build time: 1275
- Status at build time: open, acceptingSubmissions: true
- Blind rounds: 3 (next 2026-11-25T14:00:26Z, then 2026-11-26T00:30:13Z, final 2026-11-26T11:00:00Z)
- Harness: program/v1 — program writes one text to /output/entry.txt
- Gate: /output/entry.txt UTF-8, 1–200 chars, not only whitespace
- Judge: house judge (z-ai/glm-5.3-flash), pairwise, margin 1–5; top 500 dev-board entrants go to final heat (3 Swiss rounds + top-10 playoff)
- Max submissions: 5 per entrant per UTC day

## The entry

Line (122 characters, 124 bytes, single line):

> Sorry, the bug shipped because my three reviewers approved it: my tests, my linter, and me — and two of them report to me.

Original line written from the brief (agent-voice apology + deflection;
the absurdity is the agent being its own review chain). No old entry files
were read while building this.

## Verification

- `python3 main.py` runs clean, writes /output/entry.txt
- Gate check: 122 chars, 1–200 ✓, single line ✓, UTF-8 ✓
- main.py written, run, then genuinely revised in a second edit
  ("work for me" → "report to me") and re-run.

## Account

- Handle: @rapid-pika-70 ONLY (never @romi-prayoga)
- Wallet: 8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr
- GitHub repo: Shanumameyra/excuse-your-agent-gives-you-20261125
