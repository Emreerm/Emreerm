import os

BADGES = [
    {
        "id": "site",
        "label": "erim.digital",
        "has_arrow": True,
        "is_accent": True,
        "width": 136,
        "icon_type": "globe",
        "icon_trans": "translate(11, 8.5) scale(0.79)",
        "text_x": 33,
        "arrow_x": 115
    },
    {
        "id": "behance",
        "label": "Behance",
        "has_arrow": False,
        "is_accent": False,
        "width": 102,
        "icon_type": "behance",
        "icon_trans": "translate(12, 10.2) scale(0.68)",
        "text_x": 36
    },
    {
        "id": "linkedin",
        "label": "LinkedIn",
        "has_arrow": False,
        "is_accent": False,
        "width": 96,
        "icon_type": "linkedin",
        "icon_trans": "translate(10, 7.8) scale(0.85)",
        "text_x": 33
    },
    {
        "id": "x",
        "label": "X",
        "has_arrow": False,
        "is_accent": False,
        "width": 58,
        "icon_type": "x",
        "icon_trans": "translate(12, 9.4) scale(0.72)",
        "text_x": 34
    },
    {
        "id": "instagram",
        "label": "Instagram",
        "has_arrow": False,
        "is_accent": False,
        "width": 108,
        "icon_type": "instagram",
        "icon_trans": "translate(13, 10.5) scale(0.625)",
        "text_x": 36
    },
    {
        "id": "mail",
        "label": "Mail",
        "has_arrow": False,
        "is_accent": False,
        "width": 74,
        "icon_type": "mail",
        "icon_trans": "translate(11, 7.5) scale(0.88)",
        "text_x": 35
    }
]

def get_icon(icon_type, color):
    if icon_type == "globe":
        return f'''<g fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="9.5"/>
          <path d="M12 2.5a13.5 13.5 0 0 0 0 19M12 2.5a13.5 13.5 0 0 1 0 19M2.5 12h19"/>
        </g>'''
    elif icon_type == "behance":
        return f'''<path d="M22 7h-7V5h7v2zm1.726 10c-.442 1.297-2.029 3-5.171 3-3.455 0-5.555-2.477-5.555-5.554 0-3.327 2.277-5.446 5.518-5.446 3.528 0 5.171 2.399 5.171 5.446 0 .394-.047.781-.047.781h-7.643c.068 1.487 1.056 2.339 2.569 2.339 1.131 0 1.94-.482 2.396-1.566h2.762zm-7.671-3.418h4.745c-.068-1.229-.861-1.996-2.316-1.996-1.42 0-2.361.767-2.429 1.996zm-9.055 6.418H0V6h7.381c2.833 0 4.619 1.42 4.619 3.738 0 1.297-.68 2.418-1.787 2.977 1.488.582 2.195 1.932 2.195 3.547 0 2.459-1.957 3.738-5.408 3.738zm-4.367-8.625h2.385c1.199 0 2.016-.482 2.016-1.539 0-1.078-.817-1.539-2.016-1.539H2.633v3.078zm0 6.328h2.613c1.373 0 2.293-.582 2.293-1.758 0-1.229-.92-1.758-2.293-1.758H2.633v3.516z" fill="{color}"/>'''
    elif icon_type == "linkedin":
        return f'''<path d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43c-1.14 0-2.06-.92-2.06-2.06 0-1.14.92-2.06 2.06-2.06 1.14 0 2.06.92 2.06 2.06 0 1.14-.92 2.06-2.06 2.06zM7.12 20.45H3.56V9h3.56v11.45z" fill="{color}"/>'''
    elif icon_type == "x":
        return f'''<path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z" fill="{color}"/>'''
    elif icon_type == "instagram":
        return f'''<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" fill="{color}"/>'''
    elif icon_type == "mail":
        return f'''<g fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2.5" y="4.5" width="19" height="15" rx="3"/>
          <path d="m21.5 6.5-8.4 5.8a2 2 0 0 1-2.2 0L2.5 6.5"/>
        </g>'''

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(ROOT_DIR, 'assets', 'social')
os.makedirs(OUTPUT_DIR, exist_ok=True)

for theme in ['dark', 'light']:
    for b in BADGES:
        w = b["width"]
        h = 36
        rx = 10
        is_accent = b["is_accent"]
        text_x = b["text_x"]
        
        if theme == 'dark':
            if is_accent:
                bg = "#C7F551"
                stroke = "#C7F551"
                text_color = "#0B0B0C"
                icon_color = "#0B0B0C"
                font_weight = "650"
                hover_bg = "#D6FA75"
                hover_stroke = "#D6FA75"
            else:
                bg = "#0F1114"
                stroke = "#2A2E35"
                text_color = "#F5F5F2"
                icon_color = "#8B9099"
                font_weight = "500"
                hover_bg = "#181C23"
                hover_stroke = "#C7F551"
        else: # light
            if is_accent:
                bg = "#C7F551"
                stroke = "#C7F551"
                text_color = "#0B0B0C"
                icon_color = "#0B0B0C"
                font_weight = "650"
                hover_bg = "#D6FA75"
                hover_stroke = "#D6FA75"
            else:
                bg = "#FFFFFF"
                stroke = "#D8D8D2"
                text_color = "#0B0B0C"
                icon_color = "#62666D"
                font_weight = "500"
                hover_bg = "#F5F5F2"
                hover_stroke = "#8DB21A"

        arrow_markup = ""
        if b["has_arrow"]:
            arrow_x = b["arrow_x"]
            arrow_markup = f'''
  <g transform="translate({arrow_x}, 13.5)">
    <path d="M2.5 1h5.5v5.5M8 1L1 8" fill="none" stroke="{text_color}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" class="arrow"/>
  </g>'''

        icon_code = get_icon(b["icon_type"], icon_color)

        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{b['label']}">
  <defs>
    <style>
      .sans {{
        font-family: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
        font-size: 13px;
        font-weight: {font_weight};
        letter-spacing: -0.2px;
      }}
      .chip {{
        transition: all .15s ease;
      }}
      svg:hover .chip {{
        fill: {hover_bg};
        stroke: {hover_stroke};
      }}
      svg:hover .txt {{
        fill: {text_color if is_accent else ('#C7F551' if theme == 'dark' else '#8DB21A')};
      }}
    </style>
  </defs>
  <rect class="chip" x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="{rx}" fill="{bg}" stroke="{stroke}" stroke-width="1"/>
  <g transform="{b['icon_trans']}" class="icon">
    {icon_code}
  </g>
  <text x="{text_x}" y="22.5" class="sans txt" fill="{text_color}">{b['label']}</text>{arrow_markup}
</svg>'''

        filepath = os.path.join(OUTPUT_DIR, f"{b['id']}-{theme}.svg")
        with open(filepath, "w") as f:
            f.write(svg_content)
print("Regenerated badges.")
