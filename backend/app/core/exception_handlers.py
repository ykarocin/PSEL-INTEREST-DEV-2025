from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions import DomainError, NotFoundError, BusinessRuleError

def domain_exception_handler(request: Request, exc: DomainError):
    """
    Converte qualquer exceção de domínio em resposta HTTP padrão.
    """
    status_code = 400  # padrão para erros de regra de negócio

    if isinstance(exc, NotFoundError):
        status_code = 404

    return JSONResponse(
        status_code=status_code,
        content={"error_code": exc.error_code}
    )
