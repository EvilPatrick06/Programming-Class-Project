#!/bin/bash
# PlantUML Auto-regeneration Script
# Watches GameFlowchart.puml and automatically regenerates PNG when changed

echo "🔍 Watching GameFlowchart.puml for changes..."
echo "📝 Any changes will automatically regenerate the PNG"
echo "⏹️  Press Ctrl+C to stop"
echo ""

cd /workspaces/Programming-Class-Project/Documentation/FlowChartFiles

# Function to generate diagram
generate_diagram() {
    echo "🔄 Change detected! Regenerating PNG..."
    java -jar plantuml.jar GameFlowchart.puml
    if [ $? -eq 0 ]; then
        # Move the generated PNG to the Documentation folder
        mv GameFlowchart.png ../GameFlowchart.png
        echo "✅ PNG updated successfully in Documentation folder at $(date)"
    else
        echo "❌ Error generating PNG at $(date)"
    fi
    echo ""
}

# Generate once at start
echo "🚀 Initial PNG generation..."
generate_diagram

# Watch for file changes
while inotifywait -e modify,close_write GameFlowchart.puml 2>/dev/null; do
    generate_diagram
done