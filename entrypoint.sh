#!/bin/bash
set -e

echo "🚀 Starting Rasa Action Server..."
rasa run actions --port 5055 --debug
