import { Configuration } from './api-client';
import { TeamsApi, UsersApi, MembersApi } from './api-client';

const apiConfig = new Configuration({
  basePath: import.meta.env.VITE_API_URL,
});

export const teamsApi = new TeamsApi(apiConfig);
export const usersApi = new UsersApi(apiConfig);
export const membersApi = new MembersApi(apiConfig);