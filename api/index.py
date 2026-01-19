import os
import sys

# Add SkyErp folder to Python path (DO NOT import it)
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

# Set correct Django settings module
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'skyerpnext.settings'
)

# Run Vercel setup (migrate, collectstatic)
try:
    import manage_vercel
except ImportError as e:
    print("manage_vercel import failed:", e)

from django.core.asgi import get_asgi_application

app = get_asgi_application()

def handler(request):
    return app(request.scope, request.receive, request.send)
