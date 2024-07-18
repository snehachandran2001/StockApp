import React, { useState, useEffect } from 'react';
import './MarketData.css';

function MarketData() {
  const [globalData, setGlobalData] = useState([]);
  const [indianData, setIndianData] = useState([]);
  const [companyData, setCompanyData] = useState([]);

  useEffect(() => {
    fetchGlobalMarketData();
    fetchIndianMarketData();
    fetchCompanyData();
  }, []);

  const fetchGlobalMarketData = async () => {
    const response = await fetch('/api/global-market-data/');
    const data = await response.json();
    setGlobalData(data);
  };

  const fetchIndianMarketData = async () => {
    const response = await fetch('/api/indian-market-data/');
    const data = await response.json();
    setIndianData(data);
  };

  const fetchCompanyData = async () => {
    const response = await fetch('/api/top-indian-companies-data/');
    const data = await response.json();
    setCompanyData(data);
  };

  return (
    <div className="market-data">
      <section>
        <h2>Global Market Data</h2>
        <div className="data-container">
          {Object.entries(globalData).map(([name, details]) => (
            <div key={name} className="data-card">
              <h3>{name}</h3>
              <p>Close Price: {details.close_price}</p>
              <p>Change: {details.change}</p>
              <p>Percent Change: {details.percent_change}%</p>
            </div>
          ))}
        </div>
      </section>

      <section>
        <h2>Indian Market Data</h2>
        <div className="data-container">
          {Object.entries(indianData).map(([name, details]) => (
            <div key={name} className="data-card">
              <h3>{name}</h3>
              <p>Close Price: {details.close_price}</p>
              <p>Change: {details.change}</p>
              <p>Percent Change: {details.percent_change}%</p>
            </div>
          ))}
        </div>
      </section>

      <section>
        <h2>Top Indian Companies Data</h2>
        <div className="data-container">
          {Object.entries(companyData).map(([name, details]) => (
            <div key={name} className="data-card">
              <h3>{name}</h3>
              <p>Close Price: {details.close_price}</p>
              <p>Change: {details.change}</p>
              <p>Percent Change: {details.percent_change}%</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export default MarketData;
