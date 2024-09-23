# type: ignore
from typing import Any

from config_settings import BasicSettings
from pydantic import Field


class ExampleSettings(BasicSettings):
    """
    ExampleSettings class: define the variables and load values from sources
    """

    var1: str = Field(default=None, description="Variable 1")
    var2: int = Field(default=None, description="Variable 2")

    def model_post_init(self, __context: Any) -> None:
        """
        Perform additional initialization after the model has been initialized.
        """
        self.var1 = "post_init_" + self.var1


class ExampleConfig(ExampleSettings):
    """
    ExampleConfig class: finalize the configuration using variables loaded from sources
    """

    var3: str = Field(default="", description="Variable 3")

    def __init__(self, settings: ExampleSettings):
        super().__init__(settings)
        self.var3 = settings.var1 + str(settings.var2)


t = ExampleSettings()
print(t.model_dump())

tt = ExampleConfig(settings=ExampleSettings())
print(tt.model_dump())
