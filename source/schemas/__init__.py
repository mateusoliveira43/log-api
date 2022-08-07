"""Service pydantic schemas."""
# pylint: disable=too-few-public-methods

import inspect
from typing import Any

from fastapi import Form
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class BaseFormModel(BaseModel):
    """Base class for schemas with form."""

    def __init_subclass__(cls) -> None:
        """Init class that inherits from BaseModel."""
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

        def get_form(**data: Any) -> BaseModel:
            """
            Generate form for endpoints.

            Returns
            -------
            pydantic.main.BaseModel
                Form for endpoint.

            """
            return cls(**data)

        get_form.__signature__ = inspect.signature(  # type: ignore
            get_form
        ).replace(parameters=class_attributes)
        setattr(cls, "form", get_form)

    @classmethod
    def form(cls) -> None:
        """
        Return form for endpoints.

        __init_subclass__ method overrides this method.
        """
