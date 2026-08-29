import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as mpath
from matplotlib.font_manager import FontProperties

# Set directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAPHICS_DIR = os.path.join(BASE_DIR, 'graphics')
os.makedirs(GRAPHICS_DIR, exist_ok=True)

# Colors - Premium Elsevier Quality Palette
COLORS = {
    'bitumen_line': '#005b96',     # Deep Professional Blue
    'aggregate_line': '#d9534f',   # Muted Rust/Orange
    'mix_line': '#388e3c',         # Emerald Green
    'station_fill': '#ffffff',     # Pure White
    'text': '#333333',             # Dark Gray for readability
    'bg': '#fcfcfc'                # Very subtle off-white background
}

def create_subway_path(ax, points, color, linewidth=12):
    """Draws a thick subway line connecting a list of (x,y) points with rounded corners where possible."""
    x, y = zip(*points)
    ax.plot(x, y, color=color, linewidth=linewidth, 
            solid_capstyle='round', solid_joinstyle='round', zorder=1)

def draw_station(ax, x, y, color, label, label_pos='top', align='center'):
    """Draws a subway station (circle) and adds a label."""
    # Station circle
    circle = patches.Circle((x, y), radius=0.35, 
                            facecolor=COLORS['station_fill'], 
                            edgecolor=color, 
                            linewidth=4, 
                            zorder=3)
    ax.add_patch(circle)
    
    # Station inner dot
    inner_circle = patches.Circle((x, y), radius=0.1, 
                                  facecolor=color, 
                                  zorder=4)
    ax.add_patch(inner_circle)
    
    # Label positioning
    offset = 20
    if label_pos == 'top':
        xytext = (0, offset)
        va = 'bottom'
        ha = align
    elif label_pos == 'bottom':
        xytext = (0, -offset)
        va = 'top'
        ha = align
    elif label_pos == 'right':
        xytext = (offset, 0)
        va = 'center'
        ha = 'left'
    elif label_pos == 'left':
        xytext = (-offset, 0)
        va = 'center'
        ha = 'right'
    elif label_pos == 'top_right':
        xytext = (offset, offset)
        va = 'bottom'
        ha = 'left'
    
    font = FontProperties(family='sans-serif', weight='bold', size=11)
    
    ax.annotate(label, xy=(x, y), xytext=xytext, textcoords='offset points',
                ha=ha, va=va, color=COLORS['text'], fontproperties=font, zorder=6)

def generate_subway_methodology():
    """Generates the methodology flowchart in a subway map style."""
    
    fig, ax = plt.subplots(figsize=(14, 10), facecolor=COLORS['bg'])
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 1. Define Line Paths
    bitumen_path = [
        (1.0, 9.5),
        (10.5, 9.5),
        (11.5, 8.5)
    ]
    
    aggregate_path = [
        (1.0, 7.5),
        (10.5, 7.5),
        (11.5, 8.5)
    ]
    
    mix_path = [
        (11.5, 8.5),
        (11.5, 4.0),
        (10.5, 3.0),
        (3.5, 3.0),
        (2.5, 2.0),
        (2.5, -0.5)
    ]
    
    # 2. Draw Lines
    create_subway_path(ax, bitumen_path, COLORS['bitumen_line'])
    create_subway_path(ax, aggregate_path, COLORS['aggregate_line'])
    create_subway_path(ax, mix_path, COLORS['mix_line'])
    
    # 3. Define and Draw Stations
    
    # --- Bitumen Line ---
    draw_station(ax, 3.0, 9.5, COLORS['bitumen_line'], 
                 "Material Collection\nBitumen (Local & Imported)", 'top')
    draw_station(ax, 8.0, 9.5, COLORS['bitumen_line'], 
                 "Binder Characterisation\n(Penetration, Softening Point, Ductility)", 'top')
                 
    # --- Aggregate Line ---
    draw_station(ax, 2.0, 7.5, COLORS['aggregate_line'], 
                 "Material Collection\nSylhet Quarry Aggregate", 'bottom')
    draw_station(ax, 5.0, 7.5, COLORS['aggregate_line'], 
                 "Physical Properties\n(AIV, ACV, FI, EI, SG)", 'bottom')
    draw_station(ax, 7.5, 7.5, COLORS['aggregate_line'], 
                 "Sieve Analysis\n(MoRTH Grading-II)", 'bottom')
    draw_station(ax, 10.0, 7.5, COLORS['aggregate_line'], 
                 "Shape Classification\n(Zingg Diagram)", 'top_right')
                 
    # --- Mix Line (Convergence & Testing) ---
    draw_station(ax, 11.5, 8.5, COLORS['mix_line'], 
                 "Mix Batching (1200g/spec)\nLocal/Imported × Normal/Cubical", 'right')
    draw_station(ax, 11.5, 6.0, COLORS['mix_line'], 
                 "OBC Determination\nMarshall Method (Trial 4-6%)", 'right')
                 
    draw_station(ax, 11.0, 3.5, COLORS['mix_line'], 
                 "Mixing & Compaction\n(150°C, 75 blows/face)", 'top_right')
                 
    draw_station(ax, 8.0, 3.0, COLORS['mix_line'], 
                 "Performance Testing\n(Marshall Stability & Flow)", 'bottom')
    draw_station(ax, 5.0, 3.0, COLORS['mix_line'], 
                 "Volumetric Analysis\n(SG, Va%, VMA, VFA)", 'bottom')
                 
    draw_station(ax, 2.5, 1.5, COLORS['mix_line'], 
                 "Comparative Analysis\nBitumen & Aggregate Types", 'right')
    draw_station(ax, 2.5, -0.5, COLORS['mix_line'], 
                 "Techno-Economic Roadmap\nFormulation & Optimization", 'right')
                 
    # 4. Add Legends / Phase Titles
    font_phase = FontProperties(family='sans-serif', weight='bold', size=18)
    ax.text(1.0, 11.0, "Experimental Methodology Map", 
            fontproperties=font_phase, color=COLORS['text'], ha='left', va='center')
            
    # Add a small legend for the lines
    font_legend = FontProperties(family='sans-serif', weight='bold', size=10)
    ax.add_patch(patches.Rectangle((1.0, -1.0), 4.5, 1.5, fill=True, color='white', ec='#ccc', lw=1, zorder=1))
    
    ax.plot([1.2, 1.7], [-0.2, -0.2], color=COLORS['bitumen_line'], lw=5)
    ax.text(1.9, -0.2, "Phase I: Bitumen Preparation", va='center', fontproperties=font_legend, color=COLORS['text'])
    
    ax.plot([1.2, 1.7], [-0.5, -0.5], color=COLORS['aggregate_line'], lw=5)
    ax.text(1.9, -0.5, "Phase I: Aggregate Preparation", va='center', fontproperties=font_legend, color=COLORS['text'])
    
    ax.plot([1.2, 1.7], [-0.8, -0.8], color=COLORS['mix_line'], lw=5)
    ax.text(1.9, -0.8, "Phase II: Mix Design & Testing", va='center', fontproperties=font_legend, color=COLORS['text'])
    
    ax.set_xlim(0, 15)
    ax.set_ylim(-1.5, 12)
    
    # Save the figure
    plt.tight_layout()
    output_pdf = os.path.join(GRAPHICS_DIR, 'methodology_flowchart_premium.pdf')
    output_png = os.path.join(GRAPHICS_DIR, 'methodology_flowchart_premium.png')
    
    plt.savefig(output_pdf, format='pdf', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.savefig(output_png, format='png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
    
    print(f"[SUCCESS] High-quality Subway Style Methodology Flowchart generated.")
    print(f" -> PDF: {output_pdf}")
    print(f" -> PNG: {output_png}")

if __name__ == "__main__":
    generate_subway_methodology()
