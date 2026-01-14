import React from 'react';
import { Link } from 'react-router-dom';

interface SidebarProps {
  isOpen: boolean;
}

const Sidebar: React.FC<SidebarProps> = ({ isOpen }) => {
  return (
    <nav className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
      <ul>
        <li><Link to="/users">Usuários</Link></li>
        <li><Link to="/teams">Equipes</Link></li>
      </ul>
    </nav>
  );
};

export default Sidebar;