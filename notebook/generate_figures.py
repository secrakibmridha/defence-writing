"""
Generate Elsevier-quality placeholder figures for thesis.
Saves PDFs to graphics/ folder.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# ── Style Configuration ─────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Georgia'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.dpi': 600,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'axes.linewidth': 0.8,
    'lines.linewidth': 1.5,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
})

GRAPHICS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'graphics')
os.makedirs(GRAPHICS_DIR, exist_ok=True)

# Colorblind-friendly palette
COLORS = {
    'blue':   '#0072B2',
    'orange': '#E69F00',
    'green':  '#009E73',
    'red':    '#D55E00',
    'purple': '#CC79A7',
    'cyan':   '#56B4E9',
    'gray':   '#999999',
    'black':  '#000000',
}


# ═══════════════════════════════════════════════════════════════════════
# FIGURE 1: Aggregate Gradation Curve
# ═══════════════════════════════════════════════════════════════════════
def plot_gradation_curve():
    """Aggregate gradation curve with MoRTH upper/lower limits."""
    
    sieve_sizes = np.array([26.5, 19, 13.2, 9.5, 4.75, 2.36, 0.3, 0.075])
    lower_limit = np.array([100, 90, 71, 56, 38, 28, 7, 4])
    upper_limit = np.array([100, 100, 95, 80, 54, 42, 21, 8])
    trial_mix   = np.array([100, 98, 82, 64, 46, 37, 16, 6])
    
    fig, ax = plt.subplots(figsize=(7, 4.5))
    
    # Plot specification envelope (filled)
    ax.fill_between(sieve_sizes, lower_limit, upper_limit, 
                     alpha=0.15, color=COLORS['blue'], label='MoRTH Specification Envelope')
    
    # Upper and lower limits
    ax.plot(sieve_sizes, upper_limit, '-', color=COLORS['blue'], linewidth=1.2, 
            marker='s', markersize=4, label='Upper Limit')
    ax.plot(sieve_sizes, lower_limit, '-', color=COLORS['blue'], linewidth=1.2, 
            marker='s', markersize=4, markerfacecolor='white', label='Lower Limit')
    
    # Trial mix
    ax.plot(sieve_sizes, trial_mix, '-', color=COLORS['red'], linewidth=2.0, 
            marker='o', markersize=6, markeredgecolor=COLORS['red'], 
            markerfacecolor='white', markeredgewidth=1.5, label='Trial Mix', zorder=5)
    
    ax.set_xscale('log')
    ax.set_xlabel('Sieve Size (mm)')
    ax.set_ylabel('Cumulative Passing (%)')
    
    ax.set_xlim(0.05, 30)
    ax.set_ylim(0, 105)
    
    # Custom x-ticks at sieve sizes
    ax.set_xticks(sieve_sizes)
    ax.set_xticklabels([str(s) for s in sieve_sizes], rotation=45, ha='right')
    ax.minorticks_off()
    
    ax.legend(loc='lower right', frameon=True, fancybox=False, edgecolor='gray',
              framealpha=0.95)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    filepath = os.path.join(GRAPHICS_DIR, 'gradation_curve.pdf')
    fig.savefig(filepath, format='pdf')
    plt.close(fig)
    print(f"  [OK] Saved: {filepath}")


# ═══════════════════════════════════════════════════════════════════════
# FIGURE 2: Zingg Diagram
# ═══════════════════════════════════════════════════════════════════════
def plot_zingg_diagram():
    """Zingg diagram showing 4 aggregate shape classification zones."""
    
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    
    threshold = 2/3
    
    # Fill the four quadrants with distinct colors
    # Blade: ER < 2/3, FR < 2/3 (bottom-left)
    blade_rect = mpatches.FancyBboxPatch((0, 0), threshold, threshold,
                                          boxstyle="round,pad=0", 
                                          facecolor=COLORS['red'], alpha=0.15, 
                                          edgecolor='none')
    ax.add_patch(blade_rect)
    ax.text(threshold/2, threshold/2, 'BLADE\n(Flaky & Elongated)', 
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=COLORS['red'], style='italic')
    
    # Disk: ER >= 2/3, FR < 2/3 (bottom-right)
    disk_rect = mpatches.FancyBboxPatch((threshold, 0), 1-threshold, threshold,
                                         boxstyle="round,pad=0",
                                         facecolor=COLORS['orange'], alpha=0.15, 
                                         edgecolor='none')
    ax.add_patch(disk_rect)
    ax.text((1+threshold)/2, threshold/2, 'DISK\n(Flaky)', 
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=COLORS['orange'], style='italic')
    
    # Rod: ER < 2/3, FR >= 2/3 (top-left)
    rod_rect = mpatches.FancyBboxPatch((0, threshold), threshold, 1-threshold,
                                        boxstyle="round,pad=0",
                                        facecolor=COLORS['cyan'], alpha=0.15, 
                                        edgecolor='none')
    ax.add_patch(rod_rect)
    ax.text(threshold/2, (1+threshold)/2, 'ROD\n(Elongated)', 
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=COLORS['blue'], style='italic')
    
    # Cubical: ER >= 2/3, FR >= 2/3 (top-right)
    cube_rect = mpatches.FancyBboxPatch((threshold, threshold), 1-threshold, 1-threshold,
                                         boxstyle="round,pad=0",
                                         facecolor=COLORS['green'], alpha=0.20, 
                                         edgecolor='none')
    ax.add_patch(cube_rect)
    ax.text((1+threshold)/2, (1+threshold)/2, 'CUBICAL\n(Equidimensional)', 
            ha='center', va='center', fontsize=10, fontweight='bold',
            color=COLORS['green'], style='italic')
    
    # Draw threshold lines
    ax.axhline(y=threshold, color='black', linewidth=1.2, linestyle='-', zorder=3)
    ax.axvline(x=threshold, color='black', linewidth=1.2, linestyle='-', zorder=3)
    
    # Threshold annotations
    ax.annotate('2/3', xy=(threshold, -0.04), ha='center', va='top', fontsize=10,
                fontweight='bold', annotation_clip=False)
    ax.annotate('2/3', xy=(-0.04, threshold), ha='right', va='center', fontsize=10,
                fontweight='bold', annotation_clip=False)
    
    ax.set_xlabel('Elongation Ratio ($d_I / d_L$)', fontsize=12)
    ax.set_ylabel('Flatness Ratio ($d_S / d_I$)', fontsize=12)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    
    ax.set_xticks([0, 0.2, 0.4, threshold, 0.8, 1.0])
    ax.set_xticklabels(['0', '0.2', '0.4', '2/3', '0.8', '1.0'])
    ax.set_yticks([0, 0.2, 0.4, threshold, 0.8, 1.0])
    ax.set_yticklabels(['0', '0.2', '0.4', '2/3', '0.8', '1.0'])
    
    ax.grid(True, alpha=0.2, linestyle=':', linewidth=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    filepath = os.path.join(GRAPHICS_DIR, 'zingg_diagram.pdf')
    fig.savefig(filepath, format='pdf')
    plt.close(fig)
    print(f"  [OK] Saved: {filepath}")


# ═══════════════════════════════════════════════════════════════════════
# FIGURE 3: Methodology Flowchart
# ═══════════════════════════════════════════════════════════════════════
def plot_methodology_flowchart():
    """Experimental methodology flowchart."""
    
    fig, ax = plt.subplots(figsize=(8, 11))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Box styling
    box_props = dict(boxstyle='round,pad=0.4', facecolor='#F0F4F8', 
                     edgecolor=COLORS['blue'], linewidth=1.2)
    decision_props = dict(boxstyle='round,pad=0.4', facecolor='#FFF8E1',
                          edgecolor=COLORS['orange'], linewidth=1.2)
    result_props = dict(boxstyle='round,pad=0.4', facecolor='#E8F5E9',
                        edgecolor=COLORS['green'], linewidth=1.2)
    
    # Flowchart elements (x_center, y_center, text, style)
    steps = [
        (5, 15.2, 'Step 1: Material Collection\n& Initial Preparation', box_props),
        (5, 13.6, 'Step 2: Material Characterisation\nBitumen Tests | Aggregate Tests', box_props),
        (5, 12.0, 'Step 3: Sieve Analysis\n& Aggregate Gradation (MoRTH Grading-II)', box_props),
        (5, 10.4, 'Step 4: Aggregate Shape Classification\n(Zingg Diagram: Cubical, Rod, Disk, Blade)', box_props),
        (5, 8.8,  'Step 5: Mix Batching (1200 gm/specimen)\nMix-1 to Mix-4 Preparation', box_props),
        (5, 7.2,  'Step 6: OBC Determination from Mix-1\n(4.0%, 4.5%, 5.0%, 5.5%, 6.0%) → OBC = 5.0%', decision_props),
        (5, 5.6,  'Step 7: Mixing (150°C) & Compaction\n(Marshall Hammer, 75 blows/face)', box_props),
        (5, 4.0,  'Step 8: Performance Testing\nMarshall Stability & Flow', box_props),
        (5, 2.4,  'Step 9: Volumetric Analysis\nGmb, Va%, VMA%, VFB%', box_props),
        (5, 0.8,  'Results, Analysis\n& Conclusions', result_props),
    ]
    
    for x, y, text, props in steps:
        ax.text(x, y, text, ha='center', va='center', fontsize=9,
                bbox=props, fontfamily='serif')
    
    # Draw arrows between steps
    arrow_props = dict(arrowstyle='->', color=COLORS['black'], linewidth=1.2,
                       connectionstyle='arc3,rad=0')
    
    y_positions = [s[1] for s in steps]
    for i in range(len(y_positions) - 1):
        y_start = y_positions[i] - 0.5
        y_end = y_positions[i+1] + 0.5
        ax.annotate('', xy=(5, y_end), xytext=(5, y_start),
                     arrowprops=arrow_props)
    
    plt.tight_layout()
    filepath = os.path.join(GRAPHICS_DIR, 'methodology_flowchart.pdf')
    fig.savefig(filepath, format='pdf')
    plt.close(fig)
    print(f"  [OK] Saved: {filepath}")


def generate_aggregate_properties_bar():
    """Bar chart comparing aggregate properties with specification limits."""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    properties = ['AIV', 'ACV', 'Flakiness', 'Elongation']
    results = [18, 20, 15, 23]
    limits = [27, 30, 30, 30]
    
    x = np.arange(len(properties))
    width = 0.35
    
    rects1 = ax.bar(x - width/2, results, width, label='Test Result', color=COLORS['blue'], edgecolor='black', linewidth=1)
    rects2 = ax.bar(x + width/2, limits, width, label='Max Limit', color=COLORS['orange'], edgecolor='black', linewidth=1, hatch='//')
    
    ax.set_ylabel('Percentage (%)')
    ax.set_title('Physical and Mechanical Properties of Coarse Aggregates')
    ax.set_xticks(x)
    ax.set_xticklabels(properties)
    ax.legend(frameon=True, edgecolor='black', fancybox=False)
    ax.set_ylim(0, 40)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add labels on top of bars
    for rect in rects1:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)
    
    for rect in rects2:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    filepath = os.path.join(GRAPHICS_DIR, 'aggregate_properties.pdf')
    fig.savefig(filepath, format='pdf')
    plt.close(fig)
    print(f"  [OK] Saved: {filepath}")


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("Generating Elsevier-quality thesis figures...")
    print()
    
    print("[0/3] Aggregate Properties Bar Chart")
    generate_aggregate_properties_bar()
    
    print("[1/3] Aggregate Gradation Curve")
    plot_gradation_curve()
    
    print("[2/3] Zingg Diagram")
    plot_zingg_diagram()
    
    print("[3/3] Methodology Flowchart")
    plot_methodology_flowchart()
    
    print()
    print(f"All figures saved to: {GRAPHICS_DIR}")
    print("Done.")
