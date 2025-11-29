#!/usr/bin/env python3
# Write default YAML configuration file for Community Watch Neighborhood

from pathlib import Path

config_dir = Path("community-watch-neighborhood/config")
config_dir.mkdir(parents=True, exist_ok=True)
config_path = config_dir / "default.yaml"

yaml_content = """# Community Watch Neighborhood Configuration

network:
  default_bandwidth: 1000  # Mbps
  backup_bandwidth: 500    # Mbps

storage:
  default_chunk_size: 2097152  # 2MB in bytes
  retention_days: 30
  emergency_replication: true

zones:
  community_center:
    cpu: 8
    memory: 32
    storage: 2000  # GB
    bandwidth: 1000
    priority: high

  police_post:
    cpu: 4
    memory: 16
    storage: 1000
    bandwidth: 500
    priority: high

  school_zone:
    cpu: 4
    memory: 16
    storage: 500
    bandwidth: 300
    priority: medium

  residential_north:
    cpu: 2
    memory: 8
    storage: 250
    bandwidth: 200
    priority: medium

surveillance:
  max_footage_size_mb: 500
  auto_process: true
  alert_threshold_gb: 50

logging:
  level: INFO
  file: logs/community_watch.log
"""

config_path.write_text(yaml_content)
print(f"Wrote configuration to {config_path}")