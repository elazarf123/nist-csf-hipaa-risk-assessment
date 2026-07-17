"""
generate_scorecard_chart.py
Renders the maturity scorecard (assessment/scorecard.png) from scores.csv:
current vs target maturity per CSF 2.0 category, grouped by function.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

BASE = Path(__file__).resolve().parent.parent
df = pd.read_csv(BASE / "assessment" / "scores.csv")

fig, ax = plt.subplots(figsize=(12, 5.5))
x = range(len(df))
ax.bar([i - 0.2 for i in x], df["score"], width=0.4, label="Current", color="#c0392b")
ax.bar([i + 0.2 for i in x], df["target"], width=0.4, label="Target", color="#a5c8e4")
ax.set_xticks(list(x))
ax.set_xticklabels(df["category"], rotation=45, ha="right")
ax.set_ylabel("Maturity (1=Partial ... 4=Adaptive)")
ax.set_yticks([1, 2, 3, 4])
ax.set_title("Caprock Family Clinic - NIST CSF 2.0 Maturity: Current vs Target (fictional assessment)")
ax.legend()

# shade by function
bounds, prev, start = [], None, 0
for i, fn in enumerate(df["function"]):
    if fn != prev and prev is not None:
        bounds.append((start, i - 0.5, prev)); start = i - 0.5
    if prev is None: start = -0.5
    prev = fn
bounds.append((start, len(df) - 0.5, prev))
for i, (s, e, fn) in enumerate(bounds):
    ax.axvspan(s, e, color="#000000" if i % 2 else "#888888", alpha=0.05)
    ax.text((s + e) / 2, 4.25, fn, ha="center", fontweight="bold")
ax.set_ylim(0, 4.6)

fig.tight_layout()
out = BASE / "assessment" / "scorecard.png"
fig.savefig(out, dpi=120)
print(f"Saved {out}")
print(df.groupby("function")[["score", "target"]].mean().round(2))
