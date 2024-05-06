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




from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_server_v2.models.fine_tuning_job_error import FineTuningJobError
from openapi_server_v2.models.fine_tuning_job_hyperparameters import FineTuningJobHyperparameters
from openapi_server_v2.models.fine_tuning_job_integrations_inner import FineTuningJobIntegrationsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FineTuningJob(BaseModel):
    """
    The `fine_tuning.job` object represents a fine-tuning job that has been created through the API. 
    """ # noqa: E501
    id: StrictStr = Field(description="The object identifier, which can be referenced in the API endpoints.")
    created_at: StrictInt = Field(description="The Unix timestamp (in seconds) for when the fine-tuning job was created.")
    error: Optional[FineTuningJobError]
    fine_tuned_model: Optional[StrictStr] = Field(description="The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.")
    finished_at: Optional[StrictInt] = Field(description="The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.")
    hyperparameters: FineTuningJobHyperparameters
    model: StrictStr = Field(description="The base model that is being fine-tuned.")
    object: StrictStr = Field(description="The object type, which is always \"fine_tuning.job\".")
    organization_id: StrictStr = Field(description="The organization that owns the fine-tuning job.")
    result_files: List[StrictStr] = Field(description="The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](/docs/api-reference/files/retrieve-contents).")
    status: StrictStr = Field(description="The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.")
    trained_tokens: Optional[StrictInt] = Field(description="The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.")
    training_file: StrictStr = Field(description="The file ID used for training. You can retrieve the training data with the [Files API](/docs/api-reference/files/retrieve-contents).")
    validation_file: Optional[StrictStr] = Field(description="The file ID used for validation. You can retrieve the validation results with the [Files API](/docs/api-reference/files/retrieve-contents).")
    integrations: Optional[Annotated[List[FineTuningJobIntegrationsInner], Field(max_length=5)]] = Field(default=None, description="A list of integrations to enable for this fine-tuning job.")
    seed: StrictInt = Field(description="The seed used for the fine-tuning job.")
    estimated_finish: Optional[StrictInt] = Field(default=None, description="The Unix timestamp (in seconds) for when the fine-tuning job is estimated to finish. The value will be null if the fine-tuning job is not running.")
    __properties: ClassVar[List[str]] = ["id", "created_at", "error", "fine_tuned_model", "finished_at", "hyperparameters", "model", "object", "organization_id", "result_files", "status", "trained_tokens", "training_file", "validation_file", "integrations", "seed", "estimated_finish"]

    @field_validator('object')
    def object_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('fine_tuning.job'):
            raise ValueError("must be one of enum values ('fine_tuning.job')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('validating_files', 'queued', 'running', 'succeeded', 'failed', 'cancelled'):
            raise ValueError("must be one of enum values ('validating_files', 'queued', 'running', 'succeeded', 'failed', 'cancelled')")
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
        """Create an instance of FineTuningJob from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hyperparameters
        if self.hyperparameters:
            _dict['hyperparameters'] = self.hyperparameters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in integrations (list)
        _items = []
        if self.integrations:
            for _item in self.integrations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['integrations'] = _items
        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if fine_tuned_model (nullable) is None
        # and model_fields_set contains the field
        if self.fine_tuned_model is None and "fine_tuned_model" in self.model_fields_set:
            _dict['fine_tuned_model'] = None

        # set to None if finished_at (nullable) is None
        # and model_fields_set contains the field
        if self.finished_at is None and "finished_at" in self.model_fields_set:
            _dict['finished_at'] = None

        # set to None if trained_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.trained_tokens is None and "trained_tokens" in self.model_fields_set:
            _dict['trained_tokens'] = None

        # set to None if validation_file (nullable) is None
        # and model_fields_set contains the field
        if self.validation_file is None and "validation_file" in self.model_fields_set:
            _dict['validation_file'] = None

        # set to None if integrations (nullable) is None
        # and model_fields_set contains the field
        if self.integrations is None and "integrations" in self.model_fields_set:
            _dict['integrations'] = None

        # set to None if estimated_finish (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_finish is None and "estimated_finish" in self.model_fields_set:
            _dict['estimated_finish'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FineTuningJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "error": FineTuningJobError.from_dict(obj.get("error")) if obj.get("error") is not None else None,
            "fine_tuned_model": obj.get("fine_tuned_model"),
            "finished_at": obj.get("finished_at"),
            "hyperparameters": FineTuningJobHyperparameters.from_dict(obj.get("hyperparameters")) if obj.get("hyperparameters") is not None else None,
            "model": obj.get("model"),
            "object": obj.get("object"),
            "organization_id": obj.get("organization_id"),
            "result_files": obj.get("result_files"),
            "status": obj.get("status"),
            "trained_tokens": obj.get("trained_tokens"),
            "training_file": obj.get("training_file"),
            "validation_file": obj.get("validation_file"),
            "integrations": [FineTuningJobIntegrationsInner.from_dict(_item) for _item in obj.get("integrations")] if obj.get("integrations") is not None else None,
            "seed": obj.get("seed"),
            "estimated_finish": obj.get("estimated_finish")
        })
        return _obj


