from .admin import router as admin_router
from .greating import router as greating_router
from .questioning import router as questionnaire_router


ROUTERS = (
    admin_router,
    greating_router,
    questionnaire_router,
)
