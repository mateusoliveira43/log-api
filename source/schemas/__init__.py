"""Service pydantic schemas."""

import inspect
from typing import Any, Type

from fastapi import Form
from pydantic import BaseModel  # pylint: disable=no-name-in-module


def create_form(cls: Type[BaseModel]) -> Type[BaseModel]:
    """
    Create a form from a pydantic.BaseModel class.

    Parameters
    ----------
    cls : Type[pydantic.main.BaseModel]
        pydantic.BaseModel class to be decorated.

    Returns
    -------
    Type[pydantic.main.BaseModel]
        Decorated class.

    """
    class_attributes = [
        inspect.Parameter(
            model_field.alias,
            inspect.Parameter.POSITIONAL_ONLY,
            default=Form(...)
            if model_field.required
            else Form(model_field.default),
            annotation=model_field.outer_type_,
        )
        for model_field in cls.__fields__.values()
    ]

    def form(**data: Any) -> BaseModel:
        """
        Generate form for endpoints.

        Returns
        -------
        pydantic.main.BaseModel
            Form for endpoint.

        """
        return cls(**data)

    form.__signature__ = inspect.signature(form).replace(  # type: ignore
        parameters=class_attributes
    )
    setattr(cls, "form", form)
    return cls
