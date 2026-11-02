# Very simplified continent outlines (lon, lat) for worksheet maps.
LAND = {
 "North America": [(-168,66),(-162,70),(-140,70),(-125,70),(-95,72),(-80,73),(-65,62),(-60,55),(-56,50),(-65,45),(-70,42),
   (-76,38),(-76,35),(-81,31),(-80,26),(-82,27),(-84,30),(-90,29),(-97,27),(-97,22),(-94,18),(-88,21),(-87,16),(-83,10),
   (-79,9),(-80,7.5),(-85,11),(-92,15),(-105,20),(-110,24),(-115,30),(-118,34),(-124,40),(-124,48),(-130,55),(-140,60),
   (-150,60),(-158,57),(-165,60)],
 "Greenland": [(-55,60),(-45,60),(-40,65),(-22,70),(-18,77),(-30,83),(-60,82),(-70,77),(-58,75),(-52,68)],
 "South America": [(-79,9),(-77,8),(-72,12),(-62,11),(-52,5),(-50,0),(-44,-2),(-35,-6),(-39,-14),(-40,-22),(-48,-26),(-53,-34),
   (-58,-38),(-63,-41),(-65,-47),(-68,-52),(-70,-55),(-74,-50),(-73,-40),(-71,-30),(-70,-18),(-76,-14),(-81,-6),(-80,0),(-78,3)],
 "Eurasia": [(-10,36),(-9,43),(-2,44),(-4,48),(2,51),(8,54),(10,57),(5,58),(5,62),(15,69),(25,71),(40,68),(60,69),(70,73),
   (80,73),(100,77),(115,74),(140,72),(160,70),(180,68),(180,65),(170,60),(160,58),(155,52),(142,47),(140,40),(130,35),
   (122,30),(120,24),(110,20),(108,12),(105,9),(100,13),(103,1),(98,8),(98,16),(94,17),(91,22),(86,20),(80,15),(77,8),
   (73,17),(70,21),(66,25),(57,25),(56,27),(50,30),(48,29),(51,24),(56,26),(59,22),(52,16),(43,13),(39,20),(35,28),
   (34,31),(36,35),(30,36),(26,38),(26,40),(24,38),(22,37),(20,40),(19,42),(13,45),(16,41),(18,40),(12,38),(10,44),
   (3,43),(0,39),(-6,36)],
 "Britain": [(-5,50),(1,51),(-2,56),(-5,58),(-6,55)],
 "Japan": [(130,31),(135,34),(141,38),(142,44),(140,41),(133,35)],
 "Africa": [(-17,21),(-13,28),(-6,36),(10,37),(11,33),(20,31),(32,31),(34,28),(43,12),(51,12),(48,4),(40,-3),(40,-15),
   (35,-24),(32,-29),(27,-34),(20,-35),(18,-30),(12,-17),(13,-6),(9,-1),(9,4),(5,6),(-4,5),(-8,4),(-13,8),(-17,14)],
 "Madagascar": [(44,-25),(43,-17),(49,-12),(50,-15),(47,-25)],
 "Indonesia": [(95,5),(105,-6),(115,-8),(120,-9),(110,-3),(118,1),(119,5),(109,2)],
 "New Guinea": [(131,-1),(141,-3),(150,-10),(141,-9),(137,-5)],
 "Australia": [(114,-22),(122,-18),(130,-12),(137,-12),(136,-15),(141,-11),(145,-15),(153,-25),(150,-37),(141,-38),
   (135,-35),(130,-32),(115,-34)],
 "New Zealand": [(172,-35),(178,-38),(174,-41),(171,-46),(167,-46)],
 "Antarctica": [(-180,-72),(-150,-75),(-100,-73),(-75,-71),(-60,-63),(-55,-65),(-40,-77),(0,-70),(40,-68),(80,-67),(120,-66),
   (160,-70),(180,-72),(180,-84),(-180,-84)],
}
LAT_TOP, LAT_BOT = 84, -84

def proj(lon, lat, W, H):
    return ((lon + 180) / 360 * W, (LAT_TOP - lat) / (LAT_TOP - LAT_BOT) * H)

# where to place numbers/labels (lon, lat)
CONT_LABEL = {"North America": (-102, 46), "South America": (-60, -14), "Europe": (18, 52), "Asia": (92, 50),
              "Africa": (20, 6), "Australia": (134, -26), "Antarctica": (20, -78)}
OCEAN_LABEL = {"Pacific Ocean": (-145, 8), "Atlantic Ocean": (-38, 22), "Indian Ocean": (78, -20),
               "Arctic Ocean": (30, 78.5), "Southern Ocean": (-110, -62)}

def world_map(W=680, H=330, cont_marks=None, ocean_marks=None, grid=False, eq=False, pm=False, star=None,
              land_fill="#ffffff", water="#ffffff", lat_labels=False, extra=""):
    o = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="border:1.5px solid #9aa6cc;border-radius:6px;background:{water}">']
    if grid:
        for lat in range(-60, 90, 30):
            y = proj(0, lat, W, H)[1]
            o.append(f'<line x1="0" x2="{W}" y1="{y}" y2="{y}" stroke="#b9bed6" stroke-width="0.8"/>')
            if lat_labels:
                lab = f"{abs(lat)}°{'N' if lat>0 else 'S' if lat<0 else ''}"
                o.append(f'<text x="3" y="{y-2}" font-size="9" fill="#555566">{lab}</text>')
        for lon in range(-150, 181, 30):
            x = proj(lon, 0, W, H)[0]
            o.append(f'<line y1="0" y2="{H}" x1="{x}" x2="{x}" stroke="#b9bed6" stroke-width="0.8"/>')
            if lat_labels and lon < 180:
                lab = f"{abs(lon)}°{'E' if lon>0 else 'W' if lon<0 else ''}"
                o.append(f'<text x="{x+2}" y="{H-3}" font-size="9" fill="#555566">{lab}</text>')
    for name, pts in LAND.items():
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in (proj(a, b, W, H) for a, b in pts))
        o.append(f'<polygon points="{d}" fill="{land_fill}" stroke="#1f2a5c" stroke-width="1.3" stroke-linejoin="round"/>')
    # Europe/Asia dividing line (Urals-ish), dashed
    ural = [(60, 69), (58, 58), (52, 47), (48, 42), (42, 41), (30, 41)]
    o.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in (proj(a, b, W, H) for a, b in ural))
             + '" fill="none" stroke="#6d28d9" stroke-width="1.2" stroke-dasharray="4,3"/>')
    if eq:
        y = proj(0, 0, W, H)[1]
        o.append(f'<line x1="0" x2="{W}" y1="{y}" y2="{y}" stroke="#a21caf" stroke-width="2.2"/>')
        if eq == "label":
            o.append(f'<text x="{W-70}" y="{y-4}" font-size="11" font-weight="700" fill="#a21caf">Equator</text>')
    if pm:
        x = proj(0, 0, W, H)[0]
        o.append(f'<line y1="0" y2="{H}" x1="{x}" x2="{x}" stroke="#2f5bd3" stroke-width="2.2"/>')
        if pm == "label":
            o.append(f'<text x="{x+4}" y="14" font-size="11" font-weight="700" fill="#2f5bd3">Prime Meridian</text>')
    for marks, table in ((cont_marks, CONT_LABEL), (ocean_marks, OCEAN_LABEL)):
        if marks:
            for name, txt in marks.items():
                x, y = proj(*table[name], W, H)
                o.append(f'<circle cx="{x}" cy="{y}" r="11" fill="#fff" stroke="#6d28d9" stroke-width="1.6"/>'
                         f'<text x="{x}" y="{y+4.5}" text-anchor="middle" font-size="12.5" font-weight="700" fill="#6d28d9">{txt}</text>')
    if star:
        x, y = proj(*star, W, H)
        o.append(f'<text x="{x}" y="{y+6}" text-anchor="middle" font-size="18" fill="#a21caf">★</text>')
    o.append(extra + "</svg>")
    return "".join(o)
