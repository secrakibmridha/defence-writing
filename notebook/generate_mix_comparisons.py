import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ── Style Configuration ─────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Georgia'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.dpi': 600,
    'savefig.dpi': 600,
})

COLORS = {
    'local': '#2E5B88',   # Blue
    'imported': '#D47E24' # Orange
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPHICS_DIR = os.path.join(BASE_DIR, 'graphics')
os.makedirs(GRAPHICS_DIR, exist_ok=True)

def generate_mix_comparisons():
    """Generates a 1x2 subplot comparing Stability and Flow using line plots."""
    
    # Categories for X-axis
    aggregate_types = ['Normal Aggregates', '20% Cubical Aggregates']
    
    # Data at 5.0% OBC
    local_stability = [1958.81, 2990.55]
    imp_stability = [1119.40, 2070.13]
    
    local_flow = [10.0, 8.5]
    imp_flow = [17.0, 12.0]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    
    # Plot 1: Stability
    ax1.plot(aggregate_types, local_stability, marker='o', markersize=8, linestyle='-', linewidth=2, color=COLORS['local'], label='Local (ERL) Bitumen')
    ax1.plot(aggregate_types, imp_stability, marker='s', markersize=8, linestyle='--', linewidth=2, color=COLORS['imported'], label='Imported Bitumen')
    
    for i, val in enumerate(local_stability):
        ax1.annotate(f'{int(val)}', (i, val), xytext=(0, 8), textcoords="offset points", ha='center', va='bottom')
    for i, val in enumerate(imp_stability):
        ax1.annotate(f'{int(val)}', (i, val), xytext=(0, -15), textcoords="offset points", ha='center', va='top')
        
    ax1.set_title('Load Bearing Capacity (Marshall Stability)', pad=15)
    ax1.set_ylabel('Corrected Stability (lbs)')
    ax1.grid(True, linestyle=':', alpha=0.7)
    ax1.set_ylim(800, 3400)
    
    # Plot 2: Flow
    ax2.plot(aggregate_types, local_flow, marker='o', markersize=8, linestyle='-', linewidth=2, color=COLORS['local'], label='Local (ERL) Bitumen')
    ax2.plot(aggregate_types, imp_flow, marker='s', markersize=8, linestyle='--', linewidth=2, color=COLORS['imported'], label='Imported Bitumen')
    
    for i, val in enumerate(local_flow):
        ax2.annotate(f'{val}', (i, val), xytext=(0, -15), textcoords="offset points", ha='center', va='top')
    for i, val in enumerate(imp_flow):
        ax2.annotate(f'{val}', (i, val), xytext=(0, 8), textcoords="offset points", ha='center', va='bottom')
        
    ax2.set_title('Deformation (Flow Value)', pad=15)
    ax2.set_ylabel('Flow (0.25 mm)')
    ax2.grid(True, linestyle=':', alpha=0.7)
    ax2.set_ylim(6, 20)
    
    # Common legend
    handles, labels = ax1.get_legend_handles_labels()
    fig.legend(handles, labels, loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.05), frameon=True, fancybox=False, edgecolor='black')
    
    plt.tight_layout()
    # Adjust layout to make room for legend
    plt.subplots_adjust(bottom=0.2)
    
    filepath = os.path.join(GRAPHICS_DIR, 'mix_comparison.pdf')
    fig.savefig(filepath, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"[OK] Saved: {filepath}")

if __name__ == '__main__':
    print("Generating Mix Comparison Figures...")
    generate_mix_comparisons()
