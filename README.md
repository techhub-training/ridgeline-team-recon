# Ridgeline team bank reconciliation

TechHub challenge 412: **Reconcile Three Stores as a Team in One Repository**. Full instructions and hints: https://techhub.byuaccounting.net/t/412-git-reconcile-three-stores-as-a-team-in-one-repository/9412/

*Ridgeline series:* you work in accounting at Ridgeline Home & Tool. Each store deposits its sales into its own bank
account and writes vendor checks from it. October's close needs a bank reconciliation for three of them, and three
of you to do it.

## Work as a team

You are a team of three. Each of you reconciles one store's bank account for October 2026, on your own **branch**,
and gets it into `main` with a **pull request** that a teammate reviews.

| Store | Bank account | Who |
|---|---|---|
| S01 | Ridgeline Orem | Teammate 1 |
| S05 | Ridgeline St. George | Teammate 2 |
| S07 | Ridgeline Idaho Falls | Teammate 3 |

**One teammate (the owner)** clicks **Use this template › Create a new repository**, names it `ridgeline-team-recon`, makes it
**Public**, then **Settings › Collaborators › Add people** and adds the other two. They accept the invitation in their email
or at github.com/notifications. Everyone works in the owner's repository: no forks.

## What's here

| File | What it is |
|---|---|
| `data/opening_balances.csv` | Each account's balance on September 30 (reconciled; bank and books agreed) |
| `data/cash_ledger_oct2026.csv` | October entries in the general ledger's cash account, per store |
| `data/bank_statement_oct2026.csv` | October bank statement lines, per store |
| `recon/store_S01.csv`, `store_S05.csv`, `store_S07.csv` | One blank reconciliation per store: you fill in yours |
| `make_summary.py` | Combines the three into `recon/summary.csv` |

## Your task (each teammate)

1. Clone the owner's repository (or open it in a codespace) and make a branch for your store:
   `git switch -c recon-S05` (your store's number).
2. Reconcile your store. Bank balance = September 30 balance + October bank lines. GL balance = September 30 balance
   + October ledger entries. Match ledger entries to bank lines: a deposit in the ledger that isn't on the statement is
   a **deposit in transit**; a check in the ledger that hasn't cleared is an **outstanding check**.
3. Fill in `recon/store_<yours>.csv`, numbers only, no `$` or commas. Enter outstanding checks as a positive number.
   Adjusted bank balance = bank balance + deposits in transit − outstanding checks. Difference = adjusted bank balance − GL balance.
4. If your difference isn't zero, find out why and write it up in `recon/notes.md`: what it is, and the journal entry that fixes the books.
5. Commit, `git push -u origin recon-S05`, and open a pull request (`gh pr create`, or the button GitHub shows).
   Ask a teammate to review it. The reviewer checks the numbers, leaves a comment, and approves; then merge it.
6. When all three pull requests are merged, **one** of you pulls `main`, runs `python make_summary.py`, and commits
   and pushes `recon/summary.csv`. (If everyone runs it on their own branch, you'll all edit the same file and get merge conflicts.)

## Check your answer

Each of you enters the **owner's** GitHub username in the TechHub checker: https://techhub.byuaccounting.net/check/?c=412.
It reads `recon/summary.csv`, the three store files and `recon/notes.md` from the owner's `main` branch.
Your instructor looks at the **Pull requests** tab to see who did what.

The worked solution is on the [`solution` branch](https://github.com/techhub-training/ridgeline-team-recon/tree/solution).
