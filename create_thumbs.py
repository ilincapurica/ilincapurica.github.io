from PIL import Image
import os

folders = ["assets/wunderzeit", "assets/eichmann", "assets/jungendclub", "assets/reportagen"]
thumb_size = (500, 400)

for folder in folders:
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.jpg', '.jpeg')):
                filepath = os.path.join(folder, filename)
                name, ext = os.path.splitext(filename)
                thumb_path = os.path.join(folder, f"{name}-thumb{ext}")
                
                img = Image.open(filepath)
                img.thumbnail(thumb_size, Image.Resampling.LANCZOS)
                img.save(thumb_path, quality=85)
                
                print(f"✓ {folder}/{filename} → {name}-thumb{ext}")

print("\nDone! All thumbnails created.")
