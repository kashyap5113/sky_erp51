import os
import sys

# Add project root to Python path
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

# Correct Django settings module
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'skyerpnext.settings'
)

# Run Vercel setup (optional)
try:
    import manage_vercel
except ImportError:
    pass

from django.core.asgi import get_asgi_application

app = get_asgi_application()

def handler(request):
    return app(request.scope, request.receive, request.send)
