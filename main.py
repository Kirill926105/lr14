import os
import sys
sys.path.append('image_utils')

from image_utils.image_handler import ImageHandlerV5
from image_utils.image_processor import ImageProcessorV5

def get_images():
    """Получает список изображений"""
    if not os.path.exists("images"):
        os.makedirs("images")
        print("Создана папка 'images/' - добавьте туда картинки")
        return []
    
    images = [f for f in os.listdir("images") 
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if not images:
        print("В папке 'images/' нет картинок!")
        return []
    
    print("\nНайдено картинок:", len(images))
    for i, img in enumerate(images, 1):
        print(f"{i}. {img}")
    
    return images

def main():
    print("=" * 50)
    print("Лабораторная №14 - Вариант 5")
    print("=" * 50)
    
    images = get_images()
    if not images:
        return
    
    # Создаем папку для результатов
    if not os.path.exists("results"):
        os.makedirs("results")
        print("Создана папка 'results/' для сохранения")
    
    try:
        # Выбор картинки
        print(f"\nВыберите картинку (1-{len(images)}):")
        choice = input("Номер или путь к файлу: ").strip()
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(images):
                image_path = os.path.join("images", images[idx])
            else:
                print("Неверный номер!")
                return
        else:
            image_path = choice if os.path.exists(choice) else None
        
        if not image_path or not os.path.exists(image_path):
            print("Файл не найден!")
            return
        
        print(f"\nОбработка: {os.path.basename(image_path)}")
        
        # 1. Загрузка
        handler = ImageHandlerV5(image_path)
        if not handler.image:
            return
        
        # 2. Уменьшение
        if input("Уменьшить до 50%? (да/нет): ").lower() in ['да', 'y', 'yes']:
            handler.scale_to_50_percent()
        
        # 3. Обработка
        processor = ImageProcessorV5(handler.image)
        processor.apply_emboss_filter()
        processor.add_watermark("Вариант 5", opacity=0.7)
        
        # 4. Сохранение в папку results
        handler.image = processor.image
        original_name = os.path.splitext(os.path.basename(image_path))[0]
        saved = handler.save_with_date(original_name)
        
        # Перемещаем в папку results
        if saved and os.path.exists(saved):
            new_path = os.path.join("results", os.path.basename(saved))
            os.rename(saved, new_path)
            saved = new_path
        
        print(f"\n✓ Готово! Сохранено в: {saved}")
        
        # Показать
        if input("Показать результат? (да/нет): ").lower() in ['да', 'y', 'yes']:
            handler.image.show()
        
        # Еще раз?
        if input("\nОбработать еще одну картинку? (да/нет): ").lower() in ['да', 'y', 'yes']:
            print()
            main()
            
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()