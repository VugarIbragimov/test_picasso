from celery import shared_task
from .models import File
from PIL import Image
from io import BytesIO


@shared_task
def process_file(file_id):
    try:
        file = File.objects.get(id=file_id)
        # Открываем изображение с использованием Pillow
        image = Image.open(file.file)

        # Пример: изменяем размер изображения
        resized_image = image.resize((100, 100))

        # Сохраняем обработанное изображение
        buffer = BytesIO()
        resized_image.save(buffer, format='JPEG')
        file.file = buffer.getvalue()

        # Меняем статус на обработано
        file.processed = True
        file.save()

    except Exception as e:
        print(f"Error processing image: {e}")
        raise e
