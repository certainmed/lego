# 🧱 LEGO Builder

A browser-based 3D LEGO brick building simulator powered by Three.js. Build virtual LEGO creations directly in your web browser with intuitive controls and a variety of brick types and colors.

## ✨ Features

- **3D Building Environment** - Interactive 3D canvas with camera controls for orbiting, panning, and zooming
- **Multiple Brick Types** - 9 brick variants including standard bricks (1×1, 1×2, 1×4, 2×2, 2×4, 2×6) and plates (1×1, 2×2, 2×4)
- **12 Color Palette** - Red, Blue, Green, Yellow, White, Black, Orange, Purple, Pink, Cyan, Brown, Gray
- **Building Tools** - Place, Select, Paint, and Delete modes
- **Rotation System** - Rotate bricks on X, Y, and Z axes with 90° increments
- **Ghost Preview** - Semi-transparent preview shows brick placement before confirming
- **Collision Detection** - Prevents overlapping bricks with visual feedback
- **Gravity System** - Bricks automatically fall to rest on surfaces below

## 🎮 Controls

| Action | Input |
|--------|-------|
| Place / Select Brick | Left Click |
| Rotate Camera | Right Mouse Drag |
| Zoom In/Out | Scroll Wheel |
| Delete Selected | Delete / Backspace |
| Rotate X Axis | Arrow Up/Down |
| Rotate Y Axis | Arrow Left/Right |
| Rotate Z Axis | Q / E |
| Undo | Ctrl + Z |
| Redo | Ctrl + Y |
| Multi-Select | Shift + Click |
| Deselect All | Escape |

## 💾 Save & Export

- **Save Projects** - Store up to 10 builds in browser localStorage
- **Load Projects** - Restore previously saved creations
- **Export Screenshot** - Download your creation as a PNG image

## 🛠️ Technical Details

- **Single File Application** - All HTML, CSS, and JavaScript in one file
- **Dependencies** - Three.js r128 (loaded via CDN)
- **Rendering** - WebGL with shadow mapping and anti-aliasing
- **History System** - Supports up to 50 undo/redo states

## 🚀 Usage

1. Open `lego.html` in a modern web browser (Chrome, Firefox, Edge, Safari)
2. Select a brick type from the control panel
3. Choose a color from the palette
4. Click on the grid or existing bricks to place new bricks
5. Use rotation controls to orient bricks before placement
6. Save your creation or export as an image

## 📋 Requirements

- Modern web browser with WebGL support
- JavaScript enabled
- No server required - runs entirely client-side
