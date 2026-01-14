import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { TeamRead, TeamUpdate, UserRead } from '../api/api-client';
import { teamsApi, usersApi, membersApi } from '../api/apiConfig';
import { parseApiError } from '../errors/parseAPIError';
import { addMember} from '../services/memberService';

const TeamDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const teamId = parseInt(id || '0');

  const [team, setTeam] = useState<TeamRead | null>(null);
  const [leader, setLeader] = useState<UserRead | null>(null);
  const [members, setMembers] = useState<UserRead[]>([]);
  const [allUsers, setAllUsers] = useState<UserRead[]>([]);
  const [loading, setLoading] = useState(true);

  // Estados para edição
  const [isEditing, setIsEditing] = useState(false);
  const [editName, setEditName] = useState('');
  const [editLeaderId, setEditLeaderId] = useState<number | ''>('');

  // Estados para adicionar membro
  const [showAddMember, setShowAddMember] = useState(false);
  const [newMemberId, setNewMemberId] = useState<number | ''>('');
  const [addMemberError, setAddMemberError] = useState<string>('');

  useEffect(() => {
    loadTeamData();
  }, [teamId]);

  const loadTeamData = async () => {
    try {
      setLoading(true);

      // Carregar equipe
      const teamResponse = await teamsApi.teamsGetTeam(teamId);
      const teamData = teamResponse.data;
      setTeam(teamData);

      // Carregar líder
      const leaderResponse = await usersApi.usersGetUser(teamData.leader_id);
      setLeader(leaderResponse.data);

      // Carregar todos os usuários para listas
      const allUsersResponse = await usersApi.usersListUsers();
      setAllUsers(allUsersResponse.data);

      // Carregar membros da equipe
      const membersResponse = await membersApi.membersListMembers(teamId);
      const membersData = membersResponse.data;
      
      // Para cada membro, carregar os dados do usuário
      const membersWithUsers = await Promise.all(
        membersData.map(async (member) => {
          const userResponse = await usersApi.usersGetUser(member.user_id);
          return userResponse.data;
        })
      );
      
      setMembers(membersWithUsers);

    } catch (error) {
      console.error('Error loading team data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleEditTeam = async () => {
    if (!editName.trim() || editLeaderId === '') return;

    try {
      const teamUpdate: TeamUpdate = {
        name: editName,
        leader_id: editLeaderId
      };

      await teamsApi.teamsUpdateTeam(teamId, teamUpdate);
      setIsEditing(false);
      loadTeamData();
    } catch (error) {
      console.error('Error updating team:', error);
    }
  };

  const handleDeleteTeam = async () => {
    if (!window.confirm('Tem certeza que deseja deletar esta equipe?')) return;

    try {
      await teamsApi.teamsDeleteTeam(teamId);
      navigate('/teams');
    } catch (error) {
      console.error('Error deleting team:', error);
    }
  };

  const handleAddMember = async () => {
    if (newMemberId === '') return;

    try {
      await addMember(membersApi,{
        team_id: teamId,
        user_id: newMemberId
      });

      setShowAddMember(false);
      setNewMemberId('');
      setAddMemberError('');
      loadTeamData();
    } catch (error) {
      setAddMemberError(parseApiError(error));
    }
  };

  const handleRemoveMember = async (userId: number) => {
    if (!window.confirm('Tem certeza que deseja remover este membro?')) return;

    try {
      await membersApi.membersRemoveMember(teamId, userId);
      loadTeamData();
    } catch (error) {
      console.error('Error removing member:', error);
    }
  };

  const startEdit = () => {
    if (team) {
      setEditName(team.name);
      setEditLeaderId(team.leader_id);
      setIsEditing(true);
    }
  };

  const cancelEdit = () => {
    setIsEditing(false);
    setEditName('');
    setEditLeaderId('');
  };

  const getAvailableUsers = () => {
    // Usuários que não são o líder atual e não estão na equipe
    return allUsers.filter(user =>
      user.id !== team?.leader_id &&
      !members.some(member => member.id === user.id)
    );
  };

  if (loading) {
    return <div className="team-detail-page">Carregando...</div>;
  }

  if (!team || !leader) {
    return <div className="team-detail-page">Equipe não encontrada</div>;
  }

  return (
    <div className="team-detail-page">
      <div className="team-header">
        <button className="back-button" onClick={() => navigate('/teams')}>
          ← Voltar
        </button>
        <h1>{team.name}</h1>
        <div className="team-actions">
          <button className="edit-button" onClick={startEdit}>
            ✏️ Editar Equipe
          </button>
          <button className="delete-button" onClick={handleDeleteTeam}>
            🗑️ Deletar Equipe
          </button>
        </div>
      </div>

      {isEditing && (
        <div className="edit-form">
          <h3>Editar Equipe</h3>
          <div className="form-group">
            <label>Nome da equipe:</label>
            <input
              type="text"
              value={editName}
              onChange={(e) => setEditName(e.target.value)}
            />
          </div>
          <div className="form-group">
            <label>Líder:</label>
            <select
              value={editLeaderId}
              onChange={(e) => setEditLeaderId(Number(e.target.value) || '')}
            >
              <option value="">Selecione o líder</option>
              {allUsers.map((user) => (
                <option key={user.id} value={user.id}>
                  {user.name}
                </option>
              ))}
            </select>
          </div>
          <div className="form-actions">
            <button onClick={handleEditTeam}>Salvar</button>
            <button onClick={cancelEdit}>Cancelar</button>
          </div>
        </div>
      )}

      <div className="team-info">
        <div className="info-card">
          <h3>Líder da Equipe</h3>
          <p className="leader-name">{leader.name}</p>
        </div>

        <div className="info-card">
          <h3>Membros ({members.length})</h3>
          {members.length === 0 ? (
            <p className="no-members">Nenhum membro adicionado ainda</p>
          ) : (
            <ul className="members-list">
              {members.map((member) => (
                <li key={member.id} className="member-item">
                  <span>{member.name}</span>
                  <button
                    className="remove-member-button"
                    onClick={() => handleRemoveMember(member.id)}
                  >
                    Remover
                  </button>
                </li>
              ))}
            </ul>
          )}

          <div className="add-member-section">
            {!showAddMember ? (
              <button
                className="add-member-button"
                onClick={() => setShowAddMember(true)}
              >
                ➕ Adicionar Membro
              </button>
            ) : (
              <div className="add-member-form">
                <select
                  value={newMemberId}
                  onChange={(e) => { setNewMemberId(Number(e.target.value) || ''); setAddMemberError(''); }}
                >
                  <option value="">Selecione um usuário</option>
                  {getAvailableUsers().map((user) => (
                    <option key={user.id} value={user.id}>
                      {user.name}
                    </option>
                  ))}
                </select>
                {addMemberError && (
                  <div className="error-message" style={{ color: 'red', marginTop: '5px' }}>
                    {addMemberError}
                  </div>
                )}
                <div className="form-actions">
                  <button onClick={handleAddMember}>Adicionar</button>
                  <button onClick={() => { setShowAddMember(false); setAddMemberError(''); }}>Cancelar</button>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default TeamDetailPage;