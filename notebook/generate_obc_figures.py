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
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
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

def generate_obc_figures():
    """Generates a 2x3 grid of Marshall mix properties for OBC determination."""
    
    # Data
    ac_content = [4.0, 4.5, 5.0, 5.5, 6.0]
    
    # Local Bitumen
    local_stability = [1813.67, 2446.5, 2500, 2438.6, 2118.4]
    local_flow = [9.5, 9, 10, 11, 14]
    local_unit_weight = [145.719, 144.456, 147.278, 150.384, 150.892]
    local_va = [7.539, 7.437, 4.915, 2.191, 1.104]
    local_vma = [16.661, 17.437, 16.467, 15.147, 15.315]
    local_vfa = [54.75, 57.813, 70.152, 85.535, 92.791]
    
    # Imported Bitumen
    imp_stability = [1373.81, 1069.42, 1913.5, 2028.64, 2182.67]
    imp_flow = [10, 11, 12, 12, 15]
    imp_unit_weight = [145.579, 144.955, 148.512, 149.698, 151.757]
    imp_va = [7.421, 7.117, 4.110, 2.638, 0.532]
    imp_vma = [16.554, 17.345, 15.760, 15.534, 14.826]
    imp_vfa = [55.171, 58.968, 73.921, 83.011, 96.112]
    
    plots = [
        ('Stability', local_stability, imp_stability, 'Corrected Stability (lbs)'),
        ('Flow', local_flow, imp_flow, 'Flow (0.25 mm)'),
        ('Unit Weight', local_unit_weight, imp_unit_weight, 'Unit Weight (lb/cft)'),
        ('Air Voids (Va)', local_va, imp_va, 'Air Voids (%)'),
        ('VMA', local_vma, imp_vma, 'VMA (%)'),
        ('VFA', local_vfa, imp_vfa, 'VFA (%)')
    ]
    
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.flatten()
    
    for idx, (title, loc_data, imp_data, ylabel) in enumerate(plots):
        ax = axes[idx]
        ax.plot(ac_content, loc_data, marker='o', linestyle='-', color=COLORS['local'], label='Local (ERL)', linewidth=2)
        ax.plot(ac_content, imp_data, marker='s', linestyle='--', color=COLORS['imported'], label='Imported', linewidth=2)
        
        ax.set_title(title, pad=10)
        ax.set_xlabel('Asphalt Content (%)')
        ax.set_ylabel(ylabel)
        ax.grid(True, linestyle=':', alpha=0.7)
        ax.set_xticks(ac_content)
        
        # Add 4% Air voids horizontal line for the Va plot
        if title == 'Air Voids (Va)':
            ax.axhline(y=4.0, color='red', linestyle='-.', alpha=0.5, label='4% Target')
            
        if idx == 0:
            ax.legend(frameon=True, fancybox=False, edgecolor='black')
            
    plt.tight_layout()
    filepath = os.path.join(GRAPHICS_DIR, 'obc_determination.pdf')
    fig.savefig(filepath, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"[OK] Saved: {filepath}")

if __name__ == '__main__':
    print("Generating OBC Determination Figures...")
    generate_obc_figures()
