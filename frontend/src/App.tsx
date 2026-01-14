import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { QuestProvider } from './hooks/useQuestContext'
import MainLayout from './layouts/MainLayout'
import MainPage from './pages/MainPage'
import UsersPage from './pages/UsersPage'
import TeamsPage from './pages/TeamsPage'
import TeamDetailPage from './pages/TeamDetailPage'
import LandingPage from './pages/LandingPage'
import QuestPage from './pages/QuestPage'
import './App.css'

function App() {
  return (
    <QuestProvider>
      <Router>
        <Routes>
          <Route path="/" element={<MainLayout />}>
            <Route index element={<MainPage />} />
            <Route path="users" element={<UsersPage />} />
            <Route path="teams" element={<TeamsPage />} />
            <Route path="teams/:id" element={<TeamDetailPage />} />
            <Route path="landing" element={<LandingPage />} />
            <Route path="quest/:id" element={<QuestPage />} />
          </Route>
        </Routes>
      </Router>
    </QuestProvider>
  )
}

export default App
