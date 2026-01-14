import React, { useState, useEffect } from 'react';
import { UserRead, UserCreate, UserUpdate } from '../api/api-client';
import { usersApi } from '../api/apiConfig';
import { parseApiError } from '../errors/parseAPIError';

const UsersPage: React.FC = () => {
  const [users, setUsers] = useState<UserRead[]>([]);
  const [newUserName, setNewUserName] = useState('');
  const [editingUser, setEditingUser] = useState<UserRead | null>(null);
  const [editName, setEditName] = useState('');
  const [createUserError, setCreateUserError] = useState<string>('');
  

  useEffect(() => {
    loadUsers();
  }, []);

  const loadUsers = async () => {
    try {
      const response = await usersApi.usersListUsers();
      setUsers(response.data);
    } catch (error) {
      console.error('Error loading users:', error);
    }
  };

  const createUser = async () => {
    try {
      const userCreate: UserCreate = { name: newUserName };
      await usersApi.usersCreateUser(userCreate);
      setNewUserName('');
      setCreateUserError('');
      loadUsers();
    } catch (error) {
      setCreateUserError(parseApiError(error));
    }
  };

  const updateUser = async () => {
    if (!editingUser || !editName.trim()) return;
    try {
      const userUpdate: UserUpdate = { name: editName };
      await usersApi.usersUpdateUser(editingUser.id, userUpdate);
      setEditingUser(null);
      setEditName('');
      loadUsers();
    } catch (error) {
      console.error('Error updating user:', error);
    }
  };

  const deleteUser = async (id: number) => {
    try {
      await usersApi.usersDeleteUser(id);
      loadUsers();
    } catch (error) {
      console.error('Error deleting user:', error);
    }
  };

  const startEdit = (user: UserRead) => {
    setEditingUser(user);
    setEditName(user.name);
  };

  const cancelEdit = () => {
    setEditingUser(null);
    setEditName('');
  };

  return (
    <div className="users-page">
      <h2>Usuários</h2>
      <div className="create-user">
        <input
          type="text"
          value={newUserName}
          onChange={(e) => { setNewUserName(e.target.value); setCreateUserError(''); }}
          placeholder="Nome do usuário"
        />
        <button onClick={createUser}>Criar Usuário</button>
        {createUserError && (
          <div className="error-message" style={{ color: 'red', marginTop: '5px' }}>
            {createUserError}
          </div>
        )}
      </div>
      <ul className="users-list">
        {users.map((user) => (
          <li key={user.id}>
            {editingUser?.id === user.id ? (
              <div>
                <input
                  type="text"
                  value={editName}
                  onChange={(e) => setEditName(e.target.value)}
                />
                <button onClick={updateUser}>Salvar</button>
                <button onClick={cancelEdit}>Cancelar</button>
              </div>
            ) : (
              <div>
                <span>{user.name}</span>
                <button onClick={() => startEdit(user)}>Editar</button>
                <button onClick={() => deleteUser(user.id)}>Deletar</button>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UsersPage;