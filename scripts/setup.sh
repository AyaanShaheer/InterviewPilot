#!/bin/bash
# Setup script for InterviewPilot

echo "🚀 Setting up InterviewPilot..."

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env from .env.example..."
    cp .env.example .env
    echo "⚠️  Please update .env with your actual credentials"
fi

echo "✅ Setup complete!"
