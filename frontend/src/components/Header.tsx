import React from 'react'
import { Link } from 'react-router-dom'

interface HeaderProps {
  onToggleSidebar: () => void
}

const Header: React.FC<HeaderProps> = ({ onToggleSidebar }) => {
  return (
    <header className="compact-header">
      <div className="header-content">
        <button className="menu-toggle" onClick={onToggleSidebar}>
          ☰
        </button>
        <Link to="/" className="logo-link">
          <div className="logo-compact">
            <span className="logo-icon">⚔️</span>
            <div className="logo-text-group">
              <span className="logo-title">Interest</span>
              <span className="logo-subtitle">Desafio Técnico</span>
            </div>
          </div>
        </Link>
        
        <nav className="header-nav">
          <Link to="/landing" className="nav-link">Quests</Link>
          <a href="https://github.com/Joao-Marinho-Interest/Seletiva-Interest-Dev-2025" target="_blank" rel="noopener noreferrer" className="nav-link">
            GitHub
          </a>
        </nav>
      </div>
    </header>
  )
}

export default Header
