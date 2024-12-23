# External Library imports
from typing import Optional, List
from pydantic import Field


# Internal library imports
from app.resources.purchase_resource import PurchaseBaseReturnResource

from app.resources.car_resource import (
    CarBaseReturnResource,
    CustomerReturnResource,
    SalesPersonReturnResource
)


class CarPurchaseBaseReturnResource(CarBaseReturnResource):
    purchase: Optional[PurchaseBaseReturnResource] = Field(
        default=...,
        description="The car's Purchase as either a Null or a PurchaseReturnResource."
    )
    is_past_deadline: bool = Field(
        default=...,
        description="A boolean that if true then the car is past its purchase deadline and has not been purchased yet."
    )


class CarPurchaseSalePersonReturnResource(CarPurchaseBaseReturnResource):
    customer: CustomerReturnResource = Field(
        default=...,
        description="The car's Customer as a CustomerReturnResource."
    )


class SalesPersonWithCarsReturnResource(SalesPersonReturnResource):
    cars: List[CarPurchaseSalePersonReturnResource] = Field(
        default=...,
        description="The sales person's cars as a list of CarPurchaseSalePersonReturnResource."
    )


class CarPurchaseCustomerReturnResource(CarPurchaseBaseReturnResource):
    sales_person: SalesPersonReturnResource = Field(
        default=...,
        description="The car's Sales Person as a SalesPersonReturnResource."
    )


class CustomerWithCarsReturnResource(CustomerReturnResource):
    cars: List[CarPurchaseCustomerReturnResource] = Field(
        default=...,
        description="The customer's cars as a list of CarPurchaseCustomerReturnResource."
    )

class CarPurchaseReturnResource(CarPurchaseBaseReturnResource):
    sales_person: SalesPersonReturnResource = Field(
        default=...,
        description="The car's Sales Person as a SalesPersonReturnResource."
    )
    customer: CustomerReturnResource = Field(
        default=...,
        description="The car's Customer as a CustomerReturnResource."
    )
