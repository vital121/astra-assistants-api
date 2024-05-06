# coding: utf-8

"""
    OpenAI API

    The OpenAI REST API. Please see https://platform.openai.com/docs/api-reference for more details.

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from openapi_server_v2.models.message_content_text_annotations_file_path_object_file_path import MessageContentTextAnnotationsFilePathObjectFilePath
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MessageContentTextAnnotationsFilePathObject(BaseModel):
    """
    A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.
    """ # noqa: E501
    type: StrictStr = Field(description="Always `file_path`.")
    text: StrictStr = Field(description="The text in the message content that needs to be replaced.")
    file_path: MessageContentTextAnnotationsFilePathObjectFilePath
    start_index: Annotated[int, Field(strict=True, ge=0)]
    end_index: Annotated[int, Field(strict=True, ge=0)]
    __properties: ClassVar[List[str]] = ["type", "text", "file_path", "start_index", "end_index"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('file_path'):
            raise ValueError("must be one of enum values ('file_path')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MessageContentTextAnnotationsFilePathObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of file_path
        if self.file_path:
            _dict['file_path'] = self.file_path.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MessageContentTextAnnotationsFilePathObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "text": obj.get("text"),
            "file_path": MessageContentTextAnnotationsFilePathObjectFilePath.from_dict(obj.get("file_path")) if obj.get("file_path") is not None else None,
            "start_index": obj.get("start_index"),
            "end_index": obj.get("end_index")
        })
        return _obj


