import { UtilsApi } from '../api/api-client';

export async function healthCheck(api: UtilsApi) {
  const response = await api.utilsHealthCheck();
  return response.data;
}