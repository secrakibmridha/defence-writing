"""
Generate high-impact, publication-quality comparative figure for Bitumen Physical Properties
vs South Asian National Highway Specifications (Bangladesh RHD, India MORT&H, Nepal DOR, Pakistan NHA).
Saves PDF to graphics/ folder.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import numpy as np
import os

# ── Style Configuration ─────────────────────────────────────────────
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Georgia'],
    'font.size': 10,
    'axes.labelsize': 10.5,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8.5,
    'figure.dpi': 600,
    'savefig.dpi': 600,
})

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPHICS_DIR = os.path.join(BASE_DIR, 'graphics')
os.makedirs(GRAPHICS_DIR, exist_ok=True)

# Elegant color palette
COLORS = {
    'local': '#1b4965',       # Deep rich navy
    'imported': '#c1121f',    # Vivid crimson red
    'spec_range': '#e2eafc',  # Soft ice blue for range
    'spec_border': '#4361ee', # Clean blue border
    'min_line': '#2b9348',    # Forest green for min requirement line
    'fail_bg': '#fee2e2',     # Subtle red tint for substandard values
}

def generate_regional_comparison_figure():
    fig, axes = plt.subplots(2, 3, figsize=(11.5, 6.8))
    axes = axes.flatten()

    entities = ['Local\n(ERL)', 'Imported\n(Low-Cost)', 'Bangladesh\n(RHD)', 'India\n(MORT&H)', 'Nepal\n(DOR)', 'Pakistan\n(NHA)']
    x = np.arange(len(entities))

    # ────────────────────────────────────────────────────────────────
    # 1. Penetration at 25°C (dmm)
    # ────────────────────────────────────────────────────────────────
    ax = axes[0]
    local_val = 64
    imp_val = 68
    
    # Range for standards: 60 - 70 dmm across all
    bars = ax.bar([0, 1], [local_val, imp_val], width=0.55, 
                  color=[COLORS['local'], COLORS['imported']], edgecolor='black', linewidth=0.8, zorder=3)
    
    # Plot standard range bands for 4 countries
    for i in range(2, 6):
        ax.bar(i, 10, bottom=60, width=0.55, color='#d8e2dc', edgecolor='#2b2d42', linewidth=0.8, 
               hatch='///', zorder=3, label='Standard Spec Range' if i == 2 else "")
    
    # Add horizontal reference lines spanning across
    ax.axhline(60, color='#2b2d42', linestyle=':', linewidth=0.9, alpha=0.7)
    ax.axhline(70, color='#2b2d42', linestyle=':', linewidth=0.9, alpha=0.7)
    
    # Annotations
    ax.text(0, local_val + 1.2, f'{local_val}', ha='center', va='bottom', fontweight='bold', color=COLORS['local'], fontsize=9.5)
    ax.text(1, imp_val + 1.2, f'{imp_val}', ha='center', va='bottom', fontweight='bold', color=COLORS['imported'], fontsize=9.5)
    for i in range(2, 6):
        ax.text(i, 65, '60–70', ha='center', va='center', fontsize=8, color='#1d3557', fontweight='bold')

    ax.set_title('(a) Penetration at 25°C (dmm)', pad=12, fontweight='bold')
    ax.set_ylim(0, 85)
    ax.set_ylabel('Penetration (dmm)')

    # ────────────────────────────────────────────────────────────────
    # 2. Softening Point (°C) - Critical Rutting Indicator
    # ────────────────────────────────────────────────────────────────
    ax = axes[1]
    local_sp = 52
    imp_sp = 41
    
    bars = ax.bar([0, 1], [local_sp, imp_sp], width=0.55, 
                  color=[COLORS['local'], COLORS['imported']], edgecolor='black', linewidth=0.8, zorder=3)
    
    # BD: 48-56, India: 47-55 (min 47), Nepal: 48-56, Pak: 48-56
    ranges = [(48, 8), (47, 8), (48, 8), (48, 8)] # (bottom, height)
    labels_sp = ['48–56', '47–55', '48–56', '48–56']
    for idx, (b, h) in enumerate(ranges):
        ax.bar(idx + 2, h, bottom=b, width=0.55, color='#d8e2dc', edgecolor='#2b2d42', linewidth=0.8, hatch='///', zorder=3)
        ax.text(idx + 2, b + h/2, labels_sp[idx], ha='center', va='center', fontsize=8, color='#1d3557', fontweight='bold')
    
    # Highlight regional minimum boundary (~47-48°C)
    ax.axhline(47, color='#d90429', linestyle='--', linewidth=1.1, alpha=0.85, label='Regional Min Spec Threshold')
    
    # Value annotations
    ax.text(0, local_sp + 1.2, f'{local_sp}°C\n[Pass]', ha='center', va='bottom', fontweight='bold', color=COLORS['local'], fontsize=8.5)
    ax.text(1, imp_sp + 1.2, f'{imp_sp}°C\n[FAIL]', ha='center', va='bottom', fontweight='bold', color=COLORS['imported'], fontsize=8.5)

    ax.set_title('(b) Softening Point (°C)', pad=12, fontweight='bold')
    ax.set_ylim(0, 68)
    ax.set_ylabel('Softening Point (°C)')

    # ────────────────────────────────────────────────────────────────
    # 3. Ductility at 25°C (cm)
    # ────────────────────────────────────────────────────────────────
    ax = axes[2]
    local_duc = 112
    imp_duc = 91
    
    ax.bar([0, 1], [local_duc, imp_duc], width=0.55, 
           color=[COLORS['local'], COLORS['imported']], edgecolor='black', linewidth=0.8, zorder=3)
    
    # Spec mins: BD: min 100, India: min 75, Nepal: min 100, Pak: min 100
    duc_mins = [100, 75, 100, 100]
    duc_labels = ['Min 100', 'Min 75', 'Min 100', 'Min 100']
    for idx, (m, lbl) in enumerate(zip(duc_mins, duc_labels)):
        ax.bar(idx + 2, m, bottom=0, width=0.55, color='#e9ecef', edgecolor='#495057', linewidth=0.8, linestyle='--', zorder=3)
        ax.text(idx + 2, m/2, f'≥ {m} cm', ha='center', va='center', fontsize=8, color='#212529', fontweight='bold', rotation=90)
    
    ax.text(0, local_duc + 2, f'{local_duc} cm', ha='center', va='bottom', fontweight='bold', color=COLORS['local'], fontsize=8.5)
    ax.text(1, imp_duc + 2, f'{imp_duc} cm\n(Fails BD, NP, PK)', ha='center', va='bottom', fontweight='bold', color=COLORS['imported'], fontsize=8)

    ax.set_title('(c) Ductility at 25°C (cm)', pad=12, fontweight='bold')
    ax.set_ylim(0, 135)
    ax.set_ylabel('Ductility (cm)')

    # ────────────────────────────────────────────────────────────────
    # 4. Flash Point (°C) - Safety & Volatility
    # ────────────────────────────────────────────────────────────────
    ax = axes[3]
    local_fp = 255
    imp_fp = 218
    
    ax.bar([0, 1], [local_fp, imp_fp], width=0.55, 
           color=[COLORS['local'], COLORS['imported']], edgecolor='black', linewidth=0.8, zorder=3)
    
    # Mandated threshold across all 4 countries: Min 232°C
    for idx in range(2, 6):
        ax.bar(idx, 232, bottom=0, width=0.55, color='#e9ecef', edgecolor='#495057', linewidth=0.8, linestyle='--', zorder=3)
        ax.text(idx, 116, 'Min 232°C', ha='center', va='center', fontsize=8, color='#212529', fontweight='bold', rotation=90)
    
    ax.axhline(232, color='#d90429', linestyle='--', linewidth=1.1, alpha=0.85, label='Universal Safety Min (232°C)')
    
    ax.text(0, local_fp + 4, f'{local_fp}°C\n[Safe]', ha='center', va='bottom', fontweight='bold', color=COLORS['local'], fontsize=8.5)
    ax.text(1, imp_fp + 4, f'{imp_fp}°C\n[HAZARD]', ha='center', va='bottom', fontweight='bold', color=COLORS['imported'], fontsize=8.5)

    ax.set_title('(d) Flash Point (°C)', pad=12, fontweight='bold')
    ax.set_ylim(0, 300)
    ax.set_ylabel('Flash Point (°C)')

    # ────────────────────────────────────────────────────────────────
    # 5. Specific Gravity at 25°C
    # ────────────────────────────────────────────────────────────────
    ax = axes[4]
    local_sg = 1.023
    imp_sg = 0.990
    
    ax.bar([0, 1], [local_sg, imp_sg], width=0.55, 
           color=[COLORS['local'], COLORS['imported']], edgecolor='black', linewidth=0.8, zorder=3)
    
    # 1.01 - 1.06 for all
    for idx in range(2, 6):
        ax.bar(idx, 0.05, bottom=1.01, width=0.55, color='#d8e2dc', edgecolor='#2b2d42', linewidth=0.8, hatch='///', zorder=3)
        ax.text(idx, 1.035, '1.01–1.06', ha='center', va='center', fontsize=7.5, color='#1d3557', fontweight='bold')
    
    ax.axhline(1.01, color='#2b2d42', linestyle=':', linewidth=0.9, alpha=0.7)
    ax.axhline(1.06, color='#2b2d42', linestyle=':', linewidth=0.9, alpha=0.7)
    
    ax.text(0, local_sg + 0.008, f'{local_sg:.3f}', ha='center', va='bottom', fontweight='bold', color=COLORS['local'], fontsize=8.5)
    ax.text(1, imp_sg + 0.008, f'{imp_sg:.3f}\n(< 1.01)', ha='center', va='bottom', fontweight='bold', color=COLORS['imported'], fontsize=8)

    ax.set_title('(e) Specific Gravity at 25°C', pad=12, fontweight='bold')
    ax.set_ylim(0.85, 1.12)
    ax.set_ylabel('Specific Gravity')

    # ────────────────────────────────────────────────────────────────
    # 6. Comprehensive Regional Compliance Scorecard / Matrix
    # ────────────────────────────────────────────────────────────────
    ax = axes[5]
    ax.axis('off')
    
    # Create custom visual scorecard table
    table_data = [
        ['Parameter', 'Local (ERL)', 'Imported', 'Regional Status'],
        ['Penetration', '64 dmm', '68 dmm', 'All Comply (60-70)'],
        ['Softening Pt.', '52 °C', '41 °C', 'Imp. Fails All Standards'],
        ['Ductility', '112 cm', '91 cm', 'Imp. Fails BD/NP/PK'],
        ['Flash Point', '255 °C', '218 °C', 'Imp. Fire Hazard (<232)'],
        ['Specific Gravity', '1.023', '0.990', 'Imp. Substandard (<1.01)'],
    ]
    
    table = ax.table(cellText=table_data, loc='center', cellLoc='center',
                     colWidths=[0.32, 0.22, 0.22, 0.35])
    table.auto_set_font_size(False)
    table.set_fontsize(8.2)
    table.scale(1.05, 1.65)
    
    # Style table headers and cells
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor('#adb5bd')
        cell.set_linewidth(0.7)
        if row == 0:
            cell.set_facecolor('#1b4965')
            cell.set_text_props(color='white', fontweight='bold')
        elif col == 1:
            cell.set_facecolor('#e8f4f8')
            cell.set_text_props(fontweight='bold', color='#1b4965')
        elif col == 2:
            cell.set_facecolor('#fde8e8')
            cell.set_text_props(fontweight='bold', color='#c1121f')
        elif col == 3:
            txt = cell.get_text().get_text()
            if 'Fail' in txt or 'Hazard' in txt or 'Substandard' in txt:
                cell.set_facecolor('#fef2f2')
                cell.set_text_props(color='#b91c1c', fontweight='bold')
            else:
                cell.set_facecolor('#f0fdf4')
                cell.set_text_props(color='#15803d', fontweight='bold')
        else:
            cell.set_facecolor('#ffffff')
            cell.set_text_props(fontweight='bold')

    ax.set_title('(f) Regional Compliance Summary Matrix', pad=12, fontweight='bold')

    # Formatting axes common settings
    for idx in range(5):
        a = axes[idx]
        a.set_xticks(x)
        a.set_xticklabels(entities, rotation=0, ha='center', fontsize=7.8)
        a.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)
        a.spines['top'].set_visible(False)
        a.spines['right'].set_visible(False)

    # Global custom legend at top
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['local'], edgecolor='black', label='Local (ERL) Bitumen (Experimental)'),
        mpatches.Patch(facecolor=COLORS['imported'], edgecolor='black', label='Imported Low-Cost Bitumen (Experimental)'),
        mpatches.Patch(facecolor='#d8e2dc', edgecolor='#2b2d42', hatch='///', label='National Standard Spec Envelope (Range)'),
        mpatches.Patch(facecolor='#e9ecef', edgecolor='#495057', linestyle='--', label='National Standard Minimum Requirement'),
        Line2D([0], [0], color='#d90429', linestyle='--', linewidth=1.2, label='Critical Safety / Quality Threshold'),
    ]
    
    fig.legend(handles=legend_elements, loc='upper center', bbox_to_anchor=(0.5, 1.03),
               ncol=3, frameon=True, edgecolor='#cccccc', fancybox=False, fontsize=8.5)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    
    filepath = os.path.join(GRAPHICS_DIR, 'bitumen_regional_comparison.pdf')
    fig.savefig(filepath, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"[OK] Successfully saved: {filepath}")

if __name__ == '__main__':
    print("Generating Regional Comparative Assessment Figure...")
    generate_regional_comparison_figure()
