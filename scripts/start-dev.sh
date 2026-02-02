#!/bin/bash
# Start development environment

echo "🐳 Starting Docker containers..."
docker-compose up -d

echo "⏳ Waiting for services to be ready..."
sleep 10

echo "✅ Services are running!"
echo "📱 Frontend: http://localhost:3000"
echo "🔌 API Docs: http://localhost:8000/docs"
echo "📊 Qdrant Dashboard: http://localhost:6333/dashboard"
