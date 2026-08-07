#!/usr/bin/env bash
# ==============================================================================
# ATBInsight Daily Publisher Automation Script
# ==============================================================================

# 1. 基础配置与路径（使用绝对路径，避免依赖工作目录环境）
PROJECT_DIR="/opt/aitobox/ATBInsight"
LOG_DIR="${PROJECT_DIR}/var/log"
LOG_FILE="${LOG_DIR}/cron_publisher.log"
LOCK_FILE="${LOG_DIR}/cron_publisher.lock"
AGY_BIN="/home/aitobox/.local/bin/agy"
SKILL_PATH="${PROJECT_DIR}/skills/daily-publisher/SKILL.md"

# 确保日志与锁目录存在
mkdir -p "${LOG_DIR}"

# 2. 防重机制 (File Lock)
# 避免上次任务挂起或运行超时导致多个任务叠加并发
exec 200>"${LOCK_FILE}"
if ! flock -n 200; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [WARN] Another instance is already running. Exiting." >> "${LOG_FILE}"
    exit 1
fi

# 3. 环境变量补全
export PATH="/home/aitobox/miniconda3/bin:/home/aitobox/.local/bin:/usr/local/bin:$PATH"
export LANG="en_US.UTF-8"
export PYTHONUNBUFFERED=1

echo "==================================================" >> "${LOG_FILE}"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting daily publisher automation..." >> "${LOG_FILE}"

# 4. 进入项目根目录
cd "${PROJECT_DIR}" || {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [ERROR] Failed to cd into ${PROJECT_DIR}" >> "${LOG_FILE}"
    exit 1
}

# 5. 激活 Conda 环境
if [ -f "/home/aitobox/miniconda3/bin/activate" ]; then
    source "/home/aitobox/miniconda3/bin/activate" ATBInsight >> "${LOG_FILE}" 2>&1
fi

# 6. 安全加载 .env 环境变量
# 使用 allexport 确保 .env 中的 KEY=VALUE 会自动 export 成为子进程环境变量
if [ -f .env ]; then
    set -o allexport
    source .env
    set +o allexport
fi

# 7. 日志文件体积自动清理 (超过 50MB 自动裁剪，保留最后 2000 行)
if [ -f "${LOG_FILE}" ] && [ "$(stat -c%s "${LOG_FILE}" 2>/dev/null || echo 0)" -gt 52428800 ]; then
    tail -n 2000 "${LOG_FILE}" > "${LOG_FILE}.tmp" && mv "${LOG_FILE}.tmp" "${LOG_FILE}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [INFO] Log truncated due to size limit." >> "${LOG_FILE}"
fi

# 8. 执行 AGY 指令并精确捕获退出码
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Running skill: ${SKILL_PATH}" >> "${LOG_FILE}"

"${AGY_BIN}" \
    --add-dir /opt/aitobox/ATBInsight \
    --dangerously-skip-permissions   \
    --model gemini-3.6-flash-high   \
    --effort high   \
    --print-timeout 30m   \
    --output-format stream-json   \
    -p "Use skill skills/daily-publisher/SKILL.md to fetch recent 30 days good article and publish" \
     >> "${LOG_FILE}" 2>&1

EXIT_CODE=$?

# 9. 状态判定与记录
if [ ${EXIT_CODE} -eq 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [SUCCESS] Daily publisher automation completed successfully." >> "${LOG_FILE}"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [ERROR] Automation failed with exit code ${EXIT_CODE}." >> "${LOG_FILE}"
fi

exit ${EXIT_CODE}
