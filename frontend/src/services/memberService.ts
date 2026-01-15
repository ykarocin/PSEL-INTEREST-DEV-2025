import { MembersApi, MemberCreate } from '../api/api-client';

export async function addMember(
  api: MembersApi,
  data: MemberCreate
) {
  try {
    await api.membersAddMember(data);
  } catch (error: any) {
    throw error.response?.data;
  }
}

export async function listMembers(api: MembersApi, teamId: number) {
  const response = await api.membersListMembers(teamId);
  return response.data;
}

export async function removeMember(api: MembersApi, teamId: number, userId: number) {
  try {
    await api.membersRemoveMember(teamId, userId);
  } catch (error: any) {
    throw error.response?.data;
  }
}