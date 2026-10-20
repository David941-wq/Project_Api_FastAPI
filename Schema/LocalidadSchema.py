from pydantic import BaseModel, ConfigDict


class LocalidadBase(BaseModel):
    nombre: str


class LocalidadCreate(LocalidadBase):
    """Solo para uso interno (seed), no se expone en un endpoint público de creación."""
    pass


class LocalidadResponse(LocalidadBase):
    id: int

    model_config = ConfigDict(from_attributes=True)