module.exports = {
  apps: [{
    name: 'i6shark',
    script: '/opt/i6shark/src/i6shark',
    cwd: '/opt/i6shark/src',
    user: 'root', // Required for IPv6 manipulation
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production'
    },
    error_file: '/var/log/i6shark/error.log',
    out_file: '/var/log/i6shark/out.log',
    log_file: '/var/log/i6shark/combined.log',
    time: true,
    log_date_format: 'YYYY-MM-DD HH:mm:ss Z',
    // PM2 will restart the app if it crashes
    min_uptime: '10s',
    max_restarts: 10,
    // Graceful shutdown
    kill_timeout: 5000,
    listen_timeout: 3000,
    // Enable cluster mode if needed (not recommended for this app)
    exec_mode: 'fork'
  }]
};
