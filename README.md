# Code Translator Agent

An AI-powered agent that translates source code between programming languages, built for integration with [Telex.im](https://telex.im). Users can input code in one language and get a translated version in another language while preserving structure, comments, and formatting.

---

## Features

- Translate code between popular programming languages (Python, Go, Java, Rust, etc.)
- Maintain code formatting and comments during translation
- Handles incomplete requests by asking for missing information (source or target language)
- Provides a conversational interface with users on Telex.im
- Hosted as a Flask web service, integrated via A2A protocol

---

## Tech Stack

- **Backend:** Python 3.11+, Flask
- **AI Integration:** Google Gemini API
- **Platform Integration:** Telex.im (Mastra A2A protocol)
- **Deployment:** Any public hosting (Render, Railway, Replit, etc.)

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip (Python package manager)
- Google Gemini API key
- Telex.im account and access to the organization
