# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class UserIDPassword(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    UserIDPassword - a model defined in OpenAPI

        user_id: The user_id of this UserIDPassword [Optional].
        password: The password of this UserIDPassword [Optional].
    """

    user_id: Optional[str] = None
    password: Optional[str] = None

UserIDPassword.update_forward_refs()
