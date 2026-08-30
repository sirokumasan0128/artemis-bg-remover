# Usage

To run the application, ensure your virtual environment is activated and run:

```bash
python main.py
```

## Controls

Once the application is running, you can interact with the canvas using the following controls:

- **Scroll Wheel**: Vertical Pan / Zoom (when holding `Ctrl` or `Cmd`)
- **Shift + Scroll**: Horizontal Pan
- **Right Click / Middle Click / Space + Drag**: Pan Canvas
- **Left Click**: Apply the selected tool (Fill / Erase / Restore)

## Tools Overview

- **AI Remove**: Uses the `rembg` library to automatically detect and remove the background.
- **Fill**: Smart flood fill. Adjust the tolerance to control how much similar color is removed or restored.
- **Erase Brush**: Manually erase parts of the image mask.
- **Restore Brush**: Manually restore parts of the image mask.
- **Brush Size**: Slider to adjust the size of the manual brushes.
- **Undo / Redo**: Step back or forward through your mask edits.
- **Clear Mask**: Completely clear the current mask (restore the original image).
- **Save Mask**: Export the extracted subject as a transparent PNG file.
