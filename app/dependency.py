from fastapi.security import OAuth2PasswordBearer, HTTPBearer

from Domain import models
from Infrastracture.database import engine

models.Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
bearer_scheme = HTTPBearer(auto_error=False)
