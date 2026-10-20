# Ridgeline team bank reconciliation: solution

The worked solution to TechHub challenge 412, **Reconcile Three Stores as a Team in One Repository** (https://techhub.byuaccounting.net/t/412-git-reconcile-three-stores-as-a-team-in-one-repository/9412/).
The starter that students copy is on the `main` branch of https://github.com/techhub-training/ridgeline-team-recon.

`recon/summary.csv`, after all three stores are merged:

```
Store,BankBalance,DepositsInTransit,OutstandingChecks,AdjustedBank,GLBalance,Difference
S01,83377.37,8096.99,5086.58,86387.78,86387.78,0.00
S05,98943.66,7465.67,4826.34,101582.99,101582.99,0.00
S07,94785.15,6940.36,1440.70,100284.81,100319.81,-35.00
```

Orem and St. George reconcile. Idaho Falls is 35.00 short: the October statement has a **stop payment fee** (October 21)
that isn't in the ledger. The books need the entry in `recon/notes.md`. Every store's last deposit (October 30, a
Friday) reaches the bank on Monday, November 2, so each has one deposit in transit.

The team workflow, one teammate's commands:

```
gh repo clone <owner>/ridgeline-team-recon
cd ridgeline-team-recon
git switch -c recon-S07
# fill in recon/store_S07.csv and recon/notes.md
git add recon/store_S07.csv recon/notes.md
git commit -m "Reconcile Idaho Falls (S07) for October"
git push -u origin recon-S07
gh pr create --fill
```

A reviewer: `gh pr checkout <number>`, check the numbers, then `gh pr review --approve` and `gh pr merge`.
Finally, on `main`: `git pull`, `python make_summary.py`, commit and push `recon/summary.csv`.
