import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SkyErp')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SkyErp', 'skyerpnext')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyerpnext.settings')

# Run Vercel setup (migrate, collectstatic) before ASGI app
try:
    from SkyErp import manage_vercel
except ImportError:
    pass

from django.core.asgi import get_asgi_application
app = get_asgi_application()

def handler(request):
    return app(request.scope, request.receive, request.send)
