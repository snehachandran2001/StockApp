import React from 'react';
import './SideBar.css';

function Sidebar() {
  return (
    <aside className="sidebar">
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/global">Global Market</a></li>
        <li><a href="/indian">Indian Market</a></li>
        <li><a href="/companies">Top Companies</a></li>
      </ul>
    </aside>
  );
}

export default Sidebar;
