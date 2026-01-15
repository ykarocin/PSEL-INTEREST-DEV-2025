import { errorMessages, ApiErrorCode } from './errorMessages';

export function parseApiError(error: any): string {
  const code = error?.error_code as ApiErrorCode;

  if (code && errorMessages[code]) {
    return errorMessages[code];
  }

  return 'Erro inesperado. Tente novamente.';
}
