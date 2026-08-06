#!/usr/bin/env bash
set -e
cd /opt/aitobox/ATBInsight
export PATH=/usr/local/bin:$PATH
source /home/aitobox/miniconda3/bin/activate ATBInsight
if [ -f .env ]; then
  source .env
fi
mkdir -p var/log
echo "[$(date)] Starting daily publisher automation..." >> var/log/cron_publisher.log
agy run --skill skills/daily-publisher/SKILL.md >> var/log/cron_publisher.log 2>&1
echo "[$(date)] Daily publisher automation completed successfully." >> var/log/cron_publisher.log
