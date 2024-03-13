"""Fooocus API models for response"""
from typing import List

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)

from fooocusapi.models.common.task import (
    GeneratedImageResult, TaskType)


class DescribeImageResponse(BaseModel):
    """Describe image result"""
    describe: str


class TaskResponse(BaseModel):
    """Task response"""
    task_id: str = Field(description="Task ID")
    task_type: TaskType | None = Field(
        default=None, description="Task type")
    req_param: dict = Field(description="Task request params")
    in_queue_millis: int = Field(
        default=0, description="Task enqueue time in millisecond")
    start_millis: int = Field(
        default=0, description="Task start time in millisecond")
    finish_millis: int = Field(
        default=0, description="Task finish time in millisecond")
    status: str | None = Field(
        default=None, description="The state of the task in the queue, such as 'pending', 'running', 'completed'")
    task_status: str | None = Field(
        default=None, description="The running state of the task itself, such as 'success', 'failed', 'canceled'")
    progress: int = Field(
        default=0, description="Task progress, 100 is for finished.")
    task_step_preview: str | None = Field(
        default=None, description="Preview base64 image of generation steps at current time")
    webhook_url: str | None = Field(
        default=None, description="Webhook url")
    task_result: List[GeneratedImageResult] = Field(
        default=[], description="Task generation result")


class JobQueueInfo(BaseModel):
    """Job queue info"""
    running: List[TaskResponse] = Field(description="The current running task")
    pending: List[TaskResponse] = Field(description="The current pending in the queue")
    finished: List[TaskResponse] = Field(description="Finished job")


class AllModelNamesResponse(BaseModel):
    """All model names"""
    model_filenames: List[str] = Field(description="All available model filenames")
    lora_filenames: List[str] = Field(description="All available lora filenames")

    model_config = ConfigDict(
        protected_namespaces=('protect_me_', 'also_protect_')
    )


class StopResponse(BaseModel):
    """Stop response"""
    msg: str
