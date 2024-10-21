# Gerekli kütüphaneleri import et
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import requests # URL'den resim indirmek için
from io import BytesIO
import cv2
from ultralytics import YOLO
from PIL import Image # Resmi işlemek için



# Flask uygulamasını başlat
app = Flask(__name__, template_folder='apps/templates', static_folder='static/uploads')

# YOLO modelini yükle
model = YOLO('best.pt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Kullanıcının dosya mı yüklediğini yoksa URL mi girdiğini kontrol et
        file = request.files.get('file')
        url = request.form.get('url')
        selected_class = request.form.get('class')  # Seçilen sınıf (car-damage, dent, scratch, glass-break)

        filepath = None

        if file:  # Dosya yüklendiyse
            filename = secure_filename(file.filename)
            filepath = os.path.join('static/uploads', filename)
            file.save(filepath)
        elif url:  # URL girildiyse
            try:
                response = requests.get(url)
                if response.status_code != 200:
                    return f"URL'den resim indirilemedi: HTTP {response.status_code} hatası"
                
                # İçerik türünü kontrol et
                content_type = response.headers['Content-Type']
                if 'image' not in content_type:
                    return f"URL bir resim değil, içerik türü: {content_type}"
                
                # İçerik türüne göre uzantıyı belirle
                if 'jpeg' in content_type:
                    extension = 'jpg'
                elif 'png' in content_type:
                    extension = 'png'
                elif 'gif' in content_type:
                    extension = 'gif'
                else:
                    return f"Tanınmayan resim formatı: {content_type}"

                # Dosya adını ayarla
                filename = secure_filename(f"downloaded_image.{extension}")
                filepath = os.path.join('static/uploads', filename)

                # Resmi dosya olarak kaydet
                image = Image.open(BytesIO(response.content))
                image.save(filepath)
                
            except Exception as e:
                return f"URL'den resim indirilemedi: {str(e)}"

        if filepath:  # Eğer resim başarıyla işlendiyse
            results = model(filepath)
            image = cv2.imread(filepath)
            filtered_results = []
            confidence_values = []  # Tüm doğruluk değerlerini tutacak liste

            for result in results[0].boxes:
                class_name = model.names[int(result.cls)].lower()
                if class_name == selected_class:
                    filtered_results.append(result)
                    confidence_value = result.conf.item()
                    confidence_values.append(confidence_value)  # Değeri listeye ekle

            # Sonuçları görüntüde işaretleme
            for result in filtered_results:
                x1, y1, x2, y2 = map(int, result.xyxy[0])
                score = result.conf[0]
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, f'{selected_class}: {score:.2f}', (x1 + 10, y1 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # Yeni dosya kaydet
            output_filename = f"output_{filename}"
            output_filepath = os.path.join('uploads', output_filename)
            cv2.imwrite(output_filepath, image)

            # Doğruluk değerlerini yüzde formatında ve iki ondalık basamakla göster
            confidence_percentages = [f"%{conf * 100:.2f}" for conf in confidence_values]

            # Sonuçları ve doğruluk değerlerini 'result.html' sayfasına döndür
            return render_template('result.html', file=output_filename, selected_class=selected_class, confidence_values=confidence_percentages)
    return render_template('index.html')


# Uygulamayı çalıştır
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
