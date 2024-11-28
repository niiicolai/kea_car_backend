import pytest
from app.services import models_service
from app.resources.model_resource import ModelReturnResource, BrandReturnResource, ColorReturnResource
from app.exceptions.database_errors import UnableToFindIdError


# VALID TESTS FOR get_model_by_id

@pytest.mark.parametrize("valid_model_id, expected_model", [
    ("053b1148-1bb6-4445-85b1-9f71db5b7143",
     {
         "brands_id": "fff14a06-dc2a-447d-a707-9c03fe00c7a0",
         "name": "A4",
         "price": 10000.95,
         "image_url": "https://keacar.ams3.cdn.digitaloceanspaces.com/a4.png",
         "color_ids": [
             "74251648-a7b1-492a-ab2a-f2248c58da00",
             "7bb35b1d-37ff-43c2-988a-cf85c5b6d690",
             "e2164054-4cb8-49d5-a0da-eca5b36a0b3b"
         ]
     }
     ),
    ("1de1b6d3-da97-440b-ba3b-1c865e1de47f",
     {
         "brands_id": "8bb880b8-e336-4039-ad86-2f758539e454",
         "name": "Mustang",
         "price": 10990.95,
         "image_url": "https://keacar.ams3.cdn.digitaloceanspaces.com/mustang.png",
         "color_ids": [
             "7bb35b1d-37ff-43c2-988a-cf85c5b6d690",
             "e2164054-4cb8-49d5-a0da-eca5b36a0b3b"
         ]
     }
     ),
    ("41e96e21-7e57-45aa-8462-35fe83565866",
     {
         "brands_id": "fadeb491-9cde-4534-b855-b1ada31e2b47",
         "name": "Kodiaq",
         "price": 19999.95,
         "image_url": "https://keacar.ams3.cdn.digitaloceanspaces.com/kodiaq.png",
         "color_ids": [
             "7bb35b1d-37ff-43c2-988a-cf85c5b6d690",
             "e2164054-4cb8-49d5-a0da-eca5b36a0b3b"
         ]
     }
     ),
])
def test_get_model_by_id_with_valid_partitions(
        mySQLModelRepository, valid_model_id, expected_model
):
    model = models_service.get_by_id(
        repository=mySQLModelRepository,
        model_id=valid_model_id
    )
    assert isinstance(model, ModelReturnResource), \
        (f"Model is not of type ModelReturnResource, "
         f"but {type(model).__name__}")

    assert model.id == valid_model_id, \
        f"Model ID {model.id} does not match {valid_model_id}"

    assert isinstance(model.brand, BrandReturnResource), \
        (f"Model brand is not of type BrandReturnResource, "
         f"but {type(model.brand).__name__}")

    assert model.brand.id == expected_model.get('brands_id'), \
        (f"Model brand ID {model.brands_id} does not match "
         f"{expected_model.get('brands_id')}")

    assert model.name == expected_model.get('name'), \
        (f"Model name {model.name} does not match "
         f"{expected_model.get('name')}")

    assert model.price == expected_model.get('price'), \
        (f"Model price {model.price} does not match "
         f"{expected_model.get('price')}")

    assert model.image_url == expected_model.get('image_url'), \
        (f"Model image URL {model.image_url} does not match "
         f"{expected_model.get('image_url')}")

    assert isinstance(model.colors, list) and all(isinstance(color, ColorReturnResource) for color in model.colors) \
        , f"Model colors are not a list of ColorReturnResource objects, but {type(model.colors).__name__}"

    assert len(model.colors) == len(expected_model.get('color_ids')), \
        (f"Model colors length {len(model.colors)} does not match "
         f"the expected amount of colors {len(expected_model.get('color_ids'))}")

    assert all(color.id in expected_model.get('color_ids') for color in model.colors), \
        (f"Model colors IDs {', '.join(color.id for color in model.colors)} "
         f"do not match the expected color IDs {', '.join(expected_model.get('color_ids'))}")


# INVALID TESTS FOR get_model_by_id

@pytest.mark.parametrize("invalid_model_id, expected_error, expecting_error_message", [
    (None, TypeError, "model_id must be of type str, not NoneType."),
    (True, TypeError, "model_id must be of type str, not bool."),
    (1, TypeError, "model_id must be of type str, not int."),
    ("unknown-id", UnableToFindIdError, "Model with ID: unknown-id does not exist."),
])
def test_get_model_by_id_with_invalid_model_id_partitions(
        mySQLModelRepository, invalid_model_id, expected_error, expecting_error_message
):
    with pytest.raises(expected_error, match=expecting_error_message):
        models_service.get_by_id(
            repository=mySQLModelRepository,
            model_id=invalid_model_id
        )


@pytest.mark.parametrize("invalid_model_repository, expecting_error_message", [
    (None, "repository must be of type ModelRepository, not NoneType."),
    (1, "repository must be of type ModelRepository, not int."),
    (True, "repository must be of type ModelRepository, not bool."),
    ("repository", "repository must be of type ModelRepository, not str."),
])
def test_get_model_by_id_with_invalid_repository_type_partitions(invalid_model_repository, expecting_error_message):
    with pytest.raises(TypeError, match=expecting_error_message):
        models_service.get_by_id(
            repository=invalid_model_repository,
            model_id="053b1148-1bb6-4445-85b1-9f71db5b7143"
        )


def test_get_model_by_id_with_invalid_repository_types_partitions(
        mySQLAccessoryRepository, mySQLBrandRepository, mySQLInsuranceRepository
):
    with pytest.raises(TypeError,
                       match=f"repository must be of type ModelRepository, not {type(mySQLAccessoryRepository).__name__}."):
        models_service.get_by_id(
            repository=mySQLAccessoryRepository,
            model_id="053b1148-1bb6-4445-85b1-9f71db5b7143"
        )
    with pytest.raises(TypeError,
                       match=f"repository must be of type ModelRepository, not {type(mySQLBrandRepository).__name__}."):
        models_service.get_by_id(
            repository=mySQLBrandRepository,
            model_id="053b1148-1bb6-4445-85b1-9f71db5b7143"
        )
    with pytest.raises(TypeError,
                       match=f"repository must be of type ModelRepository, not {type(mySQLInsuranceRepository).__name__}."):
        models_service.get_by_id(
            repository=mySQLInsuranceRepository,
            model_id="053b1148-1bb6-4445-85b1-9f71db5b7143"
        )


# VALID TESTS FOR get_all_models

@pytest.mark.parametrize("model_id, model_name", [
    ("053b1148-1bb6-4445-85b1-9f71db5b7143", "A4"),
    ("1de1b6d3-da97-440b-ba3b-1c865e1de47f", "Mustang"),
    ("37c7b96c-4142-4890-a1c0-cdb4ff95606e", "Explorer"),
    ("41e96e21-7e57-45aa-8462-35fe83565866", "Kodiaq"),
    ("44bb8524-0b5d-4451-9d20-9bdafe6f8808", "Yeti"),
    ("45395bf5-431b-4643-bce0-c8a3bdba3a63", "A6"),
    ("460200f8-4e2d-47ad-b65e-e5e333c7ed4b", "Octavia"),
    ("48daf651-f67d-465e-8e14-fc02997c8cf9", "Rapid"),
    ("4bcd231c-8d2c-4c9e-a850-12f5e74edef5", "Series 3"),
    ("552bac65-bd5e-4dcd-8f50-cb5b1816d8b3", "S-Class"),
    ("65e666f1-ea52-4982-a1e7-0f164891fee2", "Citigo"),
    ("77dc2097-6d49-4fc9-bd1a-b0221af35dc6", "Fiesta"),
    ("78b4d92e-fa14-4081-9e77-71cd2bad502c", "i8"),
    ("866a22d1-0ea1-458d-9a12-e5206d6ed8fc", "A1"),
    ("8ce88a9b-3275-4fea-86ac-2c15b92a6727", "Fusion"),
    ("8f599259-538f-4b3e-bc3b-50daa8f5fd96", "Series 2"),
    ("996f735f-b06d-426e-ac5b-e90827d92707", "A3"),
    ("ad88f9d8-db4e-4527-b2c7-8abbb475467b", "X6"),
    ("be927e18-6bd4-491c-b031-73a569afa00b", "A-Class"),
    ("d4bd413c-00d8-45ce-be0e-1d1333ac5e75", "R8"),
    ("d96e68ef-4f6f-4623-9c7b-7c4df75ff032", "C-Class"),
    ("deec07da-2049-484f-adc8-2fea95708964", "G-Class"),
    ("ed996516-a141-4f4e-8991-3edeaba81c14", "Series 1"),
    ("fa967f9a-598b-4240-ac49-70ad190795af", "Pickup"),
    ("fb98b121-6648-4a82-b05c-6793b419c1c9", "AmgGT"),
])
def test_get_all_models_with_valid_partitions(
        mySQLModelRepository, mySQLBrandRepository, model_id, model_name
):
    models = models_service.get_all(
        model_repository=mySQLModelRepository,
        brand_repository=mySQLBrandRepository
    )
    assert isinstance(models, list) and all(isinstance(model, ModelReturnResource) for model in models) \
        , f"Models are not a list of ModelReturnResource objects, but {type(models).__name__}"

    assert len(models) == 25, \
        f"There should be 25 models, not '{len(models)}'"

    assert any(model.id == model_id for model in models), \
        f"Model ID {model_id} does not exist in models"

    assert next((model.name for model in models if model.id == model_id), None) == model_name \
        , f"Model name {model_name} not found"


@pytest.mark.parametrize("valid_models_limit, expecting_model_amount", [
    (-1, 25),
    (None, 25),
    (0, 25),
    (1, 1),
    (5, 5),
    (10, 10),
    (15, 15),
    (20, 20),
    (26, 25),
])
def test_get_all_models_with_valid_models_limit_values_partitions(
        mySQLModelRepository, mySQLBrandRepository, valid_models_limit, expecting_model_amount
):
    models = models_service.get_all(
        model_repository=mySQLModelRepository,
        brand_repository=mySQLBrandRepository,
        models_limit=valid_models_limit
    )

    assert isinstance(models, list) and all(isinstance(model, ModelReturnResource) for model in models) \
        , f"Models are not a list of ModelReturnResource objects, but {type(models).__name__}"

    assert len(models) == expecting_model_amount \
        , f"There should be {expecting_model_amount} models, not '{len(models)}'"


@pytest.mark.parametrize("valid_brand_id, expected_models", [
    (None, [
        {"model_id": "053b1148-1bb6-4445-85b1-9f71db5b7143", "model_name": "A4"},
        {"model_id": "1de1b6d3-da97-440b-ba3b-1c865e1de47f", "model_name": "Mustang"},
        {"model_id": "37c7b96c-4142-4890-a1c0-cdb4ff95606e", "model_name": "Explorer"},
        {"model_id": "41e96e21-7e57-45aa-8462-35fe83565866", "model_name": "Kodiaq"},
        {"model_id": "44bb8524-0b5d-4451-9d20-9bdafe6f8808", "model_name": "Yeti"},
        {"model_id": "45395bf5-431b-4643-bce0-c8a3bdba3a63", "model_name": "A6"},
        {"model_id": "460200f8-4e2d-47ad-b65e-e5e333c7ed4b", "model_name": "Octavia"},
        {"model_id": "48daf651-f67d-465e-8e14-fc02997c8cf9", "model_name": "Rapid"},
        {"model_id": "4bcd231c-8d2c-4c9e-a850-12f5e74edef5", "model_name": "Series 3"},
        {"model_id": "552bac65-bd5e-4dcd-8f50-cb5b1816d8b3", "model_name": "S-Class"},
        {"model_id": "65e666f1-ea52-4982-a1e7-0f164891fee2", "model_name": "Citigo"},
        {"model_id": "77dc2097-6d49-4fc9-bd1a-b0221af35dc6", "model_name": "Fiesta"},
        {"model_id": "78b4d92e-fa14-4081-9e77-71cd2bad502c", "model_name": "i8"},
        {"model_id": "866a22d1-0ea1-458d-9a12-e5206d6ed8fc", "model_name": "A1"},
        {"model_id": "8ce88a9b-3275-4fea-86ac-2c15b92a6727", "model_name": "Fusion"},
        {"model_id": "8f599259-538f-4b3e-bc3b-50daa8f5fd96", "model_name": "Series 2"},
        {"model_id": "996f735f-b06d-426e-ac5b-e90827d92707", "model_name": "A3"},
        {"model_id": "ad88f9d8-db4e-4527-b2c7-8abbb475467b", "model_name": "X6"},
        {"model_id": "be927e18-6bd4-491c-b031-73a569afa00b", "model_name": "A-Class"},
        {"model_id": "d4bd413c-00d8-45ce-be0e-1d1333ac5e75", "model_name": "R8"},
        {"model_id": "d96e68ef-4f6f-4623-9c7b-7c4df75ff032", "model_name": "C-Class"},
        {"model_id": "deec07da-2049-484f-adc8-2fea95708964", "model_name": "G-Class"},
        {"model_id": "ed996516-a141-4f4e-8991-3edeaba81c14", "model_name": "Series 1"},
        {"model_id": "fa967f9a-598b-4240-ac49-70ad190795af", "model_name": "Pickup"},
        {"model_id": "fb98b121-6648-4a82-b05c-6793b419c1c9", "model_name": "AmgGT"},
    ]),
    ("fff14a06-dc2a-447d-a707-9c03fe00c7a0", [
        {"model_id": "053b1148-1bb6-4445-85b1-9f71db5b7143", "model_name": "A4"},
        {"model_id": "45395bf5-431b-4643-bce0-c8a3bdba3a63", "model_name": "A6"},
        {"model_id": "866a22d1-0ea1-458d-9a12-e5206d6ed8fc", "model_name": "A1"},
        {"model_id": "996f735f-b06d-426e-ac5b-e90827d92707", "model_name": "A3"},
        {"model_id": "d4bd413c-00d8-45ce-be0e-1d1333ac5e75", "model_name": "R8"},
    ]),
])
def test_get_all_models_with_valid_brand_id_values_partitions(
        mySQLModelRepository, mySQLBrandRepository, valid_brand_id, expected_models
):
    models = models_service.get_all(
        model_repository=mySQLModelRepository,
        brand_repository=mySQLBrandRepository,
        brand_id=valid_brand_id
    )
    assert isinstance(models, list) and all(isinstance(model, ModelReturnResource) for model in models) \
        , f"Models are not a list of ModelReturnResource objects, but {type(models).__name__}"

    assert len(models) == len(expected_models), \
        f"There should be {len(expected_models)} models, not '{len(models)}'"

    for model in models:
        assert any(model.id == expected_model["model_id"] for expected_model in expected_models), \
            f"Model ID {model.id} does not exist in models"

        assert next(
            (expected_model["model_name"] for expected_model in expected_models if
             model.id == expected_model["model_id"]
             ), None) == model.name \
            , f"Model name {model.name} not found"

        assert isinstance(model.brand, BrandReturnResource) \
            , f"Model brand is not of type BrandReturnResource, but {type(model.brand).__name__}"

        if valid_brand_id is not None:
            assert model.brand.id == valid_brand_id, \
                f"Model brand ID {model.brand.id} does not match {valid_brand_id}"


@pytest.mark.parametrize("valid_brand_id, valid_models_limit, expecting_model_amount", [
    (None, -1, 25),
    (None, None, 25),
    (None, 0, 25),
    (None, 1, 1),
    (None, 5, 5),
    (None, 20, 20),
    (None, 26, 25),
    ("8bb880b8-e336-4039-ad86-2f758539e454", -1, 5),
    ("8bb880b8-e336-4039-ad86-2f758539e454", None, 5),
    ("8bb880b8-e336-4039-ad86-2f758539e454", 0, 5),
    ("8bb880b8-e336-4039-ad86-2f758539e454", 1, 1),
    ("8bb880b8-e336-4039-ad86-2f758539e454", 3, 3),
    ("8bb880b8-e336-4039-ad86-2f758539e454", 5, 5),
    ("8bb880b8-e336-4039-ad86-2f758539e454", 6, 5),
    ("8bb880b8-e336-4039-ad86-2f758539e454", 26, 5),
])
def test_get_all_models_with_valid_brand_id_and_models_limit_values_partitions(
        mySQLModelRepository, mySQLBrandRepository, valid_brand_id, valid_models_limit, expecting_model_amount
):
    models = models_service.get_all(
        model_repository=mySQLModelRepository,
        brand_repository=mySQLBrandRepository,
        brand_id=valid_brand_id,
        models_limit=valid_models_limit
    )
    assert isinstance(models, list) and all(isinstance(model, ModelReturnResource) for model in models) \
        , f"Models are not a list of ModelReturnResource objects, but {type(models).__name__}"

    assert len(models) == expecting_model_amount \
        , f"There should be {expecting_model_amount} models, not '{len(models)}'"

    for model in models:
        assert isinstance(model, ModelReturnResource) \
            , f"Model is not of type ModelReturnResource, but {type(model).__name__}"

        assert isinstance(model.brand, BrandReturnResource) \
            , f"Model brand is not of type BrandReturnResource, but {type(model.brand).__name__}"

        if valid_brand_id is not None:
            assert model.brand.id == valid_brand_id, \
                f"Model brand ID {model.brand.id} does not match {valid_brand_id}"


# INVALID TESTS FOR get_all_models

@pytest.mark.parametrize("invalid_models_limit, expecting_error_message", [
    ("1", "models_limit must be of type int or None, not str."),
    (1.0, "models_limit must be of type int or None, not float."),
    (True, "models_limit must be of type int or None, not bool."),
])
def test_get_all_models_with_invalid_models_limit_values_partitions(
        mySQLModelRepository, mySQLBrandRepository, invalid_models_limit, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        models_service.get_all(
            model_repository=mySQLModelRepository,
            brand_repository=mySQLBrandRepository,
            models_limit=invalid_models_limit
        )


@pytest.mark.parametrize("invalid_brand_id, expected_error, expecting_error_message", [
    (1, TypeError, "brand_id must be of type str or None, not int."),
    (True, TypeError, "brand_id must be of type str or None, not bool."),
    ("unknown-id", UnableToFindIdError, "Brand with ID: unknown-id does not exist."),
])
def test_get_all_models_with_invalid_brand_id_partitions(
        mySQLModelRepository, mySQLBrandRepository, invalid_brand_id, expected_error, expecting_error_message
):
    with pytest.raises(expected_error, match=expecting_error_message):
        models_service.get_all(
            model_repository=mySQLModelRepository,
            brand_repository=mySQLBrandRepository,
            brand_id=invalid_brand_id
        )


@pytest.mark.parametrize("invalid_model_repository_type, expecting_error_message", [
    (None, "model_repository must be of type ModelRepository, not NoneType."),
    (1, "model_repository must be of type ModelRepository, not int."),
    (True, "model_repository must be of type ModelRepository, not bool."),
    ("model_repository", "model_repository must be of type ModelRepository, not str."),
])
def test_get_all_models_with_invalid_model_repository_type_partitions(
        mySQLBrandRepository, invalid_model_repository_type, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        models_service.get_all(
            model_repository=invalid_model_repository_type,
            brand_repository=mySQLBrandRepository
        )


@pytest.mark.parametrize("invalid_brand_repository_type, expecting_error_message", [
    (None, "brand_repository must be of type BrandRepository, not NoneType."),
    (1, "brand_repository must be of type BrandRepository, not int."),
    (True, "brand_repository must be of type BrandRepository, not bool."),
    ("brand_repository", "brand_repository must be of type BrandRepository, not str."),
])
def test_get_all_models_with_invalid_brand_repository_type_partitions(
        mySQLModelRepository, invalid_brand_repository_type, expecting_error_message
):
    with pytest.raises(TypeError, match=expecting_error_message):
        models_service.get_all(
            model_repository=mySQLModelRepository,
            brand_repository=invalid_brand_repository_type
        )


def test_get_all_models_with_invalid_repository_types_partitions(
        mySQLModelRepository, mySQLBrandRepository
):
    with pytest.raises(TypeError,
                       match=f"model_repository must be of type ModelRepository, "
                             f"not {type(mySQLBrandRepository).__name__}."
                       ):
        models_service.get_all(
            model_repository=mySQLBrandRepository,
            brand_repository=mySQLBrandRepository
        )

    with pytest.raises(TypeError,
                       match=f"brand_repository must be of type BrandRepository, "
                             f"not {type(mySQLModelRepository).__name__}."):
        models_service.get_all(
            model_repository=mySQLModelRepository,
            brand_repository=mySQLModelRepository
        )
