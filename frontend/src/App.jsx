import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';
import './App.css';
import ThreeDOrb from './components/ThreeDOrb';
import PhilosophyChat from './components/PhilosophyChat';
import CitationDisplay from './components/CitationDisplay';

const API_BASE_URL = 'https://indian-philosophy-chatbot.vercel.app';

export default function App() {
  const [questions, setQuestions] = useState([]);
  const [currentAnswer, setCurrentAnswer] = useState(null);
  const [loading, setLoading] = useState(false);
  const [selectedTradition, setSelectedTradition] = useState('general');
  const [userInput, setUserInput] = useState('');
  const [activeTab, setActiveTab] = useState('chat'); // 'chat', 'browse', 'search'
  const [searchResults, setSearchResults] = useState([]);
  const [error, setError] = useState(null);

  // Fetch available questions on mount
  useEffect(() => {
    fetchAvailableQuestions();
  }, []);

  const fetchAvailableQuestions = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/available-questions`);
      setQuestions(response.data.questions);
    } catch (err) {
      console.error('Error fetching questions:', err);
      setError('Failed to load questions');
    }
  };

  const handleChat = async (question) => {
    if (!question.trim()) {
      setError('Please enter a question');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const response = await axios.post(`${API_BASE_URL}/chat`, {
        question: question,
        philosophical_tradition: selectedTradition,
        language: 'english'
      });

      setCurrentAnswer(response.data);
      setUserInput('');
    } catch (err) {
      console.error('Error:', err);
      setError('Failed to get response. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (keyword) => {
    if (!keyword.trim()) return;

    try {
      const response = await axios.get(`${API_BASE_URL}/search`, {
        params: { keyword: keyword }
      });
      setSearchResults(response.data.results);
    } catch (err) {
      console.error('Error searching:', err);
      setError('Search failed');
    }
  };

  const handleSelectQuestion = async (questionKey) => {
    setLoading(true);
    setError(null);

    try {
      const response = await axios.get(`${API_BASE_URL}/question/${questionKey}`);
      setCurrentAnswer(response.data);
      setActiveTab('chat');
    } catch (err) {
      console.error('Error:', err);
      setError('Failed to load question');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      {/* 3D Background Orb */}
      <div className="background-orb">
        <ThreeDOrb />
      </div>

      {/* Main Content */}
      <motion.div
        className="main-content"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.8 }}
      >
        {/* Header */}
        <motion.header
          className="header"
          initial={{ y: -50 }}
          animate={{ y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <h1>🕉️ Indian Philosophy Chatbot</h1>
          <p>Explore ancient wisdom with AI-powered insights</p>
        </motion.header>

        {/* Navigation Tabs */}
        <nav className="nav-tabs">
          <button
            className={`tab-btn ${activeTab === 'chat' ? 'active' : ''}`}
            onClick={() => setActiveTab('chat')}
          >
            💬 Chat
          </button>
          <button
            className={`tab-btn ${activeTab === 'browse' ? 'active' : ''}`}
            onClick={() => setActiveTab('browse')}
          >
            📚 Browse
          </button>
          <button
            className={`tab-btn ${activeTab === 'search' ? 'active' : ''}`}
            onClick={() => setActiveTab('search')}
          >
            🔍 Search
          </button>
        </nav>

        {/* Content Area */}
        <div className="content-area">
          {/* CHAT TAB */}
          {activeTab === 'chat' && (
            <motion.div
              className="tab-content chat-section"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.5 }}
            >
              <div className="tradition-selector">
                <label>Select Tradition:</label>
                <div className="tradition-buttons">
                  {[
                    { id: 'general', label: '🌟 All Traditions', color: '#FFD700' },
                    { id: 'vedanta', label: '✨ Vedanta', color: '#FF6B6B' },
                    { id: 'buddhism', label: '🔮 Buddhism', color: '#4ECDC4' },
                    { id: 'yoga', label: '🧘 Yoga', color: '#95E1D3' },
                    { id: 'samkhya', label: '📖 Samkhya', color: '#F38181' },
                    { id: 'nyaya', label: '🎯 Nyaya', color: '#AA96DA' },
                    { id: 'mimamsa', label: '⚡ Mimamsa', color: '#FCBAD3' }
                  ].map(tradition => (
                    <motion.button
                      key={tradition.id}
                      className={`tradition-btn ${selectedTradition === tradition.id ? 'selected' : ''}`}
                      style={{
                        borderColor: tradition.color,
                        color: selectedTradition === tradition.id ? '#fff' : tradition.color,
                        backgroundColor: selectedTradition === tradition.id ? tradition.color : 'transparent'
                      }}
                      onClick={() => setSelectedTradition(tradition.id)}
                      whileHover={{ scale: 1.05 }}
                      whileTap={{ scale: 0.95 }}
                    >
                      {tradition.label}
                    </motion.button>
                  ))}
                </div>
              </div>

              <PhilosophyChat
                onSubmit={handleChat}
                loading={loading}
                userInput={userInput}
                setUserInput={setUserInput}
              />

              {error && (
                <motion.div
                  className="error-message"
                  initial={{ opacity: 0, y: -10 }}
                  animate={{ opacity: 1, y: 0 }}
                >
                  ❌ {error}
                </motion.div>
              )}

              {loading && (
                <motion.div
                  className="loading-spinner"
                  animate={{ rotate: 360 }}
                  transition={{ repeat: Infinity, duration: 2 }}
                >
                  ⚡
                </motion.div>
              )}

              {currentAnswer && !loading && (
                <CitationDisplay answer={currentAnswer} />
              )}
            </motion.div>
          )}

          {/* BROWSE TAB */}
          {activeTab === 'browse' && (
            <motion.div
              className="tab-content browse-section"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.5 }}
            >
              <h2>📚 Browse All Questions</h2>
              <div className="questions-grid">
                {questions.map(q => (
                  <motion.div
                    key={q.key}
                    className="question-card"
                    whileHover={{ scale: 1.02, y: -5 }}
                    whileTap={{ scale: 0.98 }}
                    onClick={() => handleSelectQuestion(q.key)}
                  >
                    <div className="tradition-badge">{q.tradition}</div>
                    <p className="question-text">{q.question}</p>
                    <button className="read-more">Read Answer →</button>
                  </motion.div>
                ))}
              </div>
            </motion.div>
          )}

          {/* SEARCH TAB */}
          {activeTab === 'search' && (
            <motion.div
              className="tab-content search-section"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              transition={{ duration: 0.5 }}
            >
              <div className="search-box">
                <input
                  type="text"
                  placeholder="Search by keyword (e.g., Atman, Brahman, Samadhi)..."
                  onKeyPress={e => {
                    if (e.key === 'Enter') {
                      handleSearch(e.target.value);
                    }
                  }}
                  className="search-input"
                />
                <button
                  className="search-btn"
                  onClick={e => handleSearch(e.target.parentElement.querySelector('.search-input').value)}
                >
                  🔍 Search
                </button>
              </div>

              {searchResults.length > 0 && (
                <div className="search-results">
                  <h3>Found {searchResults.length} results:</h3>
                  {searchResults.map(result => (
                    <motion.div
                      key={result.key}
                      className="search-result-item"
                      initial={{ opacity: 0, x: -20 }}
                      animate={{ opacity: 1, x: 0 }}
                      onClick={() => handleSelectQuestion(result.key)}
                    >
                      <div className="result-content">
                        <p className="result-question">{result.question}</p>
                        <p className="result-tradition">📌 {result.tradition}</p>
                        <div className="result-score">Match: {(result.match_score * 100).toFixed(0)}%</div>
                      </div>
                      <button className="view-btn">View →</button>
                    </motion.div>
                  ))}
                </div>
              )}
            </motion.div>
          )}
        </div>

        {/* Footer */}
        <motion.footer
          className="footer"
          initial={{ y: 50 }}
          animate={{ y: 0 }}
          transition={{ duration: 0.6 }}
        >
          <p>🕉️ Explore the wisdom of Indian philosophy with citations from classical texts</p>
          <p className="api-status">✅ Backend: http://localhost:8000 | Docs: /docs</p>
        </motion.footer>
      </motion.div>
    </div>
  );
}