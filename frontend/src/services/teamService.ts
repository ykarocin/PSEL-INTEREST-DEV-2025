import { TeamsApi, TeamCreate, TeamUpdate } from '../api/api-client';

export async function createTeam(
  api: TeamsApi,
  data: TeamCreate
) {
  try {
    await api.teamsCreateTeam(data);
  } catch (error: any) {
    throw error.response?.data;
  }
}

export async function listTeams(api: TeamsApi) {
  const response = await api.teamsListTeams();
  return response.data;
}

export async function getTeam(api: TeamsApi, teamId: number) {
  const response = await api.teamsGetTeam(teamId);
  return response.data;
}

export async function updateTeam(
  api: TeamsApi,
  teamId: number,
  data: TeamUpdate
) {
  try {
    await api.teamsUpdateTeam(teamId, data);
  } catch (error: any) {
    throw error.response?.data;
  }
}

export async function deleteTeam(api: TeamsApi, teamId: number) {
  try {
    await api.teamsDeleteTeam(teamId);
  } catch (error: any) {
    throw error.response?.data;
  }
}