from PIL import Image
import os
from datetime import datetime

class ImageHandlerV5:
    def __init__(self, path):
        try:
            self.image = Image.open(path)
            self.original = self.image.size
            print(f"Загружено: {os.path.basename(path)} ({self.original[0]}x{self.original[1]})")
        except:
            print("Ошибка загрузки!")
            self.image = None
    
    def scale_to_50_percent(self):
        if self.image:
            w, h = self.image.size
            self.image = self.image.resize((w//2, h//2))
            print(f"Уменьшено до: {w//2}x{h//2}")
    
    def save_with_date(self, name="result"):
        if self.image:
            date = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{date}.png"
            self.image.save(filename, "PNG")
            return filename