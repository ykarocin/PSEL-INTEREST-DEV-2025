import React, { useState, useEffect } from 'react';
import { usersApi, teamsApi } from '../api/apiConfig';

const MainPage: React.FC = () => {
  const [stats, setStats] = useState({
    users: 0,
    teams: 0,
    loading: true
  });

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    try {
      const [usersResponse, teamsResponse] = await Promise.all([
        usersApi.usersListUsers(),
        teamsApi.teamsListTeams()
      ]);

      setStats({
        users: usersResponse.data.length,
        teams: teamsResponse.data.length,
        loading: false
      });
    } catch (error) {
      console.error('Error loading stats:', error);
      setStats(prev => ({ ...prev, loading: false }));
    }
  };

  return (
    <div className="main-page">
      <div className="hero-section">
        <h1>Gerenciamento de Equipes</h1>
        <p className="hero-description">
          Sistema completo para gerenciar usuários e equipes de forma eficiente.
          Crie equipes, adicione membros e organize seu projeto de maneira estruturada.
        </p>
      </div>

      <div className="stats-section">
        <div className="stat-card">
          <div className="stat-number">
            {stats.loading ? '...' : stats.users}
          </div>
          <div className="stat-label">Usuários Cadastrados</div>
        </div>
        <div className="stat-card">
          <div className="stat-number">
            {stats.loading ? '...' : stats.teams}
          </div>
          <div className="stat-label">Equipes Criadas</div>
        </div>
      </div>
    </div>
  );
};

export default MainPage;