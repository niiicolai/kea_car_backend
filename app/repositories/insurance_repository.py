# External Library imports
from abc import ABC, abstractmethod
from typing import Optional, List, cast
from sqlalchemy.orm import Session as MySQLSession
from pymongo.database import Database
from neo4j import Session as Neo4jSession, Query

# Internal library imports
from app.models.insurance import (
    InsuranceReturnResource,
    InsuranceMySQLEntity,
    InsuranceMongoEntity,
    InsuranceNeo4jEntity)


class InsuranceRepository(ABC):
    @abstractmethod
    def get_all(self, limit: Optional[int] = None) -> List[InsuranceReturnResource]:  # pragma: no cover
        pass

    @abstractmethod
    def get_by_id(self, insurance_id: str) -> Optional[InsuranceReturnResource]:  # pragma: no cover
        pass


class MySQLInsuranceRepository(InsuranceRepository):
    def __init__(self, session: MySQLSession):
        self.session = session

    def get_all(self, limit: Optional[int] = None) -> List[InsuranceReturnResource]:
        insurances_query = self.session.query(InsuranceMySQLEntity)
        if limit is not None and isinstance(limit, int) and limit > 0:
            insurances_query = insurances_query.limit(limit)
        insurances: List[InsuranceMySQLEntity] = cast(List[InsuranceMySQLEntity], insurances_query.all())
        return [insurance.as_resource() for insurance in insurances]

    def get_by_id(self, insurance_id: str) -> Optional[InsuranceReturnResource]:
        insurance: Optional[InsuranceMySQLEntity] = self.session.get(InsuranceMySQLEntity, insurance_id)
        if insurance is not None:
            return insurance.as_resource()
        return None


class MongoDBInsuranceRepository(InsuranceRepository):  # pragma: no cover
    def __init__(self, database: Database):
        self.database = database

    def get_all(self, limit: Optional[int] = None) -> List[InsuranceReturnResource]:
        insurances = self.database.get_collection("insurances").find(
        ).limit(0 if not limit else limit)
        insurances = [
            InsuranceMongoEntity(
                **insurance
            ).as_resource()
            for insurance in insurances]
        return insurances

    def get_by_id(self, insurance_id: str) -> Optional[InsuranceReturnResource]:
        insurance = self.database.get_collection("insurances").find_one(
            {"_id": insurance_id})
        if insurance is not None:
            return InsuranceMongoEntity(
                **insurance
            ).as_resource()
        return None


class Neo4jInsuranceRepository(InsuranceRepository):  # pragma: no cover
    def __init__(self, session: Neo4jSession):
        self.session = session

    def get_all(self, limit: Optional[int] = None) -> List[InsuranceReturnResource]:
        query = Query("MATCH (i:Insurance) RETURN i")
        parameters = {}
        if limit is not None and isinstance(limit, int) and limit > 0:
            query = Query("MATCH (i:Insurance) RETURN i LIMIT $limit")
            parameters["limit"] = limit
        result = self.session.run(query, parameters)
        accessories = [InsuranceNeo4jEntity(**record["i"]).as_resource() for record in result]
        return accessories

    def get_by_id(self, insurance_id: str) -> Optional[InsuranceReturnResource]:
        result = self.session.run(
            "MATCH (i:Insurance {id: $id}) RETURN i",
            id=insurance_id
        )
        record = result.single()
        if record is not None:
            return InsuranceNeo4jEntity(**record["i"]).as_resource()
        return None
