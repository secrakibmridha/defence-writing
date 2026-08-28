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
    'legend.fontsize': 9,
    'figure.dpi': 600,
    'savefig.dpi': 600,
})

COLORS = {
    'blue': '#2E5B88',
    'orange': '#D47E24',
    'black': '#333333'
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPHICS_DIR = os.path.join(BASE_DIR, 'graphics')
os.makedirs(GRAPHICS_DIR, exist_ok=True)

def generate_bitumen_properties_plot():
    """Generates a 2x3 grid of bar charts comparing local and imported bitumen."""
    properties = [
        ('Specific Gravity', 1.023, 0.99, ''),
        ('Penetration', 64, 68, '(0.1 mm)'),
        ('Softening Point', 52, 41, '(°C)'),
        ('Flash Point', 255, 218, '(°C)'),
        ('Fire Point', 312, 253, '(°C)'),
        ('Ductility', 112, 91, '(cm)')
    ]

    fig, axes = plt.subplots(2, 3, figsize=(10, 6))
    axes = axes.flatten()

    labels = ['Local (ERL)', 'Imported']
    x = np.arange(len(labels))
    width = 0.6

    for idx, (prop_name, local_val, imported_val, unit) in enumerate(properties):
        ax = axes[idx]
        values = [local_val, imported_val]
        
        # Plot bars
        bars = ax.bar(x, values, width, color=[COLORS['blue'], COLORS['orange']], edgecolor='black', linewidth=1)
        
        # Add values on top
        for bar in bars:
            height = bar.get_height()
            # formatting: float if specific gravity, else int
            fmt = f'{height:.3f}' if idx == 0 else f'{int(height)}'
            ax.annotate(fmt,
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=9)
            
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        title = f"{prop_name} {unit}" if unit else prop_name
        ax.set_title(title, pad=15)
        
        # Adjust Y limits slightly so text fits
        y_max = max(values)
        ax.set_ylim(0, y_max * 1.25)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    plt.tight_layout()
    filepath = os.path.join(GRAPHICS_DIR, 'bitumen_properties.pdf')
    fig.savefig(filepath, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"[OK] Saved: {filepath}")

if __name__ == '__main__':
    print("Generating Bitumen Properties Figure...")
    generate_bitumen_properties_plot()
