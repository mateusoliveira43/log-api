"""Configuration file for Sphinx."""

# -- Path setup --------------------------------------------------------------

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1].as_posix()

sys.path.append(PROJECT_ROOT)


# -- Project information -----------------------------------------------------

project = "Log API"
copyright = "2022, Mateus Oliveira"
author = "Mateus Oliveira"


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
]
nitpick_ignore = [
    ("py:class", "datetime.datetime"),
    ("py:class", "sqlalchemy.orm.decl_api.Base"),
    ("py:class", "sqlalchemy.orm.session.Session"),
    ("py:class", "fastapi.security.oauth2.OAuth2PasswordRequestForm"),
    ("py:class", "OAuth2PasswordRequestForm"),
    ("py:class", "pydantic.main.BaseModel"),
    ("py:class", "pydantic.networks.EmailStr"),
    ("py:class", "constr"),
    ("py:class", "source.schemas.customer.ConstrainedStrValue"),
    ("py:class", "source.schemas.event.ConstrainedStrValue"),
    ("py:class", "source.schemas.user.ConstrainedStrValue"),
    ("py:exc", "fastapi.HTTPException"),
]


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
