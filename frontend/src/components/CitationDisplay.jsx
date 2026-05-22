import React, { useState } from 'react';
import { motion } from 'framer-motion';
import './CitationDisplay.css';

export default function CitationDisplay({ answer }) {
  const [expandedCitations, setExpandedCitations] = useState({});

  const toggleCitation = (index) => {
    setExpandedCitations(prev => ({
      ...prev,
      [index]: !prev[index]
    }));
  };

  const getTraditionColor = (tradition) => {
    const colors = {
      vedanta: '#FF6B6B',
      buddhism: '#4ECDC4',
      yoga: '#95E1D3',
      samkhya: '#F38181',
      nyaya: '#AA96DA',
      mimamsa: '#FCBAD3',
      general: '#FFD700'
    };
    return colors[tradition] || '#6366f1';
  };

  const getTraditionEmoji = (tradition) => {
    const emojis = {
      vedanta: '✨',
      buddhism: '🔮',
      yoga: '🧘',
      samkhya: '📖',
      nyaya: '🎯',
      mimamsa: '⚡',
      general: '🌟'
    };
    return emojis[tradition] || '🕉️';
  };

  return (
    <motion.div
      className="citation-display"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
    >
      {/* Header with Tradition */}
      <div className="answer-header">
        <div className="tradition-badge" style={{ borderColor: getTraditionColor(answer.tradition) }}>
          <span style={{ color: getTraditionColor(answer.tradition) }}>
            {getTraditionEmoji(answer.tradition)} {answer.tradition.toUpperCase()}
          </span>
        </div>
        <div className="confidence-score">
          <div className="score-bar">
            <motion.div
              className="score-fill"
              initial={{ width: 0 }}
              animate={{ width: `${answer.confidence_score * 100}%` }}
              transition={{ duration: 0.8, ease: 'easeOut' }}
              style={{ backgroundColor: getTraditionColor(answer.tradition) }}
            />
          </div>
          <span className="score-text">{(answer.confidence_score * 100).toFixed(0)}% confidence</span>
        </div>
      </div>

      {/* Answer Body */}
      <motion.div
        className="answer-body"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.6, delay: 0.2 }}
      >
        <p className="answer-text">
          {answer.answer.split('\n').map((line, index) => (
            <React.Fragment key={index}>
              {line}
              {index < answer.answer.split('\n').length - 1 && <br />}
            </React.Fragment>
          ))}
        </p>
      </motion.div>

      {/* Citations Section */}
      {answer.citations && answer.citations.length > 0 && (
        <motion.div
          className="citations-section"
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.3 }}
        >
          <h3 className="citations-title">📚 Sources & Citations</h3>
          <div className="citations-list">
            {answer.citations.map((citation, index) => (
              <motion.div
                key={index}
                className={`citation-card ${expandedCitations[index] ? 'expanded' : ''}`}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.4, delay: 0.3 + index * 0.1 }}
              >
                <button
                  className="citation-header"
                  onClick={() => toggleCitation(index)}
                >
                  <div className="citation-source-info">
                    <span className="citation-source">{citation.source}</span>
                    {citation.verse && (
                      <span className="citation-verse">{citation.verse}</span>
                    )}
                  </div>
                  <span className={`expand-icon ${expandedCitations[index] ? 'rotated' : ''}`}>
                    ▼
                  </span>
                </button>

                {expandedCitations[index] && (
                  <motion.div
                    className="citation-content"
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: 'auto' }}
                    exit={{ opacity: 0, height: 0 }}
                    transition={{ duration: 0.3 }}
                  >
                    <div className="citation-text">
                      <p className="citation-quote">"{citation.text}"</p>
                      {citation.meaning && (
                        <p className="citation-meaning">
                          <strong>Meaning:</strong> {citation.meaning}
                        </p>
                      )}
                      {citation.context && (
                        <p className="citation-context">
                          <strong>Context:</strong> {citation.context}
                        </p>
                      )}
                    </div>
                  </motion.div>
                )}
              </motion.div>
            ))}
          </div>
        </motion.div>
      )}

      {/* Metadata Footer */}
      <motion.div
        className="answer-footer"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.6, delay: 0.4 }}
      >
        <div className="metadata">
          {answer.source && <span className="meta-item">📍 {answer.source}</span>}
          {answer.method && <span className="meta-item">🔍 {answer.method}</span>}
          {answer.timestamp && (
            <span className="meta-item">⏰ {new Date(answer.timestamp).toLocaleTimeString()}</span>
          )}
        </div>
      </motion.div>

      {/* Share/Copy Button */}
      <motion.div
        className="action-buttons"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.6, delay: 0.5 }}
      >
        <button
          className="action-btn copy-btn"
          onClick={() => {
            const text = `${answer.answer}\n\nCitations:\n${answer.citations.map(c => `${c.source}: ${c.text}`).join('\n')}`;
            navigator.clipboard.writeText(text);
            alert('✅ Copied to clipboard!');
          }}
        >
          📋 Copy Answer
        </button>
        <button
          className="action-btn cite-btn"
          onClick={() => {
            const citation = answer.citations[0];
            const text = `Source: ${citation.source}${citation.verse ? ' (' + citation.verse + ')' : ''}\nText: "${citation.text}"${citation.meaning ? '\nMeaning: ' + citation.meaning : ''}`;
            navigator.clipboard.writeText(text);
            alert('✅ Citation copied!');
          }}
        >
          📖 Copy Citation
        </button>
      </motion.div>
    </motion.div>
  );
}