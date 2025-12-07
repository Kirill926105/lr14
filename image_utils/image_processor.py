from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessorV5:
    def __init__(self, img):
        self.image = img
    
    def apply_emboss_filter(self):
        self.image = self.image.filter(ImageFilter.EMBOSS)
        print("Фильтр EMBOSS применен")
    
    def add_watermark(self, text="Вариант 5", opacity=0.7):
        draw = ImageDraw.Draw(self.image)
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        w, h = self.image.size
        draw.text((w-150, h-40), text, font=font, fill=(255,255,255,int(255*opacity)))
        print(f"Водяной знак добавлен: {text}")