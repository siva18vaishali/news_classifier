import React, { useState } from 'react';
import './App.css';

function App() {
  const [headline, setHeadline] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult("Processing...");
    
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ headline })
      });

      const data = await response.json();
      setResult(`This headline is: ${data.label}`);
    } catch (error) {
      console.error('Error:', error);
      setResult('Error: Unable to get prediction');
    }
  };

  // In App.js - Update the return statement with this enhanced UI
  return (
    <div className="App">
      <div className="container">
        <h1>News Headline Classifier</h1>
        <p className="subtitle">Detect satirical news with AI accuracy</p>
      
        <form onSubmit={handleSubmit} className="classifier-form">
          <input
            type="text"
            placeholder="Enter a news headline..."
            value={headline}
            onChange={(e) => setHeadline(e.target.value)}
            required
          />
          <button type="submit" className="predict-button">
            Analyze Headline
          </button>
        </form>

        {result && (
          <div className={`result-box ${result.includes('real') ? 'real' : 'satire'}`}>
            <h3>Analysis Result:</h3>
            <p>{result}</p>
            {result.includes('real') ? (
              <>
                <span className="result-icon">✅</span>
                <p className="confidence">Likely authentic news</p>
              </>
            ) : (
              <>
                <span className="result-icon">🤡</span>
                <p className="confidence">Potential satire detected</p>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
