import os
import sys
from django.core.asgi import get_asgi_application

# Ensure the project directory is in sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'SkyErp'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyerpnext.settings')

app = get_asgi_application()

def handler(request):
    # Vercel Python handler signature
    return app(request.scope, request.receive, request.send)
