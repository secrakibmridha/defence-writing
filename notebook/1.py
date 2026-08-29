import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.font_manager import FontProperties

# Set directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else '.'
GRAPHICS_DIR = os.path.join(BASE_DIR, 'graphics')
os.makedirs(GRAPHICS_DIR, exist_ok=True)

# Colors - Premium Elsevier Quality Palette
COLORS = {
    'bitumen_line': '#005b96',     # Deep Professional Blue
    'aggregate_line': '#d9534f',   # Muted Rust/Orange
    'mix_line': '#2e7d32',         # Emerald Green
    'station_fill': '#ffffff',     # Pure White
    'text': '#222222',             # Dark Charcoal for high contrast
    'text_sub': '#555555',         # Subtitle Gray
    'bg': '#fafafa',               # Subtle off-white background
    'legend_bg': '#ffffff'
}

def create_subway_path(ax, points, color, linewidth=10):
    """Draws a thick subway line connecting points with smooth joins."""
    x, y = zip(*points)
    ax.plot(x, y, color=color, linewidth=linewidth, 
            solid_capstyle='round', solid_joinstyle='round', zorder=2)

def draw_station(ax, x, y, color, label, label_pos='top', align=None):
    """Draws a dual-ring subway station marker and offset label."""
    # Outer circle
    circle = patches.Circle((x, y), radius=0.32, 
                            facecolor=COLORS['station_fill'], 
                            edgecolor=color, 
                            linewidth=3.5, 
                            zorder=4)
    ax.add_patch(circle)
    
    # Inner dot
    inner_circle = patches.Circle((x, y), radius=0.12, 
                                  facecolor=color, 
                                  zorder=5)
    ax.add_patch(inner_circle)
    
    # Label positioning and alignment
    offset = 18
    if label_pos == 'top':
        xytext = (0, offset)
        va = 'bottom'
        ha = align or 'center'
    elif label_pos == 'bottom':
        xytext = (0, -offset)
        va = 'top'
        ha = align or 'center'
    elif label_pos == 'right':
        xytext = (offset, 0)
        va = 'center'
        ha = align or 'left'
    elif label_pos == 'left':
        xytext = (-offset, 0)
        va = 'center'
        ha = align or 'right'
    elif label_pos == 'top_right':
        xytext = (offset, offset)
        va = 'bottom'
        ha = align or 'left'
    else:
        xytext = (0, offset)
        va = 'bottom'
        ha = 'center'
    
    font = FontProperties(family='sans-serif', weight='bold', size=9.5)
    
    ax.annotate(label, xy=(x, y), xytext=xytext, textcoords='offset points',
                ha=ha, va=va, color=COLORS['text'], fontproperties=font, 
                linespacing=1.25, zorder=6)

def generate_subway_methodology():
    """Generates the methodology flowchart without visual overlaps."""
    
    fig, ax = plt.subplots(figsize=(15, 10), facecolor=COLORS['bg'])
    ax.set_aspect('equal')
    ax.axis('off')
    
    # --- 1. Define Line Paths (45-degree clean transitions) ---
    bitumen_path = [
        (1.0, 9.5),
        (10.0, 9.5),
        (11.5, 8.0)
    ]
    
    aggregate_path = [
        (1.0, 6.5),
        (10.0, 6.5),
        (11.5, 8.0)
    ]
    
    mix_path = [
        (11.5, 8.0),
        (11.5, 3.2),
        (10.5, 2.2),
        (2.0, 2.2),
        (1.0, 1.2),
        (1.0, -0.2)
    ]
    
    # --- 2. Draw Subway Lines ---
    create_subway_path(ax, bitumen_path, COLORS['bitumen_line'])
    create_subway_path(ax, aggregate_path, COLORS['aggregate_line'])
    create_subway_path(ax, mix_path, COLORS['mix_line'])
    
    # --- 3. Stations & Labels ---
    
    # Bitumen Line (Top Track)
    draw_station(ax, 3.0, 9.5, COLORS['bitumen_line'], 
                 "Material Collection\nBitumen (Local & Imported)", 'top')
    draw_station(ax, 7.5, 9.5, COLORS['bitumen_line'], 
                 "Binder Characterisation\n(Penetration, Softening Point, Ductility)", 'top')
                 
    # Aggregate Line (Middle Track)
    draw_station(ax, 1.8, 6.5, COLORS['aggregate_line'], 
                 "Material Collection\nSylhet Quarry Aggregate", 'bottom')
    draw_station(ax, 4.4, 6.5, COLORS['aggregate_line'], 
                 "Physical Properties\n(AIV, ACV, FI, EI, SG)", 'bottom')
    draw_station(ax, 7.0, 6.5, COLORS['aggregate_line'], 
                 "Sieve Analysis\n(MoRTH Grading-II)", 'bottom')
    draw_station(ax, 9.6, 6.5, COLORS['aggregate_line'], 
                 "Shape Classification\n(Zingg Diagram)", 'bottom')
                 
    # Mix Line - Convergence & Vertical Processing
    draw_station(ax, 11.5, 8.0, COLORS['mix_line'], 
                 "Mix Batching (1200g/spec)\nLocal/Imported × Normal/Cubical", 'right')
    draw_station(ax, 11.5, 5.6, COLORS['mix_line'], 
                 "OBC Determination\nMarshall Method (Trial 4–6%)", 'right')
    draw_station(ax, 11.5, 3.8, COLORS['mix_line'], 
                 "Mixing & Compaction\n(150°C, 75 blows/face)", 'right')
                 
    # Mix Line - Horizontal Testing & Volumetrics (Bottom Track)
    draw_station(ax, 8.5, 2.2, COLORS['mix_line'], 
                 "Performance Testing\n(Marshall Stability & Flow)", 'top')
    draw_station(ax, 5.2, 2.2, COLORS['mix_line'], 
                 "Volumetric Analysis\n(SG, Va%, VMA, VFA)", 'top')
    draw_station(ax, 2.2, 2.2, COLORS['mix_line'], 
                 "Comparative Analysis\nBitumen & Aggregate Types", 'top')
                 
    # Mix Line - Terminal Optimization Station
    draw_station(ax, 1.0, -0.2, COLORS['mix_line'], 
                 "Techno-Economic Roadmap\nFormulation & Optimization", 'right')
                 
    # --- 4. Titles & Header ---
    font_title = FontProperties(family='sans-serif', weight='bold', size=16)
    font_sub = FontProperties(family='sans-serif', weight='normal', size=10)
    
    ax.text(1.0, 11.2, "Experimental Methodology Map", 
            fontproperties=font_title, color=COLORS['text'], ha='left', va='center')
    ax.text(1.0, 10.6, "Asphalt Mixture Characterisation & Performance Evaluation Framework", 
            fontproperties=font_sub, color=COLORS['text_sub'], ha='left', va='center')
            
    # --- 5. Legend (Relocated to clear bottom-right quadrant) ---
    font_legend = FontProperties(family='sans-serif', weight='bold', size=9.5)
    
    legend_box = patches.FancyBboxPatch((6.0, -1.0), 6.5, 1.8, 
                                        boxstyle="round,pad=0.2", 
                                        facecolor=COLORS['legend_bg'], 
                                        edgecolor='#d0d0d0', linewidth=1.2, zorder=3)
    ax.add_patch(legend_box)
    
    # Legend Entries
    entries = [
        (COLORS['bitumen_line'], "Phase I: Bitumen Characterisation", 0.35),
        (COLORS['aggregate_line'], "Phase I: Aggregate Preparation & Testing", -0.10),
        (COLORS['mix_line'], "Phase II: Mix Design, Volumetrics & Optimization", -0.55)
    ]
    
    for color, text, y_pos in entries:
        ax.plot([6.4, 7.2], [y_pos, y_pos], color=color, lw=6, solid_capstyle='round', zorder=4)
        ax.plot(6.8, y_pos, marker='o', markersize=6, markerfacecolor='white', 
                markeredgecolor=color, markeredgewidth=2, zorder=5)
        ax.text(7.5, y_pos, text, va='center', fontproperties=font_legend, color=COLORS['text'], zorder=4)
    
    # Canvas limits with balanced margins
    ax.set_xlim(-0.5, 16.0)
    ax.set_ylim(-1.5, 12.0)
    
    plt.tight_layout()
    output_pdf = os.path.join(GRAPHICS_DIR, '1.pdf')
    output_png = os.path.join(GRAPHICS_DIR, 'methodology_flowchart_fixed.png')
    
    plt.savefig(output_pdf, format='pdf', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    #plt.savefig(output_png, format='png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    
    print(f"[SUCCESS] Methodology Flowchart generated without overlaps.")
    print(f" -> PDF: {output_pdf}")
    print(f" -> PNG: {output_png}")

if __name__ == "__main__":
    generate_subway_methodology()