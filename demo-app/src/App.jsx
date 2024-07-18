import React from 'react';
import './App.css';
import Navbar from './components/NavBar';
import Sidebar from './components/SideBar';
import Footer from './components/Footer';
import MarketData from './components/MarketData';

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="main-content">
        <Sidebar />
        <div className="content">
          <MarketData />
        </div>
      </div>
      <Footer />
    </div>
  );
}

export default App;
