import logging
from django.shortcuts import HttpResponse

logger = logging.getLogger(__name__)

def log_view(request):
    risky_state = True

    if risky_state:
        logger.warning("Running at risk")

    return HttpResponse("Welcome to logger")