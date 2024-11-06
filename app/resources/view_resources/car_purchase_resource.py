# External Library imports
from pydantic import Field
from typing import Optional, List

# Internal library imports
from app.resources.purchase_resource import PurchaseBaseReturnResource

from app.resources.car_resource import (
    CarBaseReturnResource,
    CustomerReturnResource,
    SalesPersonReturnResource
)


class CarPurchaseReturnResource(CarBaseReturnResource):
    purchase: Optional[PurchaseBaseReturnResource] = Field(..., description="The car's Purchase as either a Null or a PurchaseReturnResource.")
    is_past_deadline: bool = Field(..., description="A boolean that if true then the car is past its purchase deadline and has not been purchased yet.")


class CarPurchaseSalePersonReturnResource(CarPurchaseReturnResource):
    customer: CustomerReturnResource = Field(..., description="The car's Customer as a CustomerReturnResource.")


class SalesPersonWithCarsReturnResource(SalesPersonReturnResource):
    cars: List[CarPurchaseSalePersonReturnResource] = Field(..., description="The sales person's cars as a list of CarPurchaseSalePersonReturnResource.")


class CarPurchaseCustomerReturnResource(CarPurchaseReturnResource):
    sales_person: SalesPersonReturnResource = Field(..., description="The car's Sales Person as a SalesPersonReturnResource.")


class CustomerWithCarsReturnResource(CustomerReturnResource):
    cars: List[CarPurchaseCustomerReturnResource] = Field(..., description="The customer's cars as a list of CarPurchaseCustomerReturnResource.")