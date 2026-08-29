import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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
    'legend.fontsize': 10,
    'figure.dpi': 600,
    'savefig.dpi': 600,
})

COLORS = ['#2E5B88', '#D47E24', '#4E79A7', '#F28E2B']
LABELS = ['Mix-1: Local+Normal', 'Mix-2: Imp+Normal', 'Mix-3: Local+Cubical', 'Mix-4: Imp+Cubical']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPHICS_DIR = os.path.join(BASE_DIR, 'graphics')
os.makedirs(GRAPHICS_DIR, exist_ok=True)

def generate_performance_figures():
    """Generates a 2x3 grid of bar charts comparing the 4 mix variants."""
    
    # Data from Table 4.2
    stability = [1958.81, 1119.40, 2990.55, 2070.13]
    flow = [10.0, 17.0, 8.5, 12.0]
    unit_weight = [149.64, 146.52, 146.64, 150.07]
    va = [3.27, 4.90, 5.20, 2.59]
    vma = [15.00, 16.77, 16.70, 14.93]
    vfa = [78.20, 70.78, 68.86, 82.65]
    
    plots = [
        ('Marshall Stability', stability, 'Corrected Stability (lbs)'),
        ('Flow Value', flow, 'Flow (0.25 mm)'),
        ('Unit Weight', unit_weight, 'Unit Weight (lb/cft)'),
        ('Air Voids (Va)', va, 'Air Voids (%)'),
        ('Voids in Mineral Aggregate (VMA)', vma, 'VMA (%)'),
        ('Voids Filled with Asphalt (VFA)', vfa, 'VFA (%)')
    ]
    
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    axes = axes.flatten()
    
    x = np.arange(len(LABELS))
    width = 0.6
    
    for idx, (title, data, ylabel) in enumerate(plots):
        ax = axes[idx]
        
        bars = ax.bar(x, data, width, color=COLORS, edgecolor='black', linewidth=1)
        
        ax.set_title(title, pad=12, fontweight='bold')
        ax.set_ylabel(ylabel)
        ax.set_xticks(x)
        ax.set_xticklabels(['M1', 'M2', 'M3', 'M4'])
        ax.grid(True, axis='y', linestyle=':', alpha=0.7)
        
        # Add value labels on top of bars
        for bar in bars:
            yval = bar.get_height()
            if yval > 1000:
                ax.text(bar.get_x() + bar.get_width()/2, yval + (max(data)*0.02), f'{int(yval)}', ha='center', va='bottom', fontsize=9)
            else:
                ax.text(bar.get_x() + bar.get_width()/2, yval + (max(data)*0.02), f'{yval:.1f}', ha='center', va='bottom', fontsize=9)
        
        # Expand Y-limit slightly to fit text
        ax.set_ylim(0, max(data) * 1.15)
        
    # Add a custom legend for the whole figure at the bottom
    import matplotlib.patches as mpatches
    legend_patches = [mpatches.Patch(color=COLORS[i], label=LABELS[i]) for i in range(len(LABELS))]
    fig.legend(handles=legend_patches, loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.02), frameon=True, fancybox=False, edgecolor='black')
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.1) # leave space for legend
    
    # Save files
    filepath_pdf = os.path.join(GRAPHICS_DIR, 'performance_assessment.pdf')
    filepath_png = os.path.join(GRAPHICS_DIR, 'performance_assessment.png')
    fig.savefig(filepath_pdf, format='pdf', bbox_inches='tight')
    fig.savefig(filepath_png, format='png', bbox_inches='tight')
    plt.close(fig)
    print(f"[OK] Saved: {filepath_pdf} and {filepath_png}")

if __name__ == '__main__':
    print("Generating Performance Assessment Figures...")
    generate_performance_figures()
