import { UsersApi, UserCreate, UserUpdate } from '../api/api-client';

export async function createUser(
  api: UsersApi,
  data: UserCreate
) {
  try {
    await api.usersCreateUser(data);
  } catch (error: any) {
    throw error.response?.data;
  }
}

export async function listUsers(api: UsersApi) {
  const response = await api.usersListUsers();
  return response.data;
}

export async function getUser(api: UsersApi, userId: number) {
  const response = await api.usersGetUser(userId);
  return response.data;
}

export async function updateUser(
  api: UsersApi,
  userId: number,
  data: UserUpdate
) {
  try {
    await api.usersUpdateUser(userId, data);
  } catch (error: any) {
    throw error.response?.data;
  }
}

export async function deleteUser(api: UsersApi, userId: number) {
  try {
    await api.usersDeleteUser(userId);
  } catch (error: any) {
    throw error.response?.data;
  }
}