# 🎯 InterviewPilot

**AI-Powered Mock Interview & Resume Analyzer Platform**

A production-grade full-stack system that provides personalized AI mock interviews based on resume analysis.

---

## 🏗️ Architecture

```
Next.js (Frontend)
        |
     Nginx
        |
    FastAPI (API Gateway)
        |
   -----------------------
   |         |           |
 Resume AI  Interview AI  Go Service
   |                      |
 Qdrant                Postgres/Redis
```

---

## 📦 Tech Stack

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Shadcn/ui** - UI components

### Backend
- **FastAPI** (Python) - API Gateway & orchestration
- **Go** - High-performance microservice for sessions & state management
- **PostgreSQL** - Primary database
- **Redis** - Caching & session storage
- **Qdrant** - Vector database for embeddings

### AI/ML
- **OpenAI GPT-4** - Interview question generation & answer evaluation
- **spaCy** - NLP for skill extraction
- **sentence-transformers** - Resume embeddings

### DevOps
- **Docker & Docker Compose** - Containerization
- **Kubernetes (k3s)** - Orchestration
- **Nginx** - Reverse proxy
- **GitHub Actions** - CI/CD
- **Prometheus & Grafana** - Monitoring

---

## 🚀 Features

- ✅ Resume upload & parsing (PDF support)
- ✅ NLP-based skill extraction
- ✅ Semantic resume search using vector embeddings
- ✅ AI-generated personalized interview questions
- ✅ Real-time answer evaluation with feedback
- ✅ Interview session management
- ✅ Progress tracking & analytics dashboard
- ✅ JWT-based authentication
- ✅ Rate limiting & security

---

## 📁 Project Structure

```
InterviewPilot/
├── frontend/              # Next.js application
├── api-gateway/          # FastAPI backend
├── ai-engine/            # AI/ML pipelines
├── go-service/           # Go microservice
├── nginx/                # Reverse proxy config
├── k8s/                  # Kubernetes manifests
├── scripts/              # Utility scripts
└── docker-compose.yml    # Local development setup
```

---

## 🛠️ Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.11+
- Go 1.21+

### Local Development

```bash
# Clone repository
git clone https://github.com/AyaanShaheer/InterviewPilot.git
cd InterviewPilot

# Copy environment files
cp .env.example .env

# Start all services
docker-compose up -d

# Access application
# Frontend: http://localhost:3000
# API: http://localhost:8000/docs
```

---

## 📚 Documentation

- [API Gateway Documentation](./api-gateway/README.md)
- [AI Engine Documentation](./ai-engine/README.md)
- [Go Service Documentation](./go-service/README.md)
- [Frontend Documentation](./frontend/README.md)
- [Deployment Guide](./docs/DEPLOYMENT.md)

---

## 🔐 Security

- JWT-based authentication
- Rate limiting on all endpoints
- Input validation & sanitization
- Security scanning with Trivy, Bandit, Gosec
- Environment-based secrets management

---

## 📊 Monitoring

- Prometheus metrics
- Grafana dashboards
- Centralized logging with Loki
- Health checks on all services

---

## 🧪 Testing

```bash
# Backend tests
cd api-gateway && pytest

# Frontend tests
cd frontend && npm test

# Go service tests
cd go-service && go test ./...
```

---

## 📝 License

MIT License

---

## 👨‍💻 Author

**Ayaan Shaheer**
- GitHub: [@AyaanShaheer](https://github.com/AyaanShaheer)

---

## 🚧 Development Status

This project is actively under development as part of a production-grade portfolio demonstration.

**Current Phase:** Phase 1 - Project Setup ✅
EOF
```

***

## Step 1.3.2: Create Service-Specific README Files

**API Gateway README:**
```bash
cat > api-gateway/README.md << 'EOF'
# 🔌 API Gateway (FastAPI)

Central orchestration layer that coordinates between AI engines, Go service, and databases.

## 🎯 Responsibilities

- User authentication & authorization (JWT)
- Resume upload & management
- Interview session orchestration
- Answer evaluation coordination
- API rate limiting
- Request validation

## 🛠️ Tech Stack

- FastAPI
- SQLAlchemy (ORM)
- Pydantic (validation)
- PostgreSQL
- Redis
- JWT

## 📂 Structure

```
api-gateway/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── models/
│   ├── schemas/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── middleware/
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md
```

## 🚀 Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📡 API Endpoints

- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /resume/upload` - Upload resume
- `GET /resume/{id}` - Get resume details
- `POST /interview/start` - Start interview session
- `POST /interview/answer` - Submit answer
- `GET /interview/{id}/report` - Get interview report

## 🧪 Testing

```bash
pytest tests/ -v --cov=app
```
EOF
```

**AI Engine README:**
```bash
cat > ai-engine/README.md << 'EOF'
# 🧠 AI Engine

Core ML/NLP pipelines for resume analysis and interview intelligence.

## 🎯 Responsibilities

- PDF text extraction
- NLP skill extraction using spaCy
- Resume embeddings with sentence-transformers
- Vector storage in Qdrant
- Interview question generation (LLM)
- Answer evaluation & feedback (LLM)

## 🛠️ Tech Stack

- Python 3.11+
- spaCy
- sentence-transformers
- Qdrant
- OpenAI API
- PyPDF2

## 📂 Structure

```
ai-engine/
├── app/
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── embeddings.py
│   ├── question_generator.py
│   ├── answer_evaluator.py
│   └── vector_store.py
├── models/
├── tests/
├── requirements.txt
└── README.md
```

## 🚀 Usage

```python
from app.resume_parser import extract_text_from_pdf
from app.skill_extractor import extract_skills

text = extract_text_from_pdf("resume.pdf")
skills = extract_skills(text)
```
EOF
```

**Go Service README:**
```bash
cat > go-service/README.md << 'EOF'
# ⚡ Go Microservice

High-performance service handling session management, state tracking, and rate limiting.

## 🎯 Responsibilities

- Interview session state management
- User session tracking
- Rate limiting logic
- Fast read/write operations
- Real-time metrics

## 🛠️ Tech Stack

- Go 1.21+
- Gin (HTTP framework)
- Redis (state storage)
- PostgreSQL

## 📂 Structure

```
go-service/
├── main.go
├── handlers/
├── services/
├── models/
├── middleware/
├── config/
└── README.md
```

## 🚀 Local Development

```bash
# Install dependencies
go mod download

# Run service
go run main.go

# Build binary
go build -o bin/go-service
```

## 🧪 Testing

```bash
go test ./... -v -cover
```
EOF
```

**Frontend README:**
```bash
cat > frontend/README.md << 'EOF'
# 🎨 Frontend (Next.js)

Modern, responsive UI for InterviewPilot platform.

## 🎯 Features

- User authentication
- Resume upload interface
- Real-time interview chat
- Progress dashboard
- Analytics & reports

## 🛠️ Tech Stack

- Next.js 14
- TypeScript
- Tailwind CSS
- Shadcn/ui
- Zustand (state management)
- React Query

## 📂 Structure

```
frontend/
├── src/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── hooks/
│   └── types/
├── public/
└── README.md
```

## 🚀 Local Development

```bash
# Install dependencies
npm install

# Run dev server
npm run dev

# Build for production
npm run build
```
EOF
```

***

## Step 1.3.3: Create Environment Variable Templates

**Root .env.example:**
```bash
cat > .env.example << 'EOF'
# ========================
# PROJECT CONFIGURATION
# ========================
PROJECT_NAME=InterviewPilot
ENVIRONMENT=development

# ========================
# API GATEWAY (FastAPI)
# ========================
API_PORT=8000
API_HOST=0.0.0.0
SECRET_KEY=your-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=1440

# ========================
# DATABASE (PostgreSQL)
# ========================
POSTGRES_USER=interviewpilot
POSTGRES_PASSWORD=change-me-in-production
POSTGRES_DB=interviewpilot_db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

# ========================
# REDIS
# ========================
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=
REDIS_DB=0
REDIS_URL=redis://${REDIS_HOST}:${REDIS_PORT}/${REDIS_DB}

# ========================
# QDRANT (Vector DB)
# ========================
QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_API_KEY=
QDRANT_URL=http://${QDRANT_HOST}:${QDRANT_PORT}

# ========================
# GO SERVICE
# ========================
GO_SERVICE_PORT=9000
GO_SERVICE_HOST=go-service
GO_SERVICE_URL=http://${GO_SERVICE_HOST}:${GO_SERVICE_PORT}

# ========================
# AI/ML SERVICES
# ========================
OPENAI_API_KEY=your-openai-api-key
MODEL_NAME=gpt-4-turbo-preview
EMBEDDING_MODEL=all-MiniLM-L6-v2
MAX_TOKENS=2000
TEMPERATURE=0.7

# ========================
# FRONTEND
# ========================
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_APP_URL=http://localhost:3000

# ========================
# NGINX
# ========================
NGINX_PORT=80
NGINX_SSL_PORT=443

# ========================
# MONITORING
# ========================
PROMETHEUS_PORT=9090
GRAFANA_PORT=3001
GRAFANA_ADMIN_PASSWORD=admin

# ========================
# SECURITY
# ========================
RATE_LIMIT_PER_MINUTE=60
MAX_UPLOAD_SIZE_MB=10
ALLOWED_ORIGINS=http://localhost:3000,http://localhost

# ========================
# LOGGING
# ========================
LOG_LEVEL=INFO