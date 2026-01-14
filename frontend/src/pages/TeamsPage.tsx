import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { TeamRead, UserRead } from '../api/api-client';
import { parseApiError } from '../errors/parseAPIError';
import { createTeam } from '../services/teamService';
import { teamsApi, usersApi } from '../api/apiConfig';

const TeamsPage: React.FC = () => {
  const [teams, setTeams] = useState<TeamRead[]>([]);
  const [users, setUsers] = useState<UserRead[]>([]);
  const [newTeamName, setNewTeamName] = useState('');
  const [newTeamLeaderId, setNewTeamLeaderId] = useState<number | ''>('');
  const [showLeaderDropdown, setShowLeaderDropdown] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string>('');

  useEffect(() => {
    loadTeams();
    loadUsers();
  }, []);

  const loadTeams = async () => {
    try {
      const response = await teamsApi.teamsListTeams();
      setTeams(response.data);
    } catch (error) {
      console.error('Error loading teams:', error);
    }
  };

  const loadUsers = async () => {
    try {
      const response = await usersApi.usersListUsers();
      setUsers(response.data);
    } catch (error) {
      console.error('Error loading users:', error);
    }
  };

  const createTeamHandler = async () => {
  if (!newTeamName.trim() || newTeamLeaderId === '') return;

  try {
    await createTeam(teamsApi, {
      name: newTeamName,
      leader_id: newTeamLeaderId,
    });

    setNewTeamName('');
    setNewTeamLeaderId('');
    setErrorMessage('');
    loadTeams();
  } catch (err) {
    setErrorMessage(parseApiError(err));
  }
};

  const getLeaderName = (leaderId: number) => {
    const leader = users.find(u => u.id === leaderId);
    return leader ? leader.name : `ID: ${leaderId}`;
  };

  return (
    <div className="teams-page">
      <h2>Equipes</h2>
      {errorMessage && (
        <div className="error-message">
          {errorMessage}
        </div>
      )}
      <div className="create-team">
        <input
          type="text"
          value={newTeamName}
          onChange={(e) => setNewTeamName(e.target.value)}
          placeholder="Nome da equipe"
        />
        <div className="custom-select">
          <div
            className="select-trigger"
            onClick={() => setShowLeaderDropdown(!showLeaderDropdown)}
          >
            {newTeamLeaderId ? getLeaderName(newTeamLeaderId) : 'Selecione o líder'}
            <span className="select-arrow">{showLeaderDropdown ? '▲' : '▼'}</span>
          </div>
          {showLeaderDropdown && (
            <div className="select-options">
              <div
                className="select-option"
                onClick={() => {
                  setNewTeamLeaderId('');
                  setShowLeaderDropdown(false);
                }}
              >
                Selecione o líder
              </div>
              {users.map((user) => (
                <div
                  key={user.id}
                  className="select-option"
                  onClick={() => {
                    setNewTeamLeaderId(user.id);
                    setShowLeaderDropdown(false);
                  }}
                >
                  {user.name}
                </div>
              ))}
            </div>
          )}
        </div>
        <button onClick={createTeamHandler}>Criar Equipe</button>
      </div>
      <ul className="teams-list">
        {teams.map((team) => (
          <li key={team.id}>
            <div>
              <Link to={`/teams/${team.id}`} className="team-link">
                <strong>{team.name}</strong>
              </Link> - Líder: {getLeaderName(team.leader_id)}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TeamsPage;