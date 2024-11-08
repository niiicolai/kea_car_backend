# External Library imports
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


from app.controllers.mysql import (
    accessories_controller as mysql_accessories_controller,
    brands_controller as mysql_brands_controller,
    cars_controller as mysql_cars_controller,
    colors_controller as mysql_colors_controller,
    customers_controller as mysql_customers_controller,
    insurances_controller as mysql_insurances_controller,
    models_controller as mysql_models_controller,
    purchases_controller as mysql_purchases_controller,
    sales_people_controller as mysql_sales_people_controller
)
from app.controllers.mysql.views import car_purchase_controller as mysql_car_purchase_controller

app = FastAPI()

CORS_SETTINGS = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"]
}

app.add_middleware(CORSMiddleware, **CORS_SETTINGS)

app.include_router(mysql_accessories_controller.router, prefix="/mysql", tags=["MySQL - Accessories"])
app.include_router(mysql_brands_controller.router, prefix="/mysql", tags=["MySQL - Brands"])
app.include_router(mysql_cars_controller.router, prefix="/mysql", tags=["MySQL - Cars"])
app.include_router(mysql_colors_controller.router, prefix="/mysql", tags=["MySQL - Colors"])
app.include_router(mysql_customers_controller.router, prefix="/mysql", tags=["MySQL - Customers"])
app.include_router(mysql_insurances_controller.router, prefix="/mysql", tags=["MySQL - Insurances"])
app.include_router(mysql_models_controller.router, prefix="/mysql", tags=["MySQL - Models"])
app.include_router(mysql_purchases_controller.router, prefix="/mysql", tags=["MySQL - Purchases"])
app.include_router(mysql_sales_people_controller.router, prefix="/mysql", tags=["MySQL - Sales People"])
app.include_router(mysql_car_purchase_controller.router, prefix="/mysql", tags=["MySQL View - Cars Purchases"])
