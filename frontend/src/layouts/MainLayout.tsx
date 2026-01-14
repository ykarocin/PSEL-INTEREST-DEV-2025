import React, { useState } from 'react'
import { Outlet } from 'react-router-dom'
import Header from '../components/Header'
import Footer from '../components/Footer'
import Sidebar from '../components/Sidebar'

const MainLayout: React.FC = () => {
  const [sidebarOpen, setSidebarOpen] = useState(false)

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen)
  }

  return (
    <div className="app-layout">
      <div className="stars"></div>
      <Header onToggleSidebar={toggleSidebar} />
      <div className="content-wrapper">
        <Sidebar isOpen={sidebarOpen} />
        <main className="main-content">
          <Outlet />
        </main>
      </div>
      <Footer />
    </div>
  )
}

export default MainLayout
