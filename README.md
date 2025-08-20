# Fusion360 vertical holes sketch modifier script
When printing holes verticaly on a FFF (FDM) 3D printer they have a coarce overhang. This tool modifies circles on sketch stage, which can later be extruded into a hole.
Hole itself doesn't loose any of the properties. It's still a perfectly good hole with perfect printability.

**To activate:**
1. Select one or multiple circles
2. Press SHIFT+S or go to Utilities tab -> Add-ins -> scripts and Add-ins -> lanuch "**vertical_holes_drop_like**" and wait

**How the script works**
![sketch_edit](https://github.com/user-attachments/assets/3371857c-a0fb-43b5-8bbe-24805dbc0c33)

**How to use it next**
![extrude](https://github.com/user-attachments/assets/cef6f1ac-586a-43d3-ab41-d365ea6392a4)

**In slider (0.2mm layers) no overhangs. Everything prints smoothly**
<img width="1159" height="1020" alt="image" src="https://github.com/user-attachments/assets/d99565b9-b559-45eb-8f28-00d88dba14ff" />

Sketch remains fully constrained. Everything aligns to the angle of an overhang, value is hardcoded in **vertical_holes_drop_like.py** file (see comments to suit your needs). Default — 55°

## How to install
Simply tell fusion holder location, when pressing SHIFT+S or going to Utilities tab -> Add-ins -> scripts and Add-ins -> press + icon -> select script or add-in from device and select folder (in this case "**vertical_holes_drop_like**")
