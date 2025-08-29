import React, { useState } from "react";

function App() {
  const [skinType, setSkinType] = useState("");
  const [category, setCategory] = useState("");
  const [results, setResults] = useState([]);

  const API_URL = window.location.hostname === "localhost"
      ? "http://localhost:5000/recommend"
      : "http://backend:5000/recommend";

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ skin_type: skinType, category })
      });
      const data = await res.json();
      setResults(data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>VANI-T AI Recommender</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Skin Type:
          <select value={skinType} onChange={(e) => setSkinType(e.target.value)} required>
            <option value="">Select</option>
            <option value="dry">Dry</option>
            <option value="oily">Oily</option>
            <option value="sensitive">Sensitive</option>
            <option value="all">All</option>
          </select>
        </label>
        <br /><br />
        <label>
          Category:
          <select value={category} onChange={(e) => setCategory(e.target.value)}>
            <option value="">Any</option>
            <option value="serum">Serum</option>
            <option value="moisturizer">Moisturizer</option>
            <option value="cleanser">Cleanser</option>
            <option value="sunscreen">Sunscreen</option>
          </select>
        </label>
        <br /><br />
        <button type="submit">Get Recommendations</button>
      </form>

      <h2>Results:</h2>
      <ul>
        {results.length === 0 ? <li>No recommendations yet</li> :
          results.map((r, index) => (
            <li key={index}>
              <a href={r.url} target="_blank" rel="noopener noreferrer">{r.name} ({r.category})</a>
            </li>
          ))
        }
      </ul>
    </div>
  );
}

export default App;