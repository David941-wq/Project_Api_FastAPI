from pydantic import BaseModel


class LocalidadBase(BaseModel):
    nombre: str


class LocalidadCreate(LocalidadBase):
    """Solo para uso interno (seed), no se expone en un endpoint público de creación."""
    pass


class LocalidadResponse(LocalidadBase):
    id: int

    class Config:
        from_attributes = True
