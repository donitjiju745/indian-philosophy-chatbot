import React from 'react';
import { motion } from 'framer-motion';
import './PhilosophyChat.css';

export default function PhilosophyChat({ onSubmit, loading, userInput, setUserInput }) {
  const handleSubmit = (e) => {
    e.preventDefault();
    if (userInput.trim() && !loading) {
      onSubmit(userInput);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey && !loading) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  // Suggested questions
  const suggestedQuestions = [
    "What is the relationship between Atman and Brahman?",
    "What are the Four Noble Truths in Buddhism?",
    "What is Samadhi in Yoga philosophy?",
    "What is the Prakriti-Purusha relationship?",
    "What is Maya in Vedanta?",
    "Explain Dependent Origination",
    "What is Dharma in Mimamsa?",
    "What are the Pramanas in Nyaya?"
  ];

  return (
    <div className="philosophy-chat">
      <form onSubmit={handleSubmit} className="chat-form">
        <div className="input-wrapper">
          <textarea
            value={userInput}
            onChange={(e) => setUserInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask about Indian philosophy... (e.g., 'What is Atman?')"
            className="chat-input"
            disabled={loading}
            rows="3"
          />
          <motion.button
            type="submit"
            className="send-button"
            disabled={loading || !userInput.trim()}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            {loading ? (
              <span>⚡ Thinking...</span>
            ) : (
              <span>Send 🚀</span>
            )}
          </motion.button>
        </div>
      </form>

      <div className="suggested-questions">
        <p className="suggestion-label">💡 Try these questions:</p>
        <div className="suggestion-buttons">
          {suggestedQuestions.map((question, index) => (
            <motion.button
              key={index}
              className="suggestion-btn"
              onClick={() => {
                setUserInput(question);
              }}
              whileHover={{ scale: 1.02, y: -2 }}
              whileTap={{ scale: 0.98 }}
            >
              {question}
            </motion.button>
          ))}
        </div>
      </div>
    </div>
  );
}