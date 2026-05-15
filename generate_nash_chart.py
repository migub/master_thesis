"""
Generate Figure 9: Deal Quality - Game-Normalized Nash Ratio by lambda Configuration
Uses agreed-only Nash ratio (from Table 12 'Agreed r_Nash' column).
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# Data from Table 12 (Agreed r_Nash column)
configs = ['Self-Only', 'Fair-Only', 'All-Equal']
grpo_values = [0.728, 0.740, 0.747]
lagrpo_values = [0.716, 0.787, 0.740]

# Bar chart setup
x = np.arange(len(configs))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 4.5))

# Colors matching original (light blue / dark blue)
color_grpo = '#7eb6e6'    # light blue
color_lagrpo = '#1f4f7a'  # dark blue

bars1 = ax.bar(x - width/2, grpo_values, width, label='GRPO', color=color_grpo, edgecolor='black', linewidth=0.5)
bars2 = ax.bar(x + width/2, lagrpo_values, width, label='LA-GRPO', color=color_lagrpo, edgecolor='black', linewidth=0.5)

# Value labels above bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.3f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)

# Y-axis from 0.5 to better show differences
ax.set_ylim(0.5, 0.82)
ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.yaxis.set_minor_locator(MultipleLocator(0.025))

ax.set_ylabel('Agreed Nash Ratio (game-normalized)', fontsize=11)
ax.set_title('Deal Quality: Agreed Game-Normalized Nash Ratio by ' + r'$\lambda$' + ' Configuration', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(configs, fontsize=11)

# Legend
ax.legend(loc='lower right', frameon=True, fontsize=10)

# Grid for readability
ax.grid(axis='y', linestyle='--', alpha=0.4, which='major')
ax.set_axisbelow(True)

# Cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('images/nash_product_comparison.pdf', bbox_inches='tight', dpi=300)
plt.savefig('/tmp/nash_preview.png', bbox_inches='tight', dpi=150)
print("Saved!")
