# External Library imports
from datetime import date
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy import text, exists
from sqlalchemy.orm import Session
from pymongo.database import Database
from pymongo import MongoClient

# Internal library imports
from app.models.purchase import PurchaseMySQLEntity
from app.models.brand import BrandMongoEntity
from app.models.car import (
    CarReturnResource,
    CarMySQLEntity,
    CarMongoEntity,
    ModelMongoEntity,
    ColorMongoEntity,
    AccessoryMongoEntity,
    InsuranceMongoEntity,
    SalesPersonMongoEntity,
    CustomerMongoEntity,
    cars_has_accessories,
    cars_has_insurances,
    prepare_car
)
from app.resources.car_resource import (
    CarCreateResource,
    CustomerReturnResource,
    SalesPersonReturnResource,
    ModelReturnResource,
    ColorReturnResource,
    AccessoryReturnResource,
    InsuranceReturnResource
)


def calculate_total_price_for_car(
        model_resource: ModelReturnResource,
        color_resource: ColorReturnResource,
        accessory_resources: List[AccessoryReturnResource],
        insurance_resources: List[InsuranceReturnResource]) -> float:
    total_price: float = 0.0
    total_price += model_resource.price + color_resource.price
    for accessory_resource in accessory_resources:
        total_price += accessory_resource.price
    for insurance_resource in insurance_resources:
        total_price += insurance_resource.price

    # Round total_price to 2 decimal places before returning
    total_price = round(total_price, 2)
    return total_price


class CarRepository(ABC):  # pragma: no cover

    @abstractmethod
    def get_all(
            self,
            customer: Optional[CustomerReturnResource] = None,
            sales_person: Optional[SalesPersonReturnResource] = None,
            is_purchased: Optional[bool] = None,
            is_past_purchase_deadline: Optional[bool] = None,
            limit: Optional[int] = None
    ) -> List[CarReturnResource]:
        pass

    @abstractmethod
    def get_by_id(self, car_id: str) -> Optional[CarReturnResource]:
        pass

    @abstractmethod
    def create(
            self,
            car_create_data: CarCreateResource,
            customer_resource: CustomerReturnResource,
            sales_person_resource: SalesPersonReturnResource,
            model_resource: ModelReturnResource,
            color_resource: ColorReturnResource,
            accessory_resources: List[AccessoryReturnResource],
            insurance_resources: List[InsuranceReturnResource]
    ) -> CarReturnResource:
        pass

    @abstractmethod
    def delete(self, car_resource: CarReturnResource, delete_purchase_too: bool):
        pass


class MySQLCarRepository(CarRepository):
    def __init__(self, session: Session):
        self.session = session

    # This is the past function for get_all,that now uses a stored procedure to handle the logic of filtering all the cars to get
    def get_all_past_function(
            self,
            customer: Optional[CustomerReturnResource] = None,
            sales_person: Optional[SalesPersonReturnResource] = None,
            is_purchased: Optional[bool] = None,
            is_past_purchase_deadline: Optional[bool] = None,
            limit: Optional[int] = None
    ) -> List[CarReturnResource]:

        car_query = self.session.query(CarMySQLEntity)
        if customer is not None and isinstance(customer, CustomerReturnResource):
            car_query = car_query.filter_by(customers_id=customer.id)
        if sales_person is not None and isinstance(sales_person, SalesPersonReturnResource):
            car_query = car_query.filter_by(sales_people_id=sales_person.id)
        if is_purchased is not None and isinstance(is_purchased, bool):
            if is_purchased:
                car_query = car_query.filter(
                    exists().where(PurchaseMySQLEntity.cars_id == CarMySQLEntity.id)
                )
            else:
                car_query = car_query.filter(
                    ~exists().where(PurchaseMySQLEntity.cars_id == CarMySQLEntity.id)
                )
        if is_past_purchase_deadline is not None and isinstance(is_past_purchase_deadline, bool):
            current_date = date.today()
            if is_past_purchase_deadline:
                car_query = car_query.filter(CarMySQLEntity.purchase_deadline < current_date)
            else:
                car_query = car_query.filter(CarMySQLEntity.purchase_deadline >= current_date)

        if limit is not None and isinstance(limit, int) and limit > 0:
            car_query = car_query.limit(limit)

        cars: List[CarMySQLEntity] = cast(List[CarMySQLEntity], car_query.all())
        car_resources: List[CarReturnResource] = []
        for car in cars:
            is_car_purchased: bool = (self.session.query(PurchaseMySQLEntity)
                                      .filter_by(cars_id=car.id).first() is not None)
            car_resources.append(car.as_resource(is_car_purchased))
        return car_resources

    def get_all(self,
                customer: Optional[CustomerReturnResource] = None,
                sales_person: Optional[SalesPersonReturnResource] = None,
                is_purchased: Optional[bool] = None,
                is_past_purchase_deadline: Optional[bool] = None,
                limit: Optional[int] = None
                ) -> List[CarReturnResource]:

        # Define parameters
        customer_id = customer.id if customer else None
        sales_person_id = sales_person.id if sales_person else None
        limit = None if limit is not None and limit <= 0 else limit

        cars_result = self.session.execute(
            text("""
                        CALL get_all_cars(
                            :p_customer_id,
                            :p_sales_person_id,
                            :p_is_purchased,
                            :p_is_past_purchase_deadline,
                            :p_current_date,
                            :p_limit
                        );
                    """),
            {
                "p_customer_id": customer_id,
                "p_sales_person_id": sales_person_id,
                "p_is_purchased": is_purchased,
                "p_is_past_purchase_deadline": is_past_purchase_deadline,
                "p_current_date": date.today(),
                "p_limit": limit
            }
        ).fetchall()

        cars: List[CarReturnResource] = []
        for car_result in cars_result:
            car_id: str = car_result[0]
            car = self.session.get(CarMySQLEntity, car_id)
            car = cast(CarMySQLEntity, car)
            is_car_purchased: bool = (self.session.query(PurchaseMySQLEntity)
                                      .filter_by(cars_id=car.id).first() is not None)
            cars.append(car.as_resource(is_car_purchased))
        return cars

    def get_by_id(self, car_id: str) -> Optional[CarReturnResource]:
        car: Optional[CarMySQLEntity] = self.session.get(CarMySQLEntity, car_id)
        if car is not None:
            is_car_purchased: bool = (self.session.query(PurchaseMySQLEntity)
                                      .filter_by(cars_id=car.id).first() is not None)
            return car.as_resource(is_car_purchased)
        return None

    def create(
            self,
            car_create_data: CarCreateResource,
            customer_resource: CustomerReturnResource,
            sales_person_resource: SalesPersonReturnResource,
            model_resource: ModelReturnResource,
            color_resource: ColorReturnResource,
            accessory_resources: List[AccessoryReturnResource],
            insurance_resources: List[InsuranceReturnResource]) -> CarReturnResource:

        try:
            new_car = CarMySQLEntity(
                models_id=model_resource.id,
                colors_id=color_resource.id,
                customers_id=customer_resource.id,
                sales_people_id=sales_person_resource.id,
                total_price=calculate_total_price_for_car(
                    model_resource,
                    color_resource,
                    accessory_resources,
                    insurance_resources
                ),
                purchase_deadline=car_create_data.purchase_deadline
            )

            self.session.add(new_car)
            self.session.flush()

            for accessory_resource in accessory_resources:
                insert = cars_has_accessories.insert(
                ).values(cars_id=new_car.id, accessories_id=accessory_resource.id)
                self.session.execute(insert)

            for insurance_resource in insurance_resources:
                insert = cars_has_insurances.insert(
                ).values(cars_id=new_car.id, insurances_id=insurance_resource.id)
                self.session.execute(insert)

            self.session.flush()
            self.session.refresh(new_car)
            return new_car.as_resource(is_purchased=False)
        except Exception as e:  # pragma: no cover
            self.session.rollback()
            raise e

    def delete(self, car_resource: CarReturnResource, delete_purchase_too: bool):
        car_id = car_resource.id
        try:
            if delete_purchase_too:
                self.session.query(PurchaseMySQLEntity).filter_by(cars_id=car_id).delete()
                self.session.flush()
            self.session.query(CarMySQLEntity).filter_by(id=car_id).delete()
            self.session.flush()
        except Exception as e:  # pragma: no cover
            self.session.rollback()
            raise e


class MongoDBCarRepository(CarRepository):  # pragma: no cover
    def __init__(self, database: Database):
        self.database = database

    def get_all(
            self,
            customer: Optional[CustomerReturnResource] = None,
            sales_person: Optional[SalesPersonReturnResource] = None,
            is_purchased: Optional[bool] = None,
            is_past_purchase_deadline: Optional[bool] = None,
            limit: Optional[int] = None
    ) -> List[CarReturnResource]:

        car_query = {}
        if customer is not None and isinstance(customer, CustomerReturnResource):
            car_query["customer._id"] = customer.id
        if sales_person is not None and isinstance(sales_person, SalesPersonReturnResource):
            car_query["sales_person._id"] = sales_person.id
        if is_past_purchase_deadline is not None and isinstance(is_past_purchase_deadline, bool):
            current_date = date.today()
            if is_past_purchase_deadline:
                car_query["purchase_deadline"] = {"$lt": current_date.strftime("%Y-%m-%d")}
            else:
                car_query["purchase_deadline"] = {"$gte": current_date.strftime("%Y-%m-%d")}

        cars_query = self.database.get_collection("cars").find(car_query)
        if limit is not None and isinstance(limit, int) and limit > 0:
            cars_query = cars_query.limit(limit)
        cars: List[CarReturnResource] = []
        for car in cars_query:
            is_car_purchased = self.database.get_collection("purchases").count_documents({"car._id": car["_id"]}) > 0
            if is_purchased is not None:
                if is_purchased and not is_car_purchased:
                    continue
                if not is_purchased and is_car_purchased:
                    continue
            car_entity = prepare_car(self.database, car)
            car_resource = car_entity.as_resource(is_car_purchased)
            cars.append(car_resource)
        return cars

    def get_by_id(self, car_id: str) -> Optional[CarReturnResource]:
        car_query = self.database.get_collection("cars").find_one({"_id": car_id})
        if car_query is None:
            return None
        car_entity = prepare_car(self.database, car_query)
        is_purchased = self.database.get_collection("purchases").count_documents({"car._id": car_query["_id"]}) > 0
        return car_entity.as_resource(is_purchased)

    def create(
            self,
            car_create_data: CarCreateResource,
            customer_resource: CustomerReturnResource,
            sales_person_resource: SalesPersonReturnResource,
            model_resource: ModelReturnResource,
            color_resource: ColorReturnResource,
            accessory_resources: List[AccessoryReturnResource],
            insurance_resources: List[InsuranceReturnResource]
    ) -> CarReturnResource:
        customer_entity = CustomerMongoEntity(**customer_resource.model_dump(), _id=customer_resource.id)
        sales_person_hashed_password = self.database.get_collection("sales_people").find_one(
            {"_id": sales_person_resource.id},
            {"hashed_password": 1}
        ).get("hashed_password")
        sales_person_entity = SalesPersonMongoEntity(
            **sales_person_resource.model_dump(),
            hashed_password=sales_person_hashed_password,
            _id=sales_person_resource.id
        )
        model_brand_entity = BrandMongoEntity(**model_resource.brand.model_dump(), _id=model_resource.brand.id)
        model_colors_entities = [ColorMongoEntity(**color.model_dump(), _id=color.id) for color in model_resource.colors]
        model_entity = ModelMongoEntity(
            **model_resource.model_dump(exclude={"brand", "colors"}),
            brand=model_brand_entity,
            colors=model_colors_entities,
            _id=model_resource.id
        )
        color_entity = ColorMongoEntity(**color_resource.model_dump())
        accessories_entities = [AccessoryMongoEntity(**accessory.model_dump()) for accessory in accessory_resources]
        insurances_entities = [InsuranceMongoEntity(**insurance.model_dump()) for insurance in insurance_resources]
        new_car = CarMongoEntity(
            total_price=calculate_total_price_for_car(
                model_resource,
                color_resource,
                accessory_resources,
                insurance_resources
            ),
            purchase_deadline=car_create_data.purchase_deadline,
            model=model_entity,
            color=color_entity,
            customer=customer_entity,
            sales_person=sales_person_entity,
            accessories=accessories_entities,
            insurances=insurances_entities
        )

        self.database.get_collection("cars").insert_one(new_car.model_dump(by_alias=True))

        return new_car.as_resource(is_purchased=False)


    def delete(self, car_resource: CarReturnResource, delete_purchase_too: bool):
        car_id = car_resource.id
        client: MongoClient = self.database.client
        session = client.start_session()
        try:
            with session.start_transaction():
                if delete_purchase_too:
                    self.database.get_collection("purchases").delete_many({"car._id": car_id}, session=session)
                self.database.get_collection("cars").delete_one({"_id": car_id}, session=session)
        except Exception as e:  # pragma: no cover
            session.abort_transaction()
            raise e
        finally:
            session.end_session()

        # Placeholder for future repositories
        # class OtherDBCarRepository(CarRepository):
        #     ...
