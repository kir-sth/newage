from .admin import router as admin_router
from .common import router as common_router
from .defending import router as last_frontier_router
from .questioning import router as questionnaire_router


ROUTERS = (
    admin_router,
    common_router,
    questionnaire_router,
    last_frontier_router,             
)
