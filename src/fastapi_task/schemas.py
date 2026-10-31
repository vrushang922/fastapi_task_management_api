from pydantic import BaseModel, ConfigDict
from pydantic import Field

class TaskCreate(BaseModel):
    title : str = Field(..., max_length=100, description="The title of the task") 
    description :str
    completed : bool = False


class TaskResponse(TaskCreate):
    id :int

    model_config = ConfigDict(from_attributes = True)

class TaskUpdate(BaseModel):
    title :str | None =  None
    description :str | None =  None
    completed : bool | None =  None