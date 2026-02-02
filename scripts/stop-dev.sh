#!/bin/bash
# Stop development environment

echo "🛑 Stopping Docker containers..."
docker-compose down

echo "✅ All services stopped!"
