"""Combine the three store reconciliations into recon/summary.csv.

Run this once, on main, after all three store pull requests are merged:
    python make_summary.py
"""
import csv, glob, os, sys

COLS = {'Bank balance': 'BankBalance', 'Deposits in transit': 'DepositsInTransit', 'Outstanding checks': 'OutstandingChecks',
        'Adjusted bank balance': 'AdjustedBank', 'GL balance': 'GLBalance', 'Difference': 'Difference'}
rows, missing = [], []
for path in sorted(glob.glob(os.path.join('recon', 'store_*.csv'))):
    store = os.path.basename(path)[6:-4]
    with open(path, newline='') as f:
        amounts = {r['Item']: r['Amount'].strip() for r in csv.DictReader(f)}
    if any(not amounts.get(item) for item in COLS):
        missing.append(store); continue
    a = {COLS[k]: round(float(v.replace(',', '').replace('$', '')), 2) for k, v in amounts.items() if k in COLS}
    if round(a['BankBalance'] + a['DepositsInTransit'] - a['OutstandingChecks'], 2) != a['AdjustedBank']:
        print(f'{store}: adjusted bank balance should be bank + deposits in transit - outstanding checks')
    if round(a['AdjustedBank'] - a['GLBalance'], 2) != a['Difference']:
        print(f'{store}: difference should be adjusted bank balance - GL balance')
    rows.append([store] + [f'{a[c]:.2f}' for c in COLS.values()])
if missing:
    sys.exit('Not finished yet: ' + ', '.join(missing) + '. Merge every store before running this.')
with open(os.path.join('recon', 'summary.csv'), 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['Store'] + list(COLS.values())); w.writerows(rows)
print(f'Wrote recon/summary.csv ({len(rows)} stores)')
for r in rows:
    if r[-1] != '0.00':
        print(f'{r[0]} does not reconcile: difference {r[-1]}. Explain it in recon/notes.md.')
