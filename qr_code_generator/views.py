from django.shortcuts import render
import qrcode
from io import BytesIO
from django.http import HttpResponse
import base64

def generate_qr_code(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer)
            img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
            return render(request, 'qr_code_generator/generate.html', {'img_str': img_str})
    return render(request, 'qr_code_generator/generate.html')
