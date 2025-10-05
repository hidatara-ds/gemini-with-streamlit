# Streamlit Gemini Apps

A comprehensive collection of Google Gemini AI-powered applications built with Streamlit, featuring multiple interaction modes including text chat, Q&A, and image analysis capabilities.

## 🚀 Features

- **Text Chat**: Interactive conversational AI with chat history
- **Q&A Mode**: Simple question and answer interface
- **Image Analysis**: Upload and analyze images with AI
- **Streaming Responses**: Real-time response streaming for better user experience
- **Session Management**: Persistent chat history across interactions
- **Modern UI**: Clean and responsive Streamlit interface

## 📁 Project Structure

```
streamlit-gemini-apps/
├── app.py          # Basic Q&A application
├── chat.py        # Streaming chat with history
├── gpt.py          # Enhanced chat interface with styling
├── qachat.py       # Q&A with chat history
├── vision.py       # Image analysis application
├── requirements.txt # Project dependencies
├── env.example     # Environment variables template
├── Dockerfile      # Docker configuration
├── docker-compose.yml # Docker Compose setup
└── README.md       # Project documentation
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/streamlit-gemini-apps.git
   cd streamlit-gemini-apps
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy the example environment file:
   ```bash
   cp env.example .env
   ```
   - Edit the `.env` file and add your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

4. **Get Google API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key to your `.env` file

## 🚀 Usage

### Basic Q&A Application
```bash
streamlit run app.py
```

### Chat with History
```bash
streamlit run chat.py
```

### Enhanced Chat Interface
```bash
streamlit run gpt.py
```

### Q&A with Chat History
```bash
streamlit run qachat.py
```

### Image Analysis
```bash
streamlit run vision.py
```

## 🐳 Docker Support

### Using Docker Compose (Recommended)

1. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env file with your Google API key
   ```

2. **Run with Docker Compose**
   ```bash
   # Run the enhanced chat interface (default)
   docker-compose up

   # Run a specific application
   docker-compose -f docker-compose.yml run --rm app streamlit run app.py
   docker-compose -f docker-compose.yml run --rm chat streamlit run chat.py
   docker-compose -f docker-compose.yml run --rm gpt streamlit run gpt.py
   docker-compose -f docker-compose.yml run --rm qachat streamlit run qachat.py
   docker-compose -f docker-compose.yml run --rm vision streamlit run vision.py
   ```

3. **Access the application**
   - Open your browser and go to `http://localhost:8501`

### Using Docker directly

1. **Build the Docker image**
   ```bash
   docker build -t streamlit-gemini-apps .
   ```

2. **Run the container**
   ```bash
   # Run with environment variables
   docker run -p 8501:8501 --env-file .env streamlit-gemini-apps

   # Run a specific application
   docker run -p 8501:8501 --env-file .env streamlit-gemini-apps streamlit run gpt.py
   ```

### Docker Commands

```bash
# Build the image
docker build -t streamlit-gemini-apps .

# Run the default application (gpt.py)
docker run -p 8501:8501 --env-file .env streamlit-gemini-apps

# Run specific applications
docker run -p 8501:8501 --env-file .env streamlit-gemini-apps streamlit run app.py
docker run -p 8501:8501 --env-file .env streamlit-gemini-apps streamlit run chat.py
docker run -p 8501:8501 --env-file .env streamlit-gemini-apps streamlit run qachat.py
docker run -p 8501:8501 --env-file .env streamlit-gemini-apps streamlit run vision.py

# Run in background
docker run -d -p 8501:8501 --env-file .env --name gemini-app streamlit-gemini-apps

# Stop the container
docker stop gemini-app

# Remove the container
docker rm gemini-app
```

### Development with Docker

For development with hot reload:

```bash
# Run in development mode with file watching
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

# Run specific application in development mode
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up app
```

### Docker Compose Services

The docker-compose.yml includes multiple services for different applications:

| Service | Port | Application | Description |
|---------|------|-------------|-------------|
| `app` | 8501 | gpt.py | Enhanced chat interface (default) |
| `qa` | 8502 | app.py | Basic Q&A application |
| `chat` | 8503 | chat.py | Streaming chat with history |
| `qachat` | 8504 | qachat.py | Q&A with chat history |
| `vision` | 8505 | vision.py | Image analysis application |

### Quick Start with Docker

```bash
# 1. Clone and setup
git clone https://github.com/yourusername/streamlit-gemini-apps.git
cd streamlit-gemini-apps

# 2. Setup environment
cp env.example .env
# Edit .env with your Google API key

# 3. Run with Docker Compose
docker-compose up

# 4. Access the application
# Open http://localhost:8501 in your browser
```

## 📋 Available Applications

| File | Description | Features |
|------|-------------|----------|
| `app.py` | Basic Q&A | Simple question-answer interface |
| `chat.py` | Streaming Chat | Real-time streaming responses |
| `gpt.py` | Enhanced Chat | Styled interface with chat history |
| `qachat.py` | Q&A with History | Question-answer with conversation memory |
| `vision.py` | Image Analysis | Upload and analyze images with AI |

## 🔧 Configuration

### Environment Variables
- `GOOGLE_API_KEY`: Your Google Gemini API key (required)

### Model Configuration
- Default model: `gemini-pro`
- Vision model: `gemini-pro-vision`
- Streaming: Enabled for real-time responses

## 📦 Dependencies

- `streamlit` - Web application framework
- `google-generativeai` - Google Gemini AI SDK
- `python-dotenv` - Environment variable management
- `PIL` (Pillow) - Image processing for vision features

## 🎯 Use Cases

- **Customer Support**: Automated Q&A systems
- **Content Analysis**: Image and text analysis
- **Educational Tools**: Interactive learning assistants
- **Research**: AI-powered research assistance
- **Prototyping**: Rapid AI application development

## 🔒 Security Notes

- Never commit your `.env` file to version control
- Keep your API keys secure and private
- Consider using environment variables in production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google for the Gemini AI API
- Streamlit team for the amazing framework
- Open source community for inspiration

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/gemini-with-streamlit/issues) page
2. Create a new issue with detailed description
3. Contact the maintainers

---

**Made with ❤️ using Streamlit and Google Gemini AI**