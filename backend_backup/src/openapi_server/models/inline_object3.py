# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class InlineObject3(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    InlineObject3 - a model defined in OpenAPI

        user_name: The user_name of this InlineObject3 [Optional].
        user_id: The user_id of this InlineObject3 [Optional].
        password: The password of this InlineObject3 [Optional].
        e_mail: The e_mail of this InlineObject3 [Optional].
    """

    user_name: Optional[str] = None
    user_id: Optional[str] = None
    password: Optional[str] = None
    e_mail: Optional[str] = None

InlineObject3.update_forward_refs()
