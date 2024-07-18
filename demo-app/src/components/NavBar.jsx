import React from 'react';
import './NavBar.css';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">Market Dashboard</div>
      <ul className="navbar-menu">
        <li><a href="/">Home</a></li>
        <li><a href="/global">Global Market</a></li>
        <li><a href="/indian">Indian Market</a></li>
        <li><a href="/companies">Top Companies</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;
