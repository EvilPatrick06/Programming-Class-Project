#!/bin/bash
# PlantUML Watcher Service Manager

SCRIPT_DIR="/workspaces/Programming-Class-Project/Documentation/FlowChartFiles"
LOG_FILE="$SCRIPT_DIR/plantuml_watch.log"
PID_FILE="$SCRIPT_DIR/plantuml_watch.pid"

start_watcher() {
    if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
        echo "⚠️  PlantUML watcher is already running (PID: $(cat $PID_FILE))"
        return 1
    fi
    
    echo "🚀 Starting PlantUML watcher..."
    cd "$SCRIPT_DIR"
    nohup ./watch_plantuml.sh > "$LOG_FILE" 2>&1 &
    echo $! > "$PID_FILE"
    echo "✅ PlantUML watcher started (PID: $!)"
    echo "📝 Logs: $LOG_FILE"
}

stop_watcher() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if kill -0 "$PID" 2>/dev/null; then
            kill "$PID"
            rm -f "$PID_FILE"
            echo "🛑 PlantUML watcher stopped"
        else
            echo "⚠️  Process not running, cleaning up PID file"
            rm -f "$PID_FILE"
        fi
    else
        echo "⚠️  No PID file found"
    fi
}

status_watcher() {
    if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
        echo "✅ PlantUML watcher is running (PID: $(cat $PID_FILE))"
        echo "📝 Log file: $LOG_FILE"
    else
        echo "❌ PlantUML watcher is not running"
    fi
}

case "$1" in
    start)
        start_watcher
        ;;
    stop)
        stop_watcher
        ;;
    restart)
        stop_watcher
        sleep 1
        start_watcher
        ;;
    status)
        status_watcher
        ;;
    logs)
        if [ -f "$LOG_FILE" ]; then
            tail -f "$LOG_FILE"
        else
            echo "❌ No log file found at $LOG_FILE"
        fi
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status|logs}"
        echo ""
        echo "Commands:"
        echo "  start   - Start the PlantUML watcher"
        echo "  stop    - Stop the PlantUML watcher"
        echo "  restart - Restart the PlantUML watcher"
        echo "  status  - Check if the watcher is running"
        echo "  logs    - Show real-time logs"
        exit 1
        ;;
esac